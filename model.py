from enum import unique
from flask import Flask
from flask.globals import session
from sqlalchemy.orm import relation, relationship, backref
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.sql import select, insert
import random, string

from sqlalchemy.sql.sqltypes import REAL
from main import *
'''
votes = [""]
subject_list = [0,5506003,5506004,5506006,5506009,5506209]
def get_votes(vote):
    votes.append(vote)
'''

def rand_string():
    letters = string.ascii_uppercase
    return ( ''.join(random.choice(letters) for i in range(3)) )

def rand_num():
    number = random.randint(100,999)
    return str(number)


class runner(db.Model):
    RID = db.Column(db.Integer, primary_key=True)
    ID = db.Column(db.String(20), nullable=True)
    Firstname = db.Column(db.String(20), nullable=False)
    Lastname = db.Column(db.String(20), nullable=False)
    Age = db.Column(db.Integer, nullable=True)
    Km = db.Column(db.Float, nullable=True)
    Trophy = db.Column(db.String(20), nullable=False)

def get_data(fname,lname,age):
    string = rand_string()
    number = rand_num()
    temp = (string+""+number)
    insert = runner(ID = temp, Firstname = fname, Lastname = lname, Age = age, Km = 0 , Trophy = "Not yet")
    db.session.add(insert)
    db.session.commit()

def update_km(id, km):
    q = db.session.query(runner)
    q = q.filter(runner.ID == id)
    rec = q.one()
    rec.Km = float(rec.Km)+float(km)
    if (float(rec.Km)>42.195):
        rec.Trophy = "Can get trophy"
    
    db.session.commit()
    

'''
db.session.query(Score).delete()
db.session.commit()


db.session.execute(insert(Score).from_select([Score.Stu_ID, Score.Sub_ID],select([Student.STID, Subject.SJID])))
db.session.commit()

qr = db.session.query(Score)
for x in range(1,26):
    q = qr.filter(Score.ID == x)
    rec = q.one()
    rec.Sc = random.randrange(1,100)
    db.session.commit()
'''