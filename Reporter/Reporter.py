import sys
sys.path.append("..")
import json
from Campaign.Campaign import *
from Manager.manager import Manager
from dataBaseConnector import Connector

class Reporter():

	def getcampaign(idC):
		c_json = Connector().retornarCampaignBD(idC)	#Traer campaña de la BD
		c_dict = json.loads(c_json) 			#json a diccionario
		campaign = Campaign(c_dict("id"), c_dict("email"), c_dict("hashtags"), c_dict("mentions"), c_dict("startDate"), c_dict("finDate"))
		return campaign
	
	def reportRawData(idC):
		campaign = getcampaign(idC)
		#tweets = Connector().returnTweetsByIDC()  #Busca tweets de determinada campaña (falta hacer en Connector)
		
		for t in tweets:
			rawData = json.dumps(t)

		return (rawData)

	def reportSummary(campaign): 
		campaign = getcampaign(idC)
		#tweets = Connector().returnTweetsByIDC()  #Busca tweets de determinada campaña (falta hacer en Connector

        cant_tweets = countTweets(tweets)			#contar cantidad de tweets	
        dictionary = ["cant_tweets"] = cant_tweets	#lo agrego al diccionario
        summary = json.dumps(dictionary)
        #Cantidad diferente de usuarios

        #Autor con mas tweets

		campaignJson = campaign.to_json()

	def countTweets(tweets):
		cant_tweets = 0
        for cant_tweets in range tweets:
        	cant_tweets = cant_tweets +1
        	return cant_tweets

