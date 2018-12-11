'''
Created on Dec 10, 2018

@author: Gabriel Torrandella
'''
from flask import Flask, json
from fetcher import Fetcher
from flask.globals import request
from flask.wrappers import Response
from Campaign import Campaign

app = Flask(__name__)

@app.route('/fetcher', methods = ['GET'])
def api_fetcher():
    
    if request.headers['Content-Type'] == 'application/json':
        if 'Campaing' in request.json and 'Last-ID' in request.json:
            cJson = json.loads(request.json['Campaing'])
            lastId = request.json['Last-ID']
            
            campaign = Campaign(cJson["id"],cJson["email"],cJson["hastags"],cJson["mentions"],sd,ed)
                                    
            tweets =  Fetcher().fetchTweets(campaign, lastId)
            resp = Response(tweets, status = 200, mimetype = 'application/json')
            return resp
        else:
            return Response(status = 400)
            
    else:
        return Response(status = 400)


if __name__ == "__main__":
    app.run()