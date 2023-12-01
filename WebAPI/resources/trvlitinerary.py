from flask import request, jsonify
from flask_restful import Resource
from http import HTTPStatus

from models.trvlitinerary import TrvlItinerary, TrvlItinerarySchema
from extensions import db

class TrvlItineraryListResource(Resource):
    def get(self):
        trvlitinerarys = TrvlItinerary.query.all()
        trvlitinerarySchema = TrvlItinerarySchema(many=True)
        data = trvlitinerarySchema.dump(trvlitinerarys)
        return jsonify(data)

    def post(self):
        data = request.get_json()

        walkin = data.get('walkin')
        custid = data.get('custid')
        paxname = data.get('paxname')
        trvlmodeid = data.get('trvlmodeid')
        travelcompany = data.get('travelcompany')
        fromdest = data.get('fromdest')
        todest = data.get('todest')
        fromdate = data.get('fromdate')
        todate = data.get('todate')
        noofpax = data.get('noofpax')
        identitydoc = data.get('identitydoc')
        bookingrefno = data.get('bookingrefno')

        trvlitinerary = TrvlItinerary()
        trvlitinerary.walkin = walkin
        trvlitinerary.custid = custid
        trvlitinerary.paxname = paxname
        trvlitinerary.trvlmodeid = trvlmodeid
        trvlitinerary.travelcompany = travelcompany
        trvlitinerary.fromdest = fromdest
        trvlitinerary.todest = todest
        trvlitinerary.fromdate = fromdate
        trvlitinerary.todate = todate
        trvlitinerary.noofpax = noofpax
        trvlitinerary.identitydoc = identitydoc
        trvlitinerary.bookingrefno = bookingrefno

        db.session.add(trvlitinerary)
        db.session.commit()
        return f'{paxname} added', HTTPStatus.CREATED

class TrvlItineraryResource(Resource):
    def get(self,id):
        trvlitinerary = TrvlItinerary.query.filter_by(id=id).first()
        if not trvlitinerary:
            return jsonify({'message': 'Item not found'})
    
        trvlitinerarySchema = TrvlItinerarySchema(many=False)
        data = trvlitinerarySchema.dump(trvlitinerary)
        return jsonify(data)
    
    def put(self,id):
        data = request.get_json()

        trvlitinerary = TrvlItinerary.query.get(id)
        if not trvlitinerary:
            return jsonify({'message': 'Item not found'})

        walkin = data.get('walkin')
        custid = data.get('custid')
        paxname = data.get('paxname')
        trvlmodeid = data.get('trvlmodeid')
        travelcompany = data.get('travelcompany')
        fromdest = data.get('fromdest')
        todest = data.get('todest')
        fromdate = data.get('fromdate')
        todate = data.get('todate')
        noofpax = data.get('noofpax')
        identitydoc = data.get('identitydoc')
        bookingrefno = data.get('bookingrefno')

        trvlitinerary.walkin = walkin
        trvlitinerary.custid = custid
        trvlitinerary.paxname = paxname
        trvlitinerary.trvlmodeid = trvlmodeid
        trvlitinerary.travelcompany = travelcompany
        trvlitinerary.fromdest = fromdest
        trvlitinerary.todest = todest
        trvlitinerary.fromdate = fromdate
        trvlitinerary.todate = todate
        trvlitinerary.noofpax = noofpax
        trvlitinerary.identitydoc = identitydoc
        trvlitinerary.bookingrefno = bookingrefno
        db.session.commit()
        return f'{paxname} updated'

    def delete(self,id):
        trvlitinerary = TrvlItinerary.query.get(id)
        if not trvlitinerary:
            return jsonify({'message': 'Item not found'})
            
        db.session.delete(trvlitinerary)
        db.session.commit()
        return f'Record ID: {id} deleted'
