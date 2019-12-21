from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):
    """Form to be used to log users in"""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    """Form used to register a new user"""

    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

#     next thing that we need to do is create an inner
# class an inner class is a class that we can use that will provide just some
# information about this form these are called meta classes and Django
# usually uses them internally to determine things about the class but
# we can also use it to specify the model that we want store information in and we
# want we want to use it to specify the fields that we're going to expose which
# our email, username, password1 and password2