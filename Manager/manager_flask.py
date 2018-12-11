'''
Created on Dec 10, 2018

@author: Gabriel Torrandella
'''
from flask import Flask, json
from wtforms import Form
from flask.globals import request
from flask.wrappers import Response
from werkzeug.wrappers import ETagRequestMixin, ETagResponseMixin, BaseRequest, BaseResponse
from Campaign import Campaign
import manager

app = Flask(__name__)

class Response(BaseResponse, ETagResponseMixin):
    pass

class Resquest(BaseRequest, ETagRequestMixin):
    pass

def checkForm(form):
    return True

@app.route('/Campaing', methods = ['POST', 'DELETE'])
def api_manager():
    
    if request.method == 'POST':
        if checkForm(request.form):
            idCampaing = manager.insertCampaign(request.form)
            res = Response(status_code = 201)
            res.set_etag(idCampaing, weak = False)    
            return res
        else:
            return Response(status_code = 412)
        
    elif request.method == 'DELETE':
        manager.deleteCampaignporid(request.get_etag())
        return Response(status_code = 200)
        
    else: 
        return Response(status_code = 400)

@app.route('/Campaing/<int:idC>', methods = ['GET', 'PATCH'])
def api_manager_id():
    
    if request.method == 'GET':
        pass
    
    elif request.method == 'PATCH':
        pass
    
    else:
        return Response(status_code = 404)
    
    pass

if __name__ == "__main__":
    app.run()