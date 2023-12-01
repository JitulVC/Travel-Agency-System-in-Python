from flask import request, jsonify
from flask_restful import Resource
from http import HTTPStatus

from models.trvlmode import TrvlMode, TrvlModeSchema
from extensions import db

class TrvlModeListResource(Resource):
    def get(self):
        trvlmodes = TrvlMode.query.all()
        trvlmodeSchema = TrvlModeSchema(many=True)
        data = trvlmodeSchema.dump(trvlmodes)
        return jsonify(data)

    def post(self):
        data = request.get_json()

        trvl_mode = data.get('trvlmode')
        trvlmode = TrvlMode(trvlmode=trvl_mode)
        db.session.add(trvlmode)
        db.session.commit()
        return f'{trvl_mode} added', HTTPStatus.CREATED

class TrvlModeResource(Resource):
    def get(self,id):
        trvlmode = TrvlMode.query.filter_by(id=id).first()
        if not trvlmode:
            return jsonify({'message': 'Item not found'})
    
        trvlmodeSchema = TrvlModeSchema(many=False)
        data = trvlmodeSchema.dump(trvlmode)
        return jsonify(data)
    
    def put(self,id):
        data = request.get_json()

        trvlmode = TrvlMode.query.get(id)
        if not trvlmode:
            return jsonify({'message': 'Item not found'})

        trvl_mode = data.get('trvlmode')
        trvlmode.trvlmode=trvl_mode
        db.session.commit()
        return f'{trvl_mode} updated'

    def delete(self,id):
        trvlmode = TrvlMode.query.get(id)
        if not trvlmode:
            return jsonify({'message': 'Item not found'})
            
        db.session.delete(trvlmode)
        db.session.commit()
        return f'Record ID: {id} deleted'
