'''
Created on Dec 12, 2018

@author: Gabriel Torrandella
'''
from flask import Flask, jsonify
from flask.wrappers import Response

from Reporter.Reporter import Reporter

app = Flask(__name__)

@app.route('/Reporter/ReporterJSON/<int:idC>', methods = ['GET'])
def api_report_json(idC):
    
    summary = Reporter().reportSummary(idC)
    if summary == 404:
        return Response(status = 404)
    elif summary == 412:
        return Response(status = 412)
    return jsonify(summary)
    
@app.route('/Reporter/ReporterRAW/<int:idC>', methods = ['GET'])
def api_report_raw(idC):
    
    data = Reporter().reportRawData(idC)
    if data == 404:
        return Response(status = 404)
    elif data == 412:
        return Response(status = 412)
    return jsonify(data)
    
if __name__ == "__main__":
    app.run()
