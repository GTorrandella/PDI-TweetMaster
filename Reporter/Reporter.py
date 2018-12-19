import json
from Tweet.Tweet import Tweet
from Campaign.Campaign import Campaign
from Manager.manager import Manager
import DataBaseConnector.Connector as Connector
from collections import Counter

class Reporter():

	def getCampaignAndTweets(self, idC): #OK falta lo de Connector y probarlo con eso
		tweets = Connector().returnTweetsByIDC(idC)  #Busca tweets de determinada campaña (falta hacer en Connector)
		#tweetsJson es lista de json -> tengo que pasarlos a diccionario
		return (tweets) #lista de tw_diccionario
	
	def reportRawData(self, idC): #OK rawData
		campaign = Connector().retornarCampaignBD(idC): #Objeto campaign
		tweets = Connector().returnTweetsByIDC(idC) #Lista de diccionarios tweet
		rawData = {"campaign" : campaign.to_dict(), "tweets" : tweets}
		return (json.dumps(rawData))

	def reportSummary(self, idC): #OK
		campaign = Connector().retornarCampaignBD(idC): #Objeto campaign
		tweets = Connector().returnTweetsByIDC(idC) #Lista de diccionarios tweet

		summary = {
			"campaign" : campaign.to_dict(), #como diccionario para que se pueda acceder a los campos mas facil
			"cant_tweets" : len(tweets),
			"moreTwUser" : self.getUserWithMoreTw(tweets), #Autor con mas tweets
			"userQuantity": self.getUserQuantity(tweets), #Cantidad diferente de usuarios
		}
		return (json.dumps(summary))

	def getUserWithMoreTw(self,tweets): #OK (falta el caso en que sean varios users en el 1er puesto)
		users=[]
		for t in tweets:
			users.append(t["user"]["name"])	#Lista de user names
		count=Counter(users).most_common(1)
		mostTwUser=count[0][0]
		return mostTwUser

	def getUserQuantity(self, dictTweets): #OK
		users=self.getUsersList(dictTweets)
		count=Counter(users)	#contador de ocurrencias en users
		uQuantity= len(count)	#cantidad de usuarios distintos
		return uQuantity

	def getUsersList(self,dictTweets): #OK
		users=[]
		for t in dictTweets:
			users.append(t["user"]["name"])	#Lista de user names
		return users