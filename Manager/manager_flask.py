'''
Created on Dec 10, 2018

@author: Gabriel Torrandella
'''
from flask import Flask, json
from flask.globals import request
from flask.wrappers import Response
from Campaign import Campaign
from Manager.manager import *

app = Flask(__name__)

def checkForm(form):

@app.route('/Campaing', methods = ['POST', 'DELETE'])
def api_manager():
    
    if request.method == 'POST':
        
        
        return request(status_code = 201)
        
    if request.method == 'DELETE':
        return request(status_code = 200)
        
    else: 
        return Response(status_code = 400)

if __name__ == "__main__":
    app.run()