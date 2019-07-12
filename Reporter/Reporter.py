import json
from DataBaseConnector.Connector import Connector
from collections import Counter
from datetime import datetime

class Reporter():

	def __init__(self, context='standar'):
		
		if context == 'test':
			self.database = Connector(context='test')
		
		else:
			self.database = Connector()

	def reportRawData(self, idC): #OK
		campaign = self.database.retornarCampaignBD(idC) #Objeto campaign, NO desempaquetamos el JSON, esto lo hace directamente flask. 
		tweets = self.database.returnTweetsByIDC(idC) #Busca tweets de determinada campaña
		
		if (campaign == [] or tweets == []):			#Revisa que exista campaña con esa ID
			return 404
		if (campaign.finDate > datetime.now()):		#la campana no finalizo aun
			return 412
		
		rawData = {"campaign" : campaign.to_dict(), "tweets" : tweets}
		return (rawData)

	def reportSummary(self, idC): #OK
		campaign = self.database.retornarCampaignBD(idC) #Objeto campaign, NO desempaquetamos el JSON, esto lo hace directamente flask. 
		tweets = self.database.returnTweetsByIDC(idC) #Lista de diccionarios tweet
		
		if (campaign == [] or tweets == []):			#Revisa que exista campaña con esa ID
			return 404
		if (campaign.finDate > datetime.now()):		#la campana no finalizo aun
			return 412
		
		summary = {
			"campaign" : campaign.to_dict(), #como diccionario para que se pueda acceder a los campos mas facil
			"cant_tweets" : len(tweets),
			"moreTwUser" : self.getUserWithMoreTw(tweets), #Autor con mas tweets
			"userQuantity": self.getUserQuantity(tweets), #Cantidad diferente de usuarios
		}
		return (summary)

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