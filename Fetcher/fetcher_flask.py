'''
Created on Dec 04, 2018

@author: Gabriel Torrandella
'''
from flask import Flask, json
from fetcher import Fetcher
from flask.globals import request
from flask.wrappers import Response

app = Flask(__name__)

@app.route('/fetcher', methods = ['GET'])
def api_fetcher():
    
    if request.headers['Content-Type'] == 'application/json':
        requestJson = json.dumps(request.json)
        campaign = requestJson['Campaing']
        lastId = requestJson['Last-ID']
        tweets =  Fetcher().fetchTweets(campaign, lastId)
        resp = Response(tweets, status = 200, mimetype = 'application/json')
        return resp
        
    else:
        return Response(status = 400)


if __name__ == "__main__":
    app.run()