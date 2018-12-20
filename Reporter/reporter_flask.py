'''
Created on Dec 12, 2018

@author: Gabriel Torrandella
'''
from flask import Flask, jsonify
from flask.globals import request
from flask.wrappers import Response

from Reporter.Reporter import Reporter

app = Flask(__name__)

@app.route('/Reporter/ReporterJSON/<int:idC>', methods = ['GET'])
def api_report_json(idC):
    if True: # Aca se fija si existe el recurso
        summary = Reporter().reportSummary(idC)
        if summary == []:
            return Response(status = 404)
        return jsonify(summary)
            
    else:
        return Response(status = 404)
    
@app.route('/Reporter/ReporterRAW/<int:idC>', methods = ['GET'])
def api_report_raw(idC):
    
    if True:
        data = Reporter().reportRawData(idC)
        if data == []:
            return Response(status = 404)
        return jsonify(data)
    else:
        return Response(status = 404)

if __name__ == "__main__":
    app.run()
