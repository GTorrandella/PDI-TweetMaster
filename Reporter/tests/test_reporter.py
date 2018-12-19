from Campaign.Campaign import Campaign 
from Manager.manager import Manager 
from Tweet.Tweet import Tweet 
import unittest
from collections import Counter
import json

class test_reporter():
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
		"user" : {"name" : "MauricioOK", "id_str" : "451325"},
		"entities" : {"hashtags" : ["#DonaldNoMeDejes"], "user_mentions" : ["@donaldTrump", "@G20"]},
		"created_at" : "Sun Mar 20 21:08:01 +0000 2018",}
	tweet3 = {
		"id_str" : "112545",
		"user" : {"name" : "MauricioOK", "id_str" : "451325"},
		"entities" : {"hashtags" : ["#DonaldNoMeDejes"], "user_mentions" : ["@donaldTrump", "@G20"]},
		"created_at" : "Mon Mar 21 23:08:01 +0000 2018",}

	"""Objetos Tweet"""
	T1=Tweet(tweet1)
	T2=Tweet(tweet2)
	T3=Tweet(tweet3)
	"""Tweet().to_json()"""
	t1=T1.to_json()
	t2=T2.to_json()
	t3=T3.to_json()
	"""lista de Tweet().to_json()"""
	tweets = [tweet1,tweet2,tweet3]	#esto me llega de Connector().returnTweetsbyIDC(idC)
	"""c: diccionario / campaign:objeto"""
	c = {"id":"1234", "email":"donaldTrump@gmail.com","hashtags": ["#donaldTrump", "#G20"], "mentions": ["@donaldTrump", "@miauricioOK"], "startDate":"28 11 2018 18:02:00", "finDate":"02 12 2018 19:26:22"}
	campaign = Campaign(c["id"], c["email"], c["hashtags"], c["mentions"], c["startDate"], c["finDate"])
	
	def reportRawData(self): #OK 
		rawData = {"campaign" : self.campaign.to_dict(), "tweets" : self.tweets}
		return (json.dumps(rawData))

	def reportSummary(self, tweets, campaign): #OK
		#campaign = self.getCampaign(idC)
		#tweets = self.getCampaignTweets(idC)  #Busca tweets de determinada campaña (falta hacer en Connector

		summary = {
			"campaign" : self.campaign.to_dict(), #como diccionario para que se pueda acceder a los campos mas facil
			"cant_tweets" : len(self.tweets),
			"moreTwUser" : self.getUserWithMoreTw(self.tweets), #Autor con mas tweets
			"userQuantity": self.getUserQuantity(self.tweets), #Cantidad diferente de usuarios
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


#from Reporter.tests.test_reporter import test_reporter as TR
"""
if __name__ == '__main__':
    unittest.main()"""