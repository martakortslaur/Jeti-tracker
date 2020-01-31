[![Build Status](https://travis-ci.com/martakortslaur/Jeti-tracker.svg?branch=master)](https://travis-ci.com/martakortslaur/Jeti-tracker)

# Jeti-tracker
For my last milestone project I chose to create an app that allows the user to be part of the creation process and 
add the bugs that they see in the app and comment on them. Also for the ecommerce part I chose the feature upvote order that
allows the user to both request and upvote features that they wpould like to see in the app. Each upvote costs €10. The feature that gets
the most upvotes will be developed.    

## UX

#### User Stories
* As a user, I would like to be able to create an account, so that I can create a user profile.
* As a user, I would like to be able to create an account, so that I can add a bug.
* As a user, I would like to be able to create an account, so that I can comment on bugs and features.
* As a user, I would like to be able to create an account, so that I can view available features.
* As a user, I would like to be able to create an account, so that I can see what features have been requested by others.
* As a user, I would like to be able to create an account, so that I can request features.
* As a user, I would like to be able to create an account, so that I can vote for features that I would like to see being developed.

## Features

#### Existing Features

##### Navbar
An unauthorised user will see the following links:
* Jeti-tracker (Navbar brand that links to the Homepage)
* Register
* Login

A logged in user will see the following links:
* Jeti-tracker
* Profile
* All Bugs
* Add Bugs
* All Features
* Add Feature
* Shopping Cart
* Logout

* User Registration
To create an account a user must enter an email address, username and password. This functionality was implemented using Django's authentication system. Once they have created an account the user is redirected to the login page. 

* Login
A registered user can login using their username and password. Once a user has successfully logged in, they will be redirected to their profile page.

* Logout
A user can log out at any time by clicking on the Logout link on the right-hand side of the navbar. Once logged out the user will be redirected to the Homepage.

* User Profile
A logged in user will be able to visit their profile page by clicking on the relevant link in the navbar. A user's profile page displays their email address.

* Reset Password
A user who has forgotten their password can request to have it reset by clicking on the 'forgot password' link below the log in form. They will be then redirected to a form where they should enter the email address that was used when creating their account. An email will be sent to that email address with instructions on how to create a new password. 

* View Bugs
If a user clicks on the 'All Bugs' link in the navbar they will be taken to a page containing a list of all the bugs that have been found. There are two types of bugs, doing and done.

* Add a Bug
Clicking on the 'Add a Bug' link in the navbar allows a user to add a new bug.

* View a bug description


* Comment on a Bug/ Feature
All logged in users can post comments on a bug report or feature request. 

* Features
A user can view a list of features that other users have requested. The colour-coded badges (ToDo, Doing and Done) that appear beside the feature title provide the user with visual cues as to what stage of development the feature is at. The thumbs-up icon to the right of the feature title tells a user how many votes that feature has received.

* Request a Feature
A user can submit a feature request by clicking on the 'Request Feature' button on the top right of the list of features. When this button is clicked the user is taken to a form where they fill in details of the feature that they would like to see added to the site. The request is then added to the top of the list on the Features page. It is free to request a feature.

* View Feature Details
In development.

* Vote for a Feature
In development.

* Delete Feature
In development.

* View Cart
In development.

* Checkout
 In development.

## Technologies Used
* HTML
* CSS
* Bootstrap
* Font Awesome
* JavaScript/ jQuery
* Django
* Python
* Stripe
* Whitenoise
* Postgres/ Sqlite3

## Deployment
Version control was carried out entirely using git. The GitHub repository can be found [here](https://github.com/martakortslaur/Jeti-tracker)

The project was hosted on Heroku. The running application is available [here](https://jeti-tracker.herokuapp.com/)

#### To deploy to Heroku I took the following steps:
* Created a requirements.txt file to hold a list of the dependencies needed to run the project
* Created an env.py file, and added it to .gitignore, to store any environment variables that I didn't want pushed to GitHub
* Created a new GitHub repository
* Created a Heroku app with a unique name
* Connected my GitHub repository to my Heroku app and enabled automatic deploys
* Under the Deploy tab I scrolled down to add-ons and connected to the Postgres database
* Under the settings tab, I clicked on Reveal Config Vars and stored the relevant environment variables as cofig variables
* Ensured all existing migrations were pushed to the new Postgres database by running:
    python manage.py makemigrations
    python manage.py migrate
* Created a Procile at the top level of my project to tell Heroku what kind of app was being deployed
* Added the Heroku app to ALLOWED_HOSTS in settings.py file


#### Local Deployment
To deploy this could locally you should:
* Clone the [GitHub repository](https://github.com/LibbyH52/Unicorn-Attractor.git)
* Install Python on your machine (if it isn't already there)
* Create a folder to store the project
* Install a virtual environment
* Create a new virtual environment and activate it
* Install Django inside your new virtual environment
* Create a new Django project
    django-admin startproject projectname
* Install the dependencies listed in requirements.txt
    pip install -r requirements.txt
* Add each app to the list of INSTALLED_APPS in settings.py
* Run make migrations to create the database
    python manage.py makemigrations
    python manage.py migrate
* To run your new django project use the following command:
    python manage.py runserver


## Testing

* Views, models and forms were validated using the PEP8 checker. 


#### Acknowledgements
I am grateful for the help I received from the tutor support, Xavier's stand up sessions and my mentor Moosa Hassan.
