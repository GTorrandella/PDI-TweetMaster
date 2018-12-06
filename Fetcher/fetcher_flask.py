'''
Created on Dec 04, 2018

@author: Gabriel Torrandella
'''
from flask import Flask, json
from fetcher import Fetcher
from flask.globals import request
from flask.wrappers import Response
from Campaign import Campaign

def fixDate(stringDate):
    date = []
    for d in stringDate.split('-'):
        date.append(int(d))
    return date

app = Flask(__name__)

@app.route('/fetcher', methods = ['GET'])
def api_fetcher():
    
    if request.headers['Content-Type'] == 'application/json':
        cJson = json.loads(request.json['Campaing'])
        lastId = request.json['Last-ID']
        
        sd = fixDate(cJson["startDate"]) 
        ed = fixDate(cJson["finDate"])
        
        campaign = Campaign(cJson["id"],cJson["email"],cJson["hastags"],cJson["mentions"],sd,ed)
                                
        tweets =  Fetcher().fetchTweets(campaign, lastId)
        resp = Response(tweets, status = 200, mimetype = 'application/json')
        return resp
        
    else:
        return Response(status = 400)


if __name__ == "__main__":
    app.run()