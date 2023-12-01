from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from extensions import db,ma

class TrvlItinerary(db.Model):
    __tablename__ = 'trvlitinerary'

    id = db.Column(db.Integer, primary_key=True)
    walkin = db.Column(db.Integer, unique=False, nullable=False)
    custid = db.Column(db.Integer, unique=False, nullable=True)
    paxname = db.Column(db.String(45), unique=False, nullable=False)
    trvlmodeid = db.Column(db.Integer, unique=False, nullable=True)
    travelcompany = db.Column(db.String(45), unique=False, nullable=True)
    fromdest = db.Column(db.String(45), unique=False, nullable=True)
    todest = db.Column(db.String(45), unique=False, nullable=True)
    fromdate = db.Column(db.DateTime(), unique=False, nullable=True)
    todate = db.Column(db.DateTime(), unique=False, nullable=True)
    noofpax = db.Column(db.Integer, unique=False, nullable=True)
    identitydoc = db.Column(db.String(45), unique=False, nullable=True)
    bookingrefno = db.Column(db.String(45), unique=False, nullable=True)
    createdon = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updatedon = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

class TrvlItinerarySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TrvlItinerary
        load_instance = True
        ordered = True
