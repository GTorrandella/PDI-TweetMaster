'''
Created on Dec 10, 2018

@author: Gabriel Torrandella
'''
from flask import Flask
from flask.globals import request
from flask.wrappers import Response
from werkzeug.wrappers import ETagRequestMixin, ETagResponseMixin, BaseRequest, BaseResponse
import manager
sys.path.append("../..")
from DatabaseConnector import configTables

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
            idCampaing = manager().insertCampaign(request.get_json())
            res = Response(status_code = 201)
            res.set_etag(idCampaing, weak = False)    
            return res
        else:
            return Response(status_code = 412)
        
    elif request.method == 'DELETE':
        if 'idC' in request.json:
            Manager.deleteCampaignporid(request.json['idC'])
        elif 'email' in request.json:
            Manager.deleteCampaignporuser(request.json['email'])
        return Response(status_code = 200)
        
    else: 
        return Response(status_code = 400)

@app.route('/Campaing/<int:idC>', methods = ['GET', 'PATCH'])
def api_manager_id(idC):
    
    if request.method == 'GET':
        jsonCampaing = Manager.returnCampaign(idC).to_json()
        res = Response(jsonCampaing, status = 200, mimetype = 'application/json')
        return res
        
    elif request.method == 'PATCH':
        if ('columnaAModif' in request.json) and ('campoColumna' in request.json):
            Manager.modifyCampaign(idC, request.json['columnaAModif'], request.json['campoColumna'])
            return Response(status_code = 202)
        else:
            return Response(status_code = 404)
        
    else:
        return Response(status_code = 404)

if __name__ == "__main__":
    app.run(debug=True)
