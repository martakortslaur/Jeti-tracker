from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm

def index(request):
    return render(request, 'index.html')

def logout(request):
  
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))


@login_required
def logout(request):

    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))

def login(request):

    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":

        print("Entering POST")
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():

            print("Form is valid")
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            

            if user:
                print("user is valid")
                messages.success(request, "You have successfully logged in!")
                auth.login(user=user, request=request)
                print("about to redirect to index")
                return redirect(reverse('index'))

            else:
                print("user was not valid")
                login_form.add_error(None, "Your username or password is incorrect")

    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})

def user_profile(request):
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})

