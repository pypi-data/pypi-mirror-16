from praw.models import Comment
import mock

from ... import IntegrationTest


class TestComment(IntegrationTest):
    def test_attributes(self):
        with self.recorder.use_cassette(
                'TestComment.test_attributes'):
            comment = Comment(self.reddit, 'cklhv0f')
            assert comment.author == 'bboe'
            assert comment.body.startswith('Yes it does.')
            assert not comment.is_root
            assert comment.permalink(fast=True) == '/comments/2gmzqe//cklhv0f'
            assert comment.submission == '2gmzqe'

    def test_clear_vote(self):
        self.reddit.read_only = False
        with self.recorder.use_cassette(
                'TestComment.test_clear_vote'):
            Comment(self.reddit, 'd1680wu').clear_vote()

    @mock.patch('time.sleep', return_value=None)
    def test_delete(self, _):
        self.reddit.read_only = False
        with self.recorder.use_cassette(
                'TestComment.test_delete'):
            comment = Comment(self.reddit, 'd1616q2')
            comment.delete()
            assert comment.author is None
            assert comment.body == '[deleted]'

    def test_downvote(self):
        self.reddit.read_only = False
        with self.recorder.use_cassette(
                'TestComment.test_downvote'):
            Comment(self.reddit, 'd1680wu').downvote()

    @mock.patch('time.sleep', return_value=None)
    def test_edit(self, _):
        self.reddit.read_only = False
        with self.recorder.use_cassette(
                'TestComment.test_edit'):
            comment = Comment(self.reddit, 'd1616q2')
            comment.edit('New text')
            assert comment.body == 'New text'

    @mock.patch('time.sleep', return_value=None)
    def test_mark_read(self, _):
        self.reddit.read_only = False
        with self.recorder.use_cassette(
                'TestComment.test_mark_read'):
            comment = next(self.reddit.inbox.unread())
            assert isinstance(comment, Comment)
            comment.mark_read()

    @mock.patch('time.sleep', return_value=None)
    def test_mark_unread(self, _):
        self.reddit.read_only = False
        with self.recorder.use_cassette(
                'TestComment.test_mark_unread'):
            comment = next(self.reddit.inbox.comment_replies())
            comment.mark_unread()

    def test_permalink(self):
        with self.recorder.use_cassette(
                'TestComment.test_permalink'):
            comment = Comment(self.reddit, 'cklhv0f')
            assert comment.permalink() == ('/r/redditdev/comments/2gmzqe/'
                                           'praw_https_enabled_praw_testing_'
                                           'needed/cklhv0f')

    def test_reply(self):
        self.reddit.read_only = False
        with self.recorder.use_cassette(
                'TestComment.test_reply'):
            parent_comment = Comment(self.reddit, 'd1616q2')
            comment = parent_comment.reply('Comment reply')
            assert comment.author == self.reddit.config.username
            assert comment.body == 'Comment reply'
            assert not comment.is_root
            assert comment.parent_id == parent_comment.fullname

    def test_report(self):
        self.reddit.read_only = False
        with self.recorder.use_cassette(
                'TestComment.test_report'):
            Comment(self.reddit, 'd0335z3').report('custom')

    def test_save(self):
        self.reddit.read_only = False
        with self.recorder.use_cassette(
                'TestComment.test_save'):
            Comment(self.reddit, 'd1680wu').save('foo')

    def test_unsave(self):
        self.reddit.read_only = False
        with self.recorder.use_cassette(
                'TestComment.test_unsave'):
            Comment(self.reddit, 'd1680wu').unsave()

    def test_upvote(self):
        self.reddit.read_only = False
        with self.recorder.use_cassette(
                'TestComment.test_upvote'):
            Comment(self.reddit, 'd1680wu').upvote()
