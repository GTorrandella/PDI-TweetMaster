'''
Created on Dec 04, 2018

@author: Gabriel Torrandella
'''
from flask import Flask, json
import fetcher
from flask.globals import request
from flask.wrappers import Response
from Campaign import Campaign

def fixDate(stringDate):
    dateList = []
    for d in stringDate.split('-'):
        for ds in d.split(' '):
            dateList.append(ds)
    date = dateList[2] + " " + dateList[1] + " " + dateList[0] + " " + dateList[3]
    return date

app = Flask(__name__)

@app.route('/fetcher', methods = ['GET'])
def api_fetcher():
    
    if request.headers['Content-Type'] == 'application/json':
        if 'Campaing' in request.json and 'Last-ID' in request.json:
            cJson = json.loads(request.json['Campaing'])
            
            sd = fixDate(cJson["startDate"]) 
            ed = fixDate(cJson["finDate"])
            
            campaign = Campaign(cJson["id"],cJson["email"],cJson["hashtags"],cJson["mentions"],sd,ed)
                                    
            tweets = fetcher.Fetcher().fetchTweets(campaign)
            resp = Response(tweets, status = 200, mimetype = 'application/json')
            return resp
        else:
            return Response(status = 400)
            
    else:
        return Response(status = 400)


if __name__ == "__main__":
    app.run()
