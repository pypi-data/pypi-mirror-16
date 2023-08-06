"""Utility to provide submission and comment statistics in a subreddit."""
from __future__ import print_function
import codecs
import re
import sys
import time
from collections import defaultdict
from datetime import datetime
from praw import Reddit
from praw.models import Redditor, Submission
from six import iteritems, text_type as tt
from .helpers import AGENT, arg_parser, check_for_updates

DAYS_IN_SECONDS = 60 * 60 * 24
MAX_BODY_SIZE = 40000


def safe_title(submission):
    """Return titles with newlines replaced by spaces and stripped."""
    return submission.title.replace('\n', ' ').strip()


class SubRedditStats(object):
    """Contain all the functionality of the subreddit_stats command."""

    post_prefix = tt('Subreddit Stats:')
    post_header = tt('---\n###{}\n')
    post_footer = tt('>Generated with [BBoe](/u/bboe)\'s [Subreddit Stats]'
                     '(https://github.com/praw-dev/prawtools)  \n{}'
                     'SRS Marker: {}')
    re_marker = re.compile('SRS Marker: (\d+)')

    @staticmethod
    def _previous_max(submission):
        return float(SubRedditStats.re_marker.findall(submission.selftext)[-1])

    @staticmethod
    def _permalink(item):
        if isinstance(item, Submission):
            return tt('/comments/{}').format(item.id)
        else:  # comment
            return tt('/comments/{}//{}?context=1').format(item.submission.id,
                                                           item.id)

    @staticmethod
    def _pts(points):
        return '1 pt' if points == 1 else '{} pts'.format(points)

    @staticmethod
    def _user(user):
        if user is None:
            return '_deleted_'
        elif isinstance(user, Redditor):
            user = str(user)
        return tt('[{}](/user/{})').format(user.replace('_', '\_'), user)

    def __init__(self, subreddit, site, verbosity, distinguished):
        """Initialize the SubRedditStats instance with config options."""
        self.reddit = Reddit(site, disable_update_check=True, user_agent=AGENT)
        self.subreddit = self.reddit.subreddit(subreddit)
        self.verbosity = verbosity
        self.distinguished = distinguished
        self.submissions = []
        self.comments = []
        self.submitters = defaultdict(list)
        self.commenters = defaultdict(list)
        self.min_date = 0
        self.max_date = time.time() - DAYS_IN_SECONDS * 3
        self.prev_srs = None

    def msg(self, msg, level, overwrite=False):
        """Output a messaage to the screen if the verbosity is sufficient."""
        if self.verbosity and self.verbosity >= level:
            sys.stdout.write(msg)
            if overwrite:
                sys.stdout.write('\r')
                sys.stdout.flush()
            else:
                sys.stdout.write('\n')

    def prev_stat(self, prev_id):
        """Load the previous subreddit stat."""
        self.prev_srs = self.reddit.submission(prev_id)
        self.min_date = self._previous_max(self.prev_srs)

    def fetch_recent_submissions(self, max_duration, after, exclude_self,
                                 exclude_link, since_last=True):
        """Fetch recent submissions in subreddit with boundaries.

        Does not include posts within the last three days as their scores may
        not be representative.

        :param max_duration: When set, specifies the number of days to include
        :param after: When set, fetch all submission after this submission id.
        :param exclude_self: When true, don't include self posts.
        :param exclude_link:  When true, don't include links.
        :param since_last: When true use info from last submission to determine
            the stop point
        :returns: True if any submissions were found.

        """
        if exclude_self and exclude_link:
            raise TypeError('Cannot set both exclude_self and exclude_link.')
        if max_duration:
            self.min_date = self.max_date - DAYS_IN_SECONDS * max_duration
        params = {'after': after} if after else None
        self.msg('DEBUG: Fetching submissions', 1)
        for submission in self.subreddit.new(limit=None, params=params):
            if submission.created_utc <= self.min_date:
                break
            if since_last and submission.title.startswith(self.post_prefix) \
               and submission.author == self.reddit.config.username:
                # Use info in this post to update the min_date
                # And don't include this post
                self.msg(tt('Found previous: {}')
                         .format(safe_title(submission)), 2)
                if self.prev_srs is None:  # Only use the most recent
                    self.min_date = max(self.min_date,
                                        self._previous_max(submission))
                    self.prev_srs = submission
                continue
            if submission.created_utc > self.max_date:
                continue
            if exclude_self and submission.is_self:
                continue
            if exclude_link and not submission.is_self:
                continue
            self.submissions.append(submission)
        num_submissions = len(self.submissions)
        self.msg('DEBUG: Found {} submissions'.format(num_submissions), 1)
        if num_submissions == 0:
            return False

        # Update real min and max dates
        self.submissions.sort(key=lambda x: x.created_utc)
        self.min_date = self.submissions[0].created_utc
        self.max_date = self.submissions[-1].created_utc
        return True

    def fetch_top_submissions(self, top, exclude_self, exclude_link):
        """Fetch top 1000 submissions by some top value.

        :param top: One of week, month, year, all
        :param exclude_self: When true, don't include self posts.
        :param exclude_link: When true, include only self posts
        :returns: True if any submissions were found.

        """
        if exclude_self and exclude_link:
            raise TypeError('Cannot set both exclude_self and exclude_link.')
        if top not in ('day', 'week', 'month', 'year', 'all'):
            raise TypeError('{!r} is not a valid top value'.format(top))
        self.msg('DEBUG: Fetching submissions', 1)
        params = {'t': top}
        for submission in self.subreddit.top(limit=None, params=params):
            if exclude_self and submission.is_self:
                continue
            if exclude_link and not submission.is_self:
                continue
            self.submissions.append(submission)
        num_submissions = len(self.submissions)
        self.msg('DEBUG: Found {} submissions'.format(num_submissions), 1)
        if num_submissions == 0:
            return False

        # Update real min and max dates
        self.submissions.sort(key=lambda x: x.created_utc)
        self.min_date = self.submissions[0].created_utc
        self.max_date = self.submissions[-1].created_utc
        return True

    def process_submitters(self):
        """Group submissions by author."""
        self.msg('DEBUG: Processing Submitters', 1)
        for submission in self.submissions:
            if submission.author and (self.distinguished or
                                      submission.distinguished is None):
                self.submitters[str(submission.author)].append(submission)

    def process_commenters(self):
        """Group comments by author."""
        num = len(self.submissions)
        self.msg('DEBUG: Processing Commenters on {} submissions'.format(num),
                 1)
        for i, submission in enumerate(self.submissions):
            submission.comment_sort = 'top'
            self.msg('{}/{} submissions'.format(i + 1, num), 2, overwrite=True)
            if submission.num_comments == 0:
                continue
            skipped = submission.comments.replace_more()
            if skipped:
                skip_num = sum(x.count for x in skipped)
                print('Ignored {} comments ({} MoreComment objects)'
                      .format(skip_num, len(skipped)))
            comments = [x for x in submission.comments.list() if
                        self.distinguished or x.distinguished is None]
            self.comments.extend(comments)
        for comment in self.comments:
            if comment.author:
                self.commenters[str(comment.author)].append(comment)

    def basic_stats(self):
        """Return a markdown representation of simple statistics."""
        sub_score = sum(x.score for x in self.submissions)
        comm_score = sum(x.score for x in self.comments)
        sub_duration = self.max_date - self.min_date
        sub_rate = (86400. * len(self.submissions) / sub_duration
                    if sub_duration else len(self.submissions))

        # Compute comment rate
        if self.comments:
            self.comments.sort(key=lambda x: x.created_utc)
            duration = (self.comments[-1].created_utc -
                        self.comments[0].created_utc)
            comm_rate = (86400. * len(self.comments) / duration
                         if duration else len(self.comments))
        else:
            comm_rate = 0

        values = [('Total', len(self.submissions), len(self.comments)),
                  ('Rate (per day)', '{:.2f}'.format(sub_rate),
                   '{:.2f}'.format(comm_rate)),
                  ('Unique Redditors', len(self.submitters),
                   len(self.commenters)),
                  ('Combined Score', sub_score, comm_score)]

        retval = 'Period: {:.2f} days\n\n'.format(sub_duration / 86400.)
        retval += '||Submissions|Comments|\n:-:|--:|--:\n'
        for quad in values:
            retval += '__{}__|{}|{}\n'.format(*quad)
        return retval + '\n'

    def top_submitters(self, num, num_submissions):
        """Return a markdown representation of the top submitters."""
        num = min(num, len(self.submitters))
        if num <= 0:
            return ''

        top_submitters = sorted(iteritems(self.submitters), reverse=True,
                                key=lambda x: (sum(y.score for y in x[1]),
                                               len(x[1])))[:num]

        retval = self.post_header.format('Top Submitters\' Top Submissions')
        for (author, submissions) in top_submitters:
            retval += '0. {}, {} submission{}: {}\n'.format(
                self._pts(sum(x.score for x in submissions)), len(submissions),
                's' if len(submissions) > 1 else '', self._user(author))
            for sub in sorted(submissions, reverse=True,
                              key=lambda x: x.score)[:num_submissions]:
                title = safe_title(sub)
                if sub.permalink != sub.url:
                    retval += tt('  0. [{}]({})').format(title, sub.url)
                else:
                    retval += tt('  0. {}').format(title)
                retval += ' ({}, [{} comment{}]({}))\n'.format(
                    self._pts(sub.score), sub.num_comments,
                    's' if sub.num_comments > 1 else '',
                    self._permalink(sub))
            retval += '\n'
        return retval

    def top_commenters(self, num):
        """Return a markdown representation of the top commenters."""
        num = min(num, len(self.commenters))
        if num <= 0:
            return ''

        top_commenters = sorted(iteritems(self.commenters), reverse=True,
                                key=lambda x: (sum(y.score for y in x[1]),
                                               len(x[1])))[:num]

        retval = self.post_header.format('Top Commenters')
        for author, comments in top_commenters:
            retval += '0. {} ({}, {} comment{})\n'.format(
                self._user(author), self._pts(sum(x.score for x in comments)),
                len(comments), 's' if len(comments) > 1 else '')
        return '{}\n'.format(retval)

    def top_submissions(self, num):
        """Return a markdown representation of the top submissions."""
        num = min(num, len(self.submissions))
        if num <= 0:
            return ''

        top_submissions = sorted(
            [x for x in self.submissions if self.distinguished or
             x.distinguished is None],
            reverse=True, key=lambda x: x.score)[:num]

        if not top_submissions:
            return ''

        retval = self.post_header.format('Top Submissions')
        for sub in top_submissions:
            title = safe_title(sub)
            if sub.permalink != sub.url:
                retval += tt('0. [{}]({})').format(title, sub.url)
            else:
                retval += tt('0. {}').format(title)
            retval += ' by {} ({}, [{} comment{}]({}))\n'.format(
                self._user(sub.author), self._pts(sub.score), sub.num_comments,
                's' if sub.num_comments > 1 else '',
                self._permalink(sub))
        return tt('{}\n').format(retval)

    def top_comments(self, num):
        """Return a markdown representation of the top comments."""
        num = min(num, len(self.comments))
        if num <= 0:
            return ''

        top_comments = sorted(self.comments, reverse=True,
                              key=lambda x: x.score)[:num]
        retval = self.post_header.format('Top Comments')
        for comment in top_comments:
            title = safe_title(comment.submission)
            retval += tt('0. {}: {}\'s [comment]({}) in {}\n').format(
                self._pts(comment.score), self._user(comment.author),
                self._permalink(comment), title)
        return tt('{}\n').format(retval)

    def publish_results(self, subreddit, submitters, commenters, submissions,
                        comments, top, debug=False):
        """Submit the results to the subreddit. Has no return value (None)."""
        def timef(timestamp, date_only=False):
            """Return a suitable string representaation of the timestamp."""
            dtime = datetime.fromtimestamp(timestamp)
            if date_only:
                retval = dtime.strftime('%Y-%m-%d')
            else:
                retval = dtime.strftime('%Y-%m-%d %H:%M PDT')
            return retval

        if self.prev_srs:
            prev = '[Prev SRS]({})  \n'.format(self._permalink(self.prev_srs))
        else:
            prev = ''

        basic = self.basic_stats()
        t_commenters = self.top_commenters(commenters)
        t_submissions = self.top_submissions(submissions)
        t_comments = self.top_comments(comments)
        footer = self.post_footer.format(prev, self.max_date)

        body = ''
        num_submissions = 10
        while body == '' or len(body) > MAX_BODY_SIZE and num_submissions > 2:
            t_submitters = self.top_submitters(submitters, num_submissions)
            body = (basic + t_submitters + t_commenters + t_submissions +
                    t_comments + footer)
            num_submissions -= 1

        if len(body) > MAX_BODY_SIZE:
            print('The resulting message is too big. Not submitting.')
            debug = True

        # Set the initial title
        base_title = '{} {} {}posts from {} to {}'.format(
            self.post_prefix, str(self.subreddit),
            'top ' if top else '', timef(self.min_date, True),
            timef(self.max_date))

        submitted = False
        while not debug and not submitted:
            if subreddit:  # Verify the user wants to submit to the subreddit
                msg = ('You are about to submit to subreddit {} as {}.\n'
                       'Are you sure? yes/[no]: '
                       .format(subreddit, self.reddit.config.username))
                sys.stdout.write(msg)
                sys.stdout.flush()
                if sys.stdin.readline().strip().lower() not in ['y', 'yes']:
                    subreddit = None
            elif not subreddit:  # Prompt for the subreddit to submit to
                msg = ('Please enter a subreddit to submit to (press return to'
                       ' abort): ')
                sys.stdout.write(msg)
                sys.stdout.flush()
                subreddit = sys.stdin.readline().strip()
                if not subreddit:
                    print('Submission aborted\n')
                    debug = True

            # Vary the title depending on where posting
            if str(self.subreddit) == subreddit:
                title = '{} {}posts from {} to {}'.format(
                    self.post_prefix, 'top ' if top else '',
                    timef(self.min_date, True), timef(self.max_date))
            else:
                title = base_title

            if subreddit:
                subreddit = self.reddit.subreddit(subreddit)
                try:  # Attempt to make the submission
                    print(subreddit.submit(title, selftext=body).permalink)
                    submitted = True
                except Exception as error:
                    print('The submission failed: {!r}'.format(error))
                    subreddit = None

        if not submitted:
            print(base_title)
            print(body)

    def save_csv(self, filename):
        """Create csv file containing comments and submissions by author."""
        redditors = set(self.submitters.keys()).union(self.commenters.keys())
        mapping = dict((x.lower(), x) for x in redditors)
        with codecs.open(filename, 'w', encoding='utf-8') as outfile:
            outfile.write('username, type, permalink, score\n')
            for _, redditor in sorted(mapping.items()):
                for submission in self.submitters.get(redditor, []):
                    outfile.write(u'{}, submission, {}, {}\n'
                                  .format(redditor, submission.permalink,
                                          submission.score))
                for comment in self.commenters.get(redditor, []):
                    outfile.write(u'{}, comment, {}, {}\n'
                                  .format(redditor, comment.permalink,
                                          comment.score))


def main():
    """Provide the entry point to the subreddit_stats command.

    :returns: 0 on success, 1 otherwise

    """
    parser = arg_parser(usage='usage: %prog [options] [SUBREDDIT]')
    parser.add_option('-s', '--submitters', type='int', default=5,
                      help='Number of top submitters to display '
                      '[default %default]')
    parser.add_option('-c', '--commenters', type='int', default=10,
                      help='Number of top commenters to display '
                      '[default %default]')
    parser.add_option('-a', '--after',
                      help='Submission ID to fetch after')
    parser.add_option('-d', '--days', type='int', default=32,
                      help=('Number of previous days to include submissions '
                            'from. Use 0 for unlimited. Default: %default'))
    parser.add_option('-D', '--debug', action='store_true',
                      help='Enable debugging mode. Does not post stats.')
    parser.add_option('-R', '--submission-reddit',
                      help=('Subreddit to submit to. If not present, '
                            'submits to the subreddit processed'))
    parser.add_option('-t', '--top',
                      help=('Run on top submissions either by day, week, '
                            'month, year, or all'))
    parser.add_option('', '--distinguished', action='store_true',
                      help=('Include distinguished subissions and '
                            'comments (default: False). Note that regular '
                            'comments of distinguished submissions will still '
                            'be included.'))
    parser.add_option('', '--no-self', action='store_true',
                      help=('Do not include self posts (and their comments) in'
                            ' the calculation.'))
    parser.add_option('', '--no-link', action='store_true',
                      help=('Only include self posts (and their comments) in '
                            'the calculation.'))
    parser.add_option('', '--prev',
                      help='Provide the submission id of previous SRS page.')
    parser.add_option('', '--include-prev', action='store_true',
                      help='Don\'t try to avoid overlap with a previous SRS.')
    parser.add_option('-o', '--output',
                      help='Save result csv to named file.')

    options, args = parser.parse_args()
    if len(args) != 1:
        sys.stdout.write('Enter subreddit name: ')
        sys.stdout.flush()
        subject_reddit = sys.stdin.readline().strip()
        if not subject_reddit:
            parser.error('No subreddit name entered')
    else:
        subject_reddit = args[0]

    check_for_updates(options)

    print('You chose to analyze this subreddit: {}'.format(subject_reddit))

    if options.no_link and options.no_self:
        parser.error('You are choosing to exclude self posts but also only '
                     'include self posts. Consider checking your arguments.')

    if options.submission_reddit:
        submission_reddit = options.submission_reddit
    else:
        submission_reddit = subject_reddit

    srs = SubRedditStats(subject_reddit, options.site, options.verbose,
                         options.distinguished)
    if options.prev:
        srs.prev_stat(options.prev)
    if options.top:
        found = srs.fetch_top_submissions(options.top, options.no_self,
                                          options.no_link)
    else:
        since_last = not options.include_prev
        found = srs.fetch_recent_submissions(max_duration=options.days,
                                             after=options.after,
                                             exclude_self=options.no_self,
                                             exclude_link=options.no_link,
                                             since_last=since_last)
    if not found:
        print('No submissions were found.')
        return 1
    srs.process_submitters()
    if options.commenters > 0:
        srs.process_commenters()
    if options.output:
        srs.save_csv(options.output)
    srs.publish_results(submission_reddit, options.submitters,
                        options.commenters, 5, 5, options.top, options.debug)
