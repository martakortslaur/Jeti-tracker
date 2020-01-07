from django.test import TestCase, Client
from django.utils import timezone
from .models import bug, Comment


class BugModelTest(TestCase):
    def test_str(self):
        bug = bug(title='Yet another one')
        self.assertEqual(str(bug), bug.title)


class CommentModelTest(TestCase):
    def test_str(self):
        comment = Comment(comment='I am having the same problem')
        self.assertEqual(str(comment), comment.comment)