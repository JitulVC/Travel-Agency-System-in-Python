

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from extensions import db,ma

class Country(db.Model):
    __tablename__ = 'country'
    id = db.Column(db.Integer, primary_key=True)
    countryname = db.Column(db.String(80), unique=False, nullable=False)
    iso = db.Column(db.String(2), unique=False, nullable=False)
    def __repr__(self):
        return f"id : {self.id}, CountryName : {self.countryname}"

class CountrySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Country
        load_instance = True
        ordered = True
