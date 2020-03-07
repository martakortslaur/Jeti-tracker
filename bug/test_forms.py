from django.test import TestCase
from bug.forms import AddBugForm, CommentForm


class TestAddBugForm(TestCase):
    def test_can_create_bug_with_missing_data(self):
        form = AddBugForm({'title': 'A New Bug', 'details': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['details'], [u'This field is required.'])

class TestCommentForm(TestCase):
    def test_can_create_bug_with_missing_data(self):
        form = CommentForm({'comment': ' '})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['comment'], [u'This field is required.'])

