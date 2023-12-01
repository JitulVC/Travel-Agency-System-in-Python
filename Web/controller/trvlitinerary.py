from flask import Flask, request, jsonify, render_template, redirect
from http import HTTPStatus
import requests
import json

from config import Config
from models.trvlmode import TrvlMode
from models.customer import Customer
from models.trvlitinerary import TrvlItinerary

class TrvlItineraryController:
    def trvlitinerary():
        rawdata = requests.get(Config.RESTAPI_URL+'/trvlitinerary')
        data = rawdata.json()
        return render_template('trvlitinerary.html', trvlitineraries=data)

    def trvlitineraryform():
        trvlitinerary = TrvlItinerary(0,0,0,'',0,'','','','','',0,'','')
        data = json.dumps(trvlitinerary.__dict__)
        
        rawdata = requests.get(Config.RESTAPI_URL+'/trvlmode')
        trvlmodes = rawdata.json()

        rawdata = requests.get(Config.RESTAPI_URL+'/customer')
        customers = rawdata.json()

        return render_template('additinerary.html', trvlitinerary=data,trvlmodes=trvlmodes, customers=customers)

    def addtrvlitinerary():
        id = request.form.get("id")
        walkin = request.form.get("iswalkin")
        custid = request.form.get("customer")
        paxname = request.form.get("paxname")    
        trvlmodeid = request.form.get("trvlmode")    
        travelcompany = request.form.get("travelcompany")    
        fromdest = request.form.get("fromdest")    
        todest = request.form.get("todest")    
        fromdate = request.form.get("fromdate")    
        todate = request.form.get("todate")    
        noofpax = request.form.get("noofpax")    
        bookingrefno = request.form.get("bookingrefno")    
        identitydoc = request.form.get("identitydoc")

        if paxname != '' and bookingrefno is not None:
            if id == '' or id is None:
                trvlitinerary = TrvlItinerary(0,walkin,custid,paxname,trvlmodeid,travelcompany,fromdest,todest,fromdate,todate,noofpax,identitydoc,bookingrefno)
                data = json.dumps(trvlitinerary.__dict__)
                data = json.loads(data)
                result = requests.post(Config.RESTAPI_URL+'/trvlitinerary', json=data)
            else:
                trvlitinerary = TrvlItinerary(id,walkin,custid,paxname,trvlmodeid,travelcompany,fromdest,todest,fromdate,todate,noofpax,identitydoc,bookingrefno)
                data = json.dumps(trvlitinerary.__dict__)
                data = json.loads(data)
                result = requests.put(Config.RESTAPI_URL+f'/trvlitinerary/{id}', json=data)

        return redirect('/trvlitinerary')

    def edititinerary(id):
        rawdata = requests.get(Config.RESTAPI_URL+f'/trvlitinerary/{id}')
        data = rawdata.json()
        
        rawdata = requests.get(Config.RESTAPI_URL+'/trvlmode')
        trvlmodes = rawdata.json()

        rawdata = requests.get(Config.RESTAPI_URL+'/customer')
        customers = rawdata.json()

        return render_template('additinerary.html', trvlitinerary=data, trvlmodes=trvlmodes, customers=customers)

    def delitineraryconf():
        args = request.args
        id = args.get('id')
        bookingrefno = args.get('bookingrefno')
        paxname = args.get('paxname')
        return render_template('delitineraryconf.html', trvlitinerary={'id':id, 'bookingrefno':bookingrefno, 'paxname':paxname})

    def delitinerary(id):
        result = requests.delete(Config.RESTAPI_URL+f'/trvlitinerary/{id}')
        return redirect('/trvlitinerary')
