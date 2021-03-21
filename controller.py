from flask import Flask ,render_template, request, redirect
from flask.globals import session
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, desc
from model import *

@app.route('/')
def index():
        return render_template('index.html',runner_querys=runner.query.all())

@app.route('/', methods=['POST'])
def no1():
    if request.method == "POST":
        fname = request.form["fname"]
        lname = request.form["lname"]
        age = request.form["age"]
        get_data(fname ,lname ,age)
        return render_template('index.html',runner_querys=runner.query.all())

@app.route('/kilo', methods=['POST'])
def kilo():
    if request.method == "POST":
        id = request.form["id"]
        km = request.form["km"]
        if (float(km)>10):
            return render_template('index.html',runner_querys=runner.query.all())
        else:
            update_km(id,km)
            return render_template('index.html',runner_querys=runner.query.all())

@app.route('/top', methods=['POST'])
def top():
    if request.method == "POST":
        return render_template('1.html',runner_querys = db.session.query(runner.ID, runner.Firstname, runner.Lastname, runner.Age, runner.Km, runner.Trophy).order_by(desc(runner.Km)))
