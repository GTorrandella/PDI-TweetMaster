import sys
sys.path.append("..")
import json
from Tweet.Tweet import *
from Campaign.Campaign import *
from Manager.manager import Manager
from DataBaseConnector import Connector
from collections import Counter

class Reporter():
	"""Hardcodeanding"""
	"""tweets diccionario"""
	tweet1 = {
        "id_str" : "123456",
        "user" : {"name" : "NASAOk", "id_str" : "789456"},
        "entities" : {"hashtags" : ["#mars","#venus","#earth"],"user_mentions" : ["@NASA", "@planets"]},
        "created_at" : "Sun Mar 20 15:11:01 +0000 2018",
    }
	tweet2 = {
		"id_str" : "112112",
		"user" : {"name" : "MiauricioOK", "id_str" : "451325"},
		"entities" : {"hashtags" : ["#DonaldNoMeDejes"], "user_mentions" : ["@donaldTrump", "@G20"]},
		"created_at" : "Sun Mar 20 21:08:01 +0000 2018",}	
	"""Objetos Tweet"""
	T1=Tweet(tweet1)
	T2=Tweet(tweet2)
	"""Tweet().to_json()"""
	t1=T1.to_json()
	t2=T2.to_json()
	"""lista de Tweet().to_json()"""
	tweets = [t1,t2]	#esto me llega de Connector().returnTweetsbyIDC(idC)
	"""c: diccionario / campaign:objeto"""
	c = {"id":"1234", "email":"donaldTrump@gmail.com","hashtags": ["#donaldTrump", "#G20"], "mentions": ["@donaldTrump", "@miauricioOK"], "startDate":"28 11 2018 18:02:00", "finDate":"02 12 2018 19:26:22"}
	campaign = Campaign(c["id"], c["email"], c["hashtags"], c["mentions"], c["startDate"], c["finDate"])


	def getCampaign(self, idC): #OK falta probar con lo de Connector
		c_dict = Connector().retornarCampaignBD(idC)	#Traer campaña de la BD (diccionario)
		campaign = Campaign(c_dict["id"], c_dict["email"], c_dict["hashtags"], c_dict["mentions"], c_dict["startDate"], c_dict["finDate"])
		return campaign

	def getCampaignTweets(self, idC): #OK falta lo de Connector y probarlo con eso
		#tweetsJson = Connector().returnTweetsByIDC(idC)  #Busca tweets de determinada campaña (falta hacer en Connector)
		#tweetsJson es lista de json -> tengo que pasarlos a diccionario
		tweets = []	
		tweets=self.getDictList(tweetsJson) 
		return (tweetsList) #lista de tw_diccionario

	def reportRawData(self, idC): #OK rawData
		campaign = self.getCampaign(idC)	#Busco la campaña con un idCampaña
		tweetsList = self.getCampaignTweets(idC) #Busca tweets de determinada campaña (falta hacer en Connector)
		rawData = {"campaign" : campaign.to_dict(), "tweets" : tweetsList}
		return (rawData)

	def reportSummary(self, tweets, campaign): #OK
		#campaign = self.getCampaign(idC)
		#tweets = self.getCampaignTweets(idC)  #Busca tweets de determinada campaña (falta hacer en Connector

		summary = {
			"campaign" : campaign.to_dict(), #como diccionario para que se pueda acceder a los campos mas facil
			"cant_tweets" : len(tweets),
			"moreTwUser" : self.getUserWithMoreTw(tweets), #Autor con mas tweets
			"userQuantity": self.getUserQuantity(tweets), #Cantidad diferente de usuarios
		}
		return summary

	def getUserWithMoreTw(self,jsonTweets): #OK (falta el caso en que sean varios users en el 1er puesto)
		tweets=self.getDictList(jsonTweets)
		users=[]
		for t in tweets:
			users.append(t["user"]["name"])	#Lista de user names
		count=Counter(users).most_common(1)
		mostTwUser=count[0][0]
		return mostTwUser

	def getUserQuantity(self, jsonTweets): #OK
		dictTweets=self.getDictList(jsonTweets)
		users=self.getUsersList(dictTweets)
		count=Counter(users)	#contador de ocurrencias en users
		uQuantity= len(count)	#cantidad de usuarios distintos
		return uQuantity

	def getUsersList(self,dictTweets): #OK
		users=[]
		for t in dictTweets:
			users.append(t["user"]["name"])	#Lista de user names
		return users

	def getDictList(self,jsonList): #OK
		dictList = []	
		for j in jsonList:
			dictList.append(json.loads(j)) #Armo lista de diccionarios
		return (dictList)


#exec(open("Reporter.py").read())