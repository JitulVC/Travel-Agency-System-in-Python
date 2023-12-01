from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from extensions import db,ma

class TrvlMode(db.Model):
    __tablename__ = 'trvlmode'

    id = db.Column(db.Integer, primary_key=True)
    trvlmode = db.Column(db.String(30), unique=False, nullable=False)

class TrvlModeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TrvlMode
        load_instance = True
        ordered = True
