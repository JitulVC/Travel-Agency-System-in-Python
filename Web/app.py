from flask import Flask, request, jsonify, render_template, redirect
from http import HTTPStatus

from config import Config

from controller.trvlitinerary import TrvlItineraryController
from controller.customer import CustomerController
from controller.country import CountryController

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    return app
 
app = create_app()
 

@app.route('/index', methods=['GET'])
def home():
    return render_template('index.html')

# BOOKING
@app.route('/trvlitinerary', methods=['GET'])
def trvlitinerary():
    return TrvlItineraryController.trvlitinerary()
             
@app.route('/trvlitineraryform', methods=['GET'])
def trvlitineraryform():
    return TrvlItineraryController.trvlitineraryform()

@app.route('/addtrvlitinerary', methods=['POST'])
def addtrvlitinerary():
    return TrvlItineraryController.addtrvlitinerary()

@app.route('/edititinerary/<int:id>', methods=['GET'])
def edititinerary(id):
    return TrvlItineraryController.edititinerary(id)

@app.route('/delitineraryconf', methods=['GET'])
def delitineraryconf():
    return TrvlItineraryController.delitineraryconf()

@app.route('/delitinerary/<int:id>', methods=['GET'])
def delitinerary(id):
    return TrvlItineraryController.delitinerary(id)

# CUSTOMER
@app.route('/customer', methods=['GET'])
def customer():
    return CustomerController.customer()

@app.route('/customerform', methods=['GET'])
def customerform():
    return CustomerController.customerform()

@app.route('/addcustomer', methods=['POST'])
def addcustomer():
    return CustomerController.addcustomer()

@app.route('/editcustomer/<int:id>', methods=['GET'])
def editcustomer(id):
    return CustomerController.editcustomer(id)

@app.route('/delcustomerconf', methods=['GET'])
def delcustomerconf():
    return CustomerController.delcustomerconf()

@app.route('/delcustomer/<int:id>', methods=['GET'])
def delcustomer(id):
    return CustomerController.delcustomer(id)

# COUNTRY
@app.route('/country', methods=['GET'])
def country():
    return CountryController.country()
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)

