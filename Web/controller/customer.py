from flask import Flask, request, jsonify, render_template, redirect
from http import HTTPStatus
import requests
import json

from config import Config
from models.customer import Customer

class CustomerController:
    def customer():
        rawdata = requests.get(Config.RESTAPI_URL+'/customer')
        data = rawdata.json()
        return render_template('customer.html', customers=data)

    def customerform():
        customer = Customer(0,'','','','','','','')
        data = json.dumps(customer.__dict__)
        return render_template('addcustomer.html', customer=data)

    def addcustomer():
        id = request.form.get("id")
        custname = request.form.get("custname")
        add1 = request.form.get("add1")
        add2 = request.form.get("add2")    
        city = request.form.get("city")    
        pincode = request.form.get("pincode")    
        phoneno = request.form.get("phoneno")    
        email = request.form.get("email")    

        if custname != '' and phoneno is not None:
            if id == '' or id is None:
                customer = Customer(0,custname,add1,add2,city,pincode,phoneno,email)
                data = json.dumps(customer.__dict__)
                data = json.loads(data)
                result = requests.post(Config.RESTAPI_URL+'/customer', json=data)
            else:
                customer = Customer(id,custname,add1,add2,city,pincode,phoneno,email)
                data = json.dumps(customer.__dict__)
                data = json.loads(data)
                result = requests.put(Config.RESTAPI_URL+f'/customer/{id}', json=data)

        return redirect('/customer')

    def editcustomer(id):
        rawdata = requests.get(Config.RESTAPI_URL+f'/customer/{id}')
        data = rawdata.json()
        return render_template('addcustomer.html', customer=data)

    def delcustomerconf():
        args = request.args
        id = args.get('id')
        custname = args.get('cname')
        return render_template('delcustomerconf.html', customer={'id':id, 'custname':custname})

    def delcustomer(id):
        result = requests.delete(Config.RESTAPI_URL+f'/customer/{id}')
        return redirect('/customer')
