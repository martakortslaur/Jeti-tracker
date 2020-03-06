[![Build Status](https://travis-ci.com/martakortslaur/Jeti-tracker.svg?branch=master)](https://travis-ci.com/martakortslaur/Jeti-tracker)

# Jeti-tracker
For my last milestone project I chose to create an app that allows the user to be part of the creation process and 
add the bugs that they see in the app and comment on them. Also for the ecommerce part I chose the feature vote/upvote order that
allows the user to both add and upvote features that they wpould like to see in the app. Each upvote costs €10. The feature that gets
the most upvotes will be developed.  
I named it Jeti-tracker as to emphasize the exciting and adventurous character of this website. I pay a lot of attention to
the feeling the website would create for the user by choosing the cold mountain background picture what is the habitat of Jetis animals. 

## UX

#### User Stories
* As a user, I would like to be able to create an account, so that I can create a user profile.
* As a user, I would like to be able to create an account, so that I can add a bug.
* As a user, I would like to be able to create an account, so that I can comment on bugs and features.
* As a user, I would like to be able to create an account, so that I can view  features.
* As a user, I would like to be able to create an account, so that I can see what features have been requested by others.
* As a user, I would like to be able to create an account, so that I can request a features.
* As a user, I would like to be able to create an account, so that I can vote for features that I would like to see being dealt with.

## Features

#### Existing Features

##### Navbar
An unauthorised user will see the following links:
* Jeti-tracker (Navbar brand that links to the Homepage)
* Login
* Register
* All bugs


A logged in user will see the following links:
* Jeti-tracker
* Profile
* All Bugs
* All Features
* Cart
* Checkout
* Logout

* User Registration
To create an account a user must enter an email address, username and password. This functionality was implemented using Django's authentication system.
Once they have created an account the user is redirected to the login page. 

* Login
A registered user can login using their username and password. Once a user has successfully logged in, they will be redirected to their profile page.

* Logout
A user can log out at any time by clicking on the Logout link on the right-hand side of the navbar. Once logged out the user
will be redirected to the Homepage.

* User Profile
A logged in user will be able to visit their profile page by clicking on the relevant link in the navbar.
A user's profile page displays their email address.

* Reset Password
A user who has forgotten their password can request to have it reset by clicking on the 'forgot password' link below the log in form.
They will be then redirected to a form where they should enter the email address that was used when creating their account.
An email will be sent to that email address with instructions on how to create a new password. 

* View Bugs
If a user clicks on the 'All Bugs' link in the navbar they will be taken to a page containing a list of all the bugs that have been found.
There are two types of bugs, doing and done.

* Add a Bug
Clicking on the 'Add a Bug' link in the navbar allows a user to add a new bug.

* View a bug description

* Comment on a Bug/ Feature
All logged in users can post comments on a bug report or feature request.

* Delete comment on a Bug

* Toggle a bug
All logged in users can click the toggle button when it is done, or again toggle it back to doing.

* Features
A user can view a list of features that other users have requested. The colour-coded badges (ToDo, Doing and Done) that appear
beside the feature title provide the user with visual cues as to what stage of development the feature is at.
The thumbs-up icon to the right of the feature title tells a user how many votes that feature has received.

* Add a Feature
A user can submit a feature request by clicking on the 'Add Feature' button on the top of the list of features.
When this button is clicked the user is taken to a form where they fill in details of the feature that
they would like to see added to the site. The request is then added to the bottom of the list on the Features page. It is free to request a feature.

* View Feature Details
In development.

* Vote for a Feature
The user can 

* Delete Feature from the cart
The user can delete the voted features from the cart.

* View Cart
The user can see the voted features with the name and description of the feature. They can remove them from the cart if they don't want to upvote
these features.

* Checkout
 The user has the option to use given card numbers and do a so  called mock purchase to vote for the favourite feature.

#### Features I want to develop

* The delete function to bugs and features if the user was their author.

* Profile with showing the personally added bugs and features.


## Technologies Used
* HTML
* CSS
* Bootstrap
* Font Awesome
* Humanize
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
    python3 manage.py makemigrations
    python3 manage.py migrate
* Created a Procile at the top level of my project to tell Heroku what kind of app was being deployed
* Added the Heroku app to ALLOWED_HOSTS in settings.py file


#### Local Deployment
To deploy this could locally you should:
* Clone the [GitHub repository](https://github.com/martakortslaur/Jeti-tracker)
* Install Python on your computer
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
    python3 manage.py makemigrations
    python3 manage.py migrate
* To run your new django project use the following command:
    python3 manage.py runserver
* For saving the staticfiles and also CSS changes there was written the python3 manage.py collectstatic command to git commandline
to save the changes to AWS.
* To reset the data I used the Heroku reset data feature and run migrations again.

## Testing

* Developer tool for correcting the errors that have appeared. Using also print statement in the code to see the desired
messages print on the terminal.

* All HTML and CSS code used on the site has been tested using The W3 CSS Validation Service and The W3 Markup Validation Service.
The W3C shows that we conform to the standards of HTML and CSS.

* Site was viewed and tested in Google Chrome, Mozilla Firefox and Internet Explorer.

#### Acknowledgements

I received inspiration for this project from [here] (https://unicorn-attractor-milestone-4.herokuapp.com/), especially the
idea for this project. Some less time consuming yet the websites purpose-fulfilling solutions I received visiting this [website]
(https://unicorn-bug-tracker.herokuapp.com/) and this [website] (https://unicorn-attractor-project.herokuapp.com/). Picture 
for the background I got [here] (https://pixabay.com/photos/snowy-mountains-cloudy-snow-1149692/).
Specially the contrasting sections and the invitation sentence to ask people to write about their projects to me.
Also, I wanted to have some features similar to the portfolio of Haley Schafer. For example the navbar and rounded icons.
I am grateful for the help I received from the tutor support especially Xavier's stand up sessions, screenshares with Anna and good
 advice I received from my mentor Moosa Hassan.
