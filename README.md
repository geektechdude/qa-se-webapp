# qa-se-webapp
Software Engineering &amp; Agile Assignment - Web Application Development. Application written in Python. Any information stored in database is dummy information.

# Introduction
As part of the Software Engineering & Agile module of my degree I am required to design, develop and test a web database application written in Python. The Python Web Framework can be any (Django, FastAPI, Flask), however I am using Flask.

# Requirements
The web app has restrictions / requirements as per the brief, these are:
- It must feature a relational database (e.g. SQL) backend.
- The database can have a minimum of 2 tables and a maximum of 4 tables.
- The web application should have 2 types of users: regular and admin.
- Regular users should be able to carry out CREATE, READ and UPDATE actions on the database via the web app.
- Admin users should be able to carry out CREATE, READ, UPDATE and DELETE actions on the database via the web app.

Running In DEV Mode - NOTE: Commands are case-sensitive:
- Clone the repository
- Open the repository (change to the repository directory)
- Create a Virtual Environment using the command "python3 -m venv ./venv"
- Activate the Virtual Environment using the command "source ./venv/bin/activate"
- Install the required Python modules using the command "pip install -r requirements.txt"
- Set the FLASK_APP environment variable using the command "export FLASK_APP=flaskwebapp.__init__.py"
- Initialise database using command "flask init-db"
- Run the Flask app using the command "flask run"
