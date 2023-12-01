from flask import Flask
from flask_restful import Api 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

from config import Config
from extensions import db, ma
from models.trvlmode import TrvlMode
from resources.trvlmode import TrvlModeListResource, TrvlModeResource
from models.customer import Customer
from resources.customer import CustomerListResource, CustomerResource
from models.trvlitinerary import TrvlItinerary
from resources.trvlitinerary import TrvlItineraryListResource, TrvlItineraryResource
from models.country import Country
from resources.country import CountryListResource

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    register_extensions(app)
    register_resources(app)

    return app


def register_extensions(app):
    db.init_app(app)
    ma.init_app(app)

def register_resources(app):
    api = Api(app)
    api.add_resource(TrvlModeListResource, '/trvlmode')
    api.add_resource(TrvlModeResource, '/trvlmode/<int:id>')
    api.add_resource(CustomerListResource, '/customer')
    api.add_resource(CustomerResource, '/customer/<int:id>')
    api.add_resource(TrvlItineraryListResource, '/trvlitinerary')
    api.add_resource(TrvlItineraryResource, '/trvlitinerary/<int:id>')
    api.add_resource(CountryListResource, '/country')

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=4500)
