import sys
sys.path.append("..")
import json
from Campaign import Campaign
from manager import Manager
import Connector

class Reporter():

	def getcampaign(self,idC):
		c_json = Connector().retornarCampaignBD(idC)	#Traer campaña de la BD
		c_dict = json.loads(c_json) 			#json a diccionario
		campaign = Campaign(c_dict("id"), c_dict("email"), c_dict("hashtags"), c_dict("mentions"), c_dict("startDate"), c_dict("finDate"))
		return campaign
	
	def reportRawData(self,idC):
		campaign = self.getcampaign(idC)
		#tweets = Connector().returnTweetsByIDC()  #Busca tweets de determinada campaña (falta hacer en Connector)
		
		for t in tweets:
			rawData = json.dumps(t)

		return (rawData)

	def countTweets(self, tweets):
		cant_tweets = 0
        for cant_tweets in range tweets:
        	cant_tweets = cant_tweets +1
        	return cant_tweets
        
	def reportSummary(self, idC): 
		campaign = self.getcampaign(idC)
		#tweets = Connector().returnTweetsByIDC()  #Busca tweets de determinada campaña (falta hacer en Connector
		
		cant_tweets = self.countTweets(tweets)			#contar cantidad de tweets	
        dictionary = ["cant_tweets"] = cant_tweets	#lo agrego al diccionario
        summary = json.dumps(dictionary)
        #Cantidad diferente de usuarios

        #Autor con mas tweets

		campaignJson = campaign.to_json()


