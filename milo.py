#!/usr/bin/env python

from flask import Flask, render_template,url_for
#from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://crappy-database.db'
#db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html",
      leafletjs = url_for('static', filename="leaflet.js"),
      leafletcss = url_for('static', filename="leaflet.css"),
      milojs = url_for('static', filename="milo.js"))

if __name__ == "__main__":
    app.run(debug=True)
