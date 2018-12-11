'''
Created on Dec 10, 2018

@author: Gabriel Torrandella
'''
from flask import Flask, json
from wtforms import Form
from flask.globals import request
from flask.wrappers import Response
from Campaign import Campaign
import manager

app = Flask(__name__)

def checkForm(form):
    return True

@app.route('/Campaing', methods = ['POST', 'DELETE'])
def api_manager():
    
    if request.method == 'POST':
        if checkForm(request.form):
            idCampaing = manager.insertCampaign(request.form)
            res = Response(status_code = 201)
            res.set_etag(idCampaing)    
            return res
        else:
            return Response(status_code = 412)
        
    if request.method == 'DELETE':
        return Response(status_code = 200)
        
    else: 
        return Response(status_code = 400)

if __name__ == "__main__":
    app.run()