'''
Created on Dec 12, 2018

@author: Gabriel Torrandella
'''
from flask import Flask, json
from flask.globals import request
from flask.wrappers import Response

from Reporter import Reporter

app = Flask(__name__)

@app.route('/Reporter/ReporterJSON/<int:idC> ', methods = ['GET'])
def api_report_json(idC):
    
    if True: # Aca se fija si existe el recurso
        json = Reporter().reportSummary(idC)
        return Response(json, status = 200, mimetype='aplication/json')
            
    else:
        return Response(status = 404)
    
@app.route('/Reporter/ReporterRAW/<int:idC> ', methods = ['GET'])
def api_report_raw(idC):
    
    if True:
        data = Reporter().reportRawData(idC)
        return Response(data, status = 200)
    else:
        return Response(status = 404)

if __name__ == "__main__":
    app.run()
