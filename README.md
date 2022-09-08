# qa-se-webapp
Software Engineering &amp; Agile Assignment - Web Application Development. Application written in Python. Any information stored in database is dummy information.

# Introduction
As part of the Software Engineering & Agile module of my degree I am required to design, develop and test a web database application written in Python. The Python Web Framework can be any (Django, FastAPI, Flask), however I am using Flask.

# Requirements
The web app has restrictions / requirements as per the brief, these are:
- It must feature a relational database (e.g. SQL) backend.
The web app currently uses a different SQLlite backend for the production (live) version of the app and the development (test) version. 
SQLAlchemy handles the connectivity and the database settings can be set via environment variables or within the config.py file.
- The database can have a minimum of 2 tables and a maximum of 4 tables.
The database has 2 tables. One for Users and one for Assets. Both tables have a Primary Key set on their ID fields. 
A relationship exists between Assets.AssignedBy and Users.ID to record who has assigned / updated the Asset record.
- The web application should have 2 types of users: regular and admin.
The web application has regular users and admin users. 
The application looks for an environment variable or a variable within the config.py file for the admin user email address. 
Upon signing up with the appropriate email address the admin user gains admin privileages.
- Regular users should be able to carry out CREATE, READ and UPDATE actions on the database via the web app.
Regular users can create assets, read asset details and update asset details.
- Admin users should be able to carry out CREATE, READ, UPDATE and DELETE actions on the database via the web app.
The admin user can do everything a regular user can, and also has an option to delete an asset when on the "Edit Asset" screen.
- Admin users should be able to make changes to the underlaying database.
The underlaying database can be accessed from the device running the application using the following command from within the "flaskwebapp" directory:
flask shell
Database commands such as User.query.all() to list all users can be run. To exit the Flask Shell using the command:
exit()

# Modularisation
The web app has been split into modules to assist with maintaining it and to (hopefully) make it easier to understand.
The web app resides within the "flaskwebapp" directory. The README.md and requirements.txt, alongside non-essentials (.github, .vscode, .gitignore, venv), are outside this directory to keep the flaskwebapp directory free from clutter and files that are generated on first run.

Within the flaskwebapp directory is assets.py which is the application and a config.py file containing the configuration that the app requires. Configuration can also be set via environment variables if preferred.

The app directory contains templates for "auth" and "main". Each of these contain views.py which tell Flask what should be shown where (e.g. which URL endpoints are available, who they are available to, where they are available and what functions they carry out). forms.py tells Flask what should be on a form and what should be expected from the form, also carrying out entry validation. tables.py tells Flask what details should be on a table. errors.py is to enable custome error pages.

The static/css directory contains the CSS style sheet which can be used to overide CSS settings in the flask-bootstrap library.

The templates directory contains a base.html written in HTML with Jinja2 formatting that acts as a template for the other pages. The templates tell Flask how to display (or not display) information on web pages. The subdirectories are are named auth for authorisation pages (e.g. account registration, account login), errors for error pages and views for regular pages.

models.py contains the classes that are used to create and allow interaction with the database. Each table (e.g., Users, Assets) is it's own class.

The tests directory contains the Unit Test files (each starting with the name test_) that are used to test the web application.

# Naming Conventions
Functions, variables and routes within the web app have been named appropriatly. For example the /add and /delete routes of /asset/ do as they are named (add and delete). The AddAsset, SearchAsset, EditAsset classes from within forms.py also do as labelled (add, search and edit).

# Usability (Notifications)
The flash module of Flask is used to display notifications to the end user upon certain actions such as creating an account, logging out, adding an asset and editing an asset. A warning message is displayed to admin users upon trying to delete an asset asking them if they are sure they want to delete the asset.

# Running The Application
Running In DEV Mode - NOTE: Commands are case-sensitive:
- Clone the repository
- Open the repository (change to the repository directory)
- Create a Virtual Environment using the command "python3 -m venv ./venv"
- Activate the Virtual Environment using the command "source ./venv/bin/activate"
- Install the required Python modules using the command "pip install -r requirements.txt"
- Set the FLASK_APP environment variable using the command "export FLASK_APP=assets.py"
- Change to the flaskwebapp directory
- Initialise database using command "flask db init"
- Migrate any database changges using command "flask db migrate"
- Upgrade database using command "flask db upgrade"
- Run the Flask app using the command "flask run"
OR
- Run the unit tests using the command "flask test"
