from flask import request, jsonify
from flask_restful import Resource
from http import HTTPStatus

from models.customer import Customer, CustomerSchema
from extensions import db

class CustomerListResource(Resource):
    def get(self):
        customers = Customer.query.all()
        customerSchema = CustomerSchema(many=True)
        data = customerSchema.dump(customers)
        return jsonify(data)

    def post(self):
        data = request.get_json()

        custname = data.get('custname')
        add1 = data.get('add1')
        add2 = data.get('add2')
        city = data.get('city')
        pincode = data.get('pincode')
        phoneno = data.get('phoneno')
        email = data.get('email')
        customer = Customer()
        customer.custname = custname
        customer.add1 = add1
        customer.add2 = add2
        customer.city = city
        customer.pincode = pincode
        customer.phoneno = phoneno
        customer.email = email
        db.session.add(customer)
        db.session.commit()
        return f'{custname} added', HTTPStatus.CREATED

class CustomerResource(Resource):
    def get(self,id):
        customer = Customer.query.filter_by(id=id).first()
        if not customer:
            return jsonify({'message': 'Item not found'})
    
        customerSchema = CustomerSchema(many=False)
        data = customerSchema.dump(customer)
        return jsonify(data)
    
    def put(self,id):
        data = request.get_json()

        customer = Customer.query.get(id)
        if not customer:
            return jsonify({'message': 'Item not found'})

        custname = data.get('custname')
        add1 = data.get('add1')
        add2 = data.get('add2')
        city = data.get('city')
        pincode = data.get('pincode')
        phoneno = data.get('phoneno')
        email = data.get('email')

        customer.custname = custname
        customer.add1 = add1
        customer.add2 = add2
        customer.city = city
        customer.pincode = pincode
        customer.phoneno = phoneno
        customer.email = email
        db.session.commit()
        return f'{custname} updated'

    def delete(self,id):
        customer = Customer.query.get(id)
        if not customer:
            return jsonify({'message': 'Item not found'})
            
        db.session.delete(customer)
        db.session.commit()
        return f'Record ID: {id} deleted'
