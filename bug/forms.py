from django import forms
from .models import Bug, Comment


class AddBugForm(forms.ModelForm):

    class Meta:
        model = Bug
        fields = ['title', 'details']

class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(
        attrs={'rows': '3', 'cols': '4'}))

    class Meta:
        model = Comment
        fields = ['comment',]