from flask import Flask, render_template, url_for
from flask.ext.sqlalchemy import SQLAlchemy

# The setup of the Flask framework as well as the SQL-Alchemy database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    # Creates an ID for the User that is unique
    id = db.Column(db.Integer, primary_key=True)
    # An attribute of the User (a column)
    username = db.Column(db.String(80), unique=True)
    # An attribute of the User (a column)
    email = db.Column(db.String(120), unique=True)

    # Creates the User for the database, a constructor if you will. 
    # Take a username and an email to make a User
    def __init__(self, username, email):
        self.username = username
        self.email = email

    # Print's human readable presentation of the User object
    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/")
# Loads the index page
def index():
    # Get all the users within the database
    users = User.query.all()
    # Render the index page as well as pass the users in the DB, and load the leaflet js and css files and the milo javascript file
    return render_template('index.html', 
        users=users,
        leafletjs = url_for('static', filename="leaflet.js"),
        leafletcss = url_for('static', filename="leaflet.css"),
        milojs = url_for('static', filename="milo.js"),
        milocss = url_for('static', filename="milo.css"))

# When you call >>> python milo.py this command is run and shows debugging in your terminal
if __name__ == "__main__":
    app.run(debug=True)