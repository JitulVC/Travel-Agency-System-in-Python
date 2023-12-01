from flask import Flask, request, jsonify, render_template, redirect
from http import HTTPStatus
import requests
import json

from config import Config
from models.country import Country

class CountryController:
    def country():
        rawdata = requests.get(Config.RESTAPI_URL+'/country')
        data = rawdata.json()
        return render_template('country.html', countries=data)
