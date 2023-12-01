from flask import request, jsonify
from flask_restful import Resource
from http import HTTPStatus

from models.country import Country, CountrySchema
from extensions import db

class CountryListResource(Resource):
    def get(self):
        countries = Country.query.all()
        countrySchema = CountrySchema(many=True)
        data = countrySchema.dump(countries)
        return jsonify(data)
