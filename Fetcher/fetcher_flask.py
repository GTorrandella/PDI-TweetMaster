'''
Created on Dec 04, 2018

@author: Gabriel Torrandella
'''
from flask import Flask, json, jsonify
from flask.globals import request
from flask.wrappers import Response

import Fetcher.fetcher as fetcher
from Campaign.Campaign import Campaign

from os import path


def fixDate(stringDate):
    dateList = []
    for d in stringDate.split('-'):
        for ds in d.split(' '):
            dateList.append(ds)
    date = dateList[0] + " " + dateList[1] + " " + dateList[2] + " " + dateList[3]
    return date

app = Flask(__name__)

@app.route('/fetcher', methods = ['GET'])
def api_fetcher():
    if 'Content-Type' in request.headers.keys():
        if request.headers['Content-Type'] == 'application/json':
            if 'Campaign' in request.json.keys():
                
                cJson = json.loads(request.json['Campaign'])
                
                sd = fixDate(cJson["startDate"]) 
                ed = fixDate(cJson["finDate"])
                
                campaign = Campaign(cJson["id"],cJson["email"],cJson["hashtags"],cJson["mentions"],sd,ed)
                                        
                tweets = jsonify(fetcher.Fetcher().fetchTweets(campaign))
                parentDir = path.dirname(path.abspath(__file__))
                tokenPath = path.join(parentDir, 'log')
                f = open(tokenPath, 'w')
                f.write(str(tweets))
                f.close
                return tweets
            else:
                return Response(status = 400)
                
    else:
        return Response(status = 400)


if __name__ == "__main__":
    app.run()
