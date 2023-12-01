from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from extensions import db,ma

class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True)
    custname = db.Column(db.String(45), unique=False, nullable=False)
    add1 = db.Column(db.String(45), unique=False, nullable=True)
    add2 = db.Column(db.String(45), unique=False, nullable=True)
    city = db.Column(db.String(45), unique=False, nullable=True)
    pincode = db.Column(db.String(7), unique=False, nullable=True)
    phoneno = db.Column(db.String(20), unique=False, nullable=True)
    email = db.Column(db.String(45), unique=False, nullable=True)
    createdon = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updatedon = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer
        load_instance = True
        ordered = True
