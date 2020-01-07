from django import forms
from .models import bug


class AddBugForm(forms.ModelForm):
    """
    Creates a form to allow a user to
    add a bug report
    """
    class Meta:
        model = bug
        fields = ('title', 'details')