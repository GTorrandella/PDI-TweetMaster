from flask import Flask, jsonify
from flask.globals import request
from flask.wrappers import Response, Request
from werkzeug.wrappers import ETagRequestMixin, ETagResponseMixin, BaseRequest, BaseResponse
from Manager.manager import Manager
from Campaign.Campaign import Campaign

app = Flask(__name__)

def checkForm(json):
    keys = json.keys()
    return ('email' in keys and "hashtags" in keys and "mentions" in keys and "startDate" in keys and "endDate" in keys)

#Goes from guinated string to list
def fixCampaing(c):
    c.hashtags = c.hashtags.split("-")
    c.mentions = c.mentions.split("-")
    return c

def defineContext(context='standar'):
    global manager
    if context == 'test':
        manager = Manager(context='test')
    else:
        manager = Manager()

@app.route('/Campaing', methods = ['POST', 'DELETE'])
def api_manager():
    
    if request.method == 'POST' and 'application/json' == request.headers['Content-Type']:
        if checkForm(request.json):
            idCampaing = manager.insertCampaign(request.get_json())
            res = Response(status = 201)
            res.set_etag(str(idCampaing), weak = False)    
            return res
        else:
            return Response(status = 412)
        
    elif request.method == 'DELETE':
        if 'idC' in request.json.keys():
            res = manager.deleteCampaignByID(request.json['idC'])
            return Response(status = res)
        elif 'email' in request.json.keys():
            res = manager.deleteCampaignsByEmail(request.json['email'])
            return Response(status = res)
        else:
            return Response(status = 412)
    else: 
        return Response(status = 400)

@app.route('/Campaing/<int:idC>', methods = ['GET', 'PATCH'])
def api_manager_id(idC):
    
    if request.method == 'GET':
        campaign = manager.returnCampaign(idC)
        return (Response(status = 404) if campaign == [] else jsonify(fixCampaing(campaign).to_json()))

    elif request.method == 'PATCH':
        if ('columnaAModif' in request.json.keys()) and ('campoColumna' in request.json.keys()):
            res = manager.modifyCampaign(idC, request.json['columnaAModif'], request.json['campoColumna'])
            return Response(status = res)  
        else: return Response(status = 412)   
    else:
        return Response(status = 404)

if __name__ == "__main__":
    defineContext()
    app.run(debug=True)