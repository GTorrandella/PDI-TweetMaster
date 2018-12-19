import unittest
from Reporter import Reporter
from collections import Counter
from Tweet.Tweet import Tweet 
from Campaign.Campaign import Campaign
from datetime import date
from DataBaseConnector import Connector
from Manager import manager
import json

class test_reporter(unittest.TestCase):
	
	#Dada la campaña y tweets testeamos si los datos raw son retornados correctamente:
	def test_reportRawData(self):  #OK

		#Inicializamos los Tweets diccionarios:
		tweet1 = { "id_str" : "123456", "user" : {"name" : "NASAOk", "id_str" : "789456"}, "entities" : {"hashtags" : ["#mars","#venus","#earth"],"user_mentions" : ["@NASA", "@planets"]}, "created_at" : "Sun Mar 20 15:11:01 +0000 2018", }
		tweet2 = { "id_str" : "112112", "user" : {"name" : "MauricioOK", "id_str" : "451325"}, "entities" : {"hashtags" : ["#DonaldNoMeDejes"], "user_mentions" : ["@donaldTrump", "@G20"]}, "created_at" : "Sun Mar 20 21:08:01 +0000 2018",}
		tweet3 = { "id_str" : "112545", "user" : {"name" : "MauricioOK", "id_str" : "451325"}, "entities" : {"hashtags" : ["#DonaldNoMeDejes"], "user_mentions" : ["@donaldTrump", "@G20"]}, "created_at" : "Mon Mar 21 23:08:01 +0000 2018",}
		#Para pasarlos a un objeto Tweet: T1=Tweet(tweet1)
		#Para pasar estos objetos Tweet a Json usando el metodo to_json del objeto Tweet: t1=T1.to_json()
		
		#Lo que me llegaría de Connector().returnTweetsbyIDC(idC):
		tweets = [tweet1,tweet2,tweet3]

		#Inicializamos un objeto campaign a partir de un diccionario c_
		c = {"id":"1234", "email":"donaldTrump@gmail.com","hashtags": ["#donaldTrump", "#G20"], "mentions": ["@donaldTrump", "@miauricioOK"], "startDate":"28 11 2018 18:02:00", "finDate":"02 12 2018 19:26:22"}
		self.campaign = Campaign(c["id"], c["email"], c["hashtags"], c["mentions"], c["startDate"], c["finDate"])
	
		rawData = {"campaign" : self.campaign, "tweets" : tweets}
		return (json.dumps(rawData))

	#Dada la campaña y tweets testeamos si los datos summary son retornados correctamente:
	def test_reportSummary(self, tweets, campaign):  #OK
		
		#Inicializamos los Tweets diccionarios:
		tweet1 = { "id_str" : "123456", "user" : {"name" : "NASAOk", "id_str" : "789456"}, "entities" : {"hashtags" : ["#mars","#venus","#earth"],"user_mentions" : ["@NASA", "@planets"]}, "created_at" : "Sun Mar 20 15:11:01 +0000 2018", }
		tweet2 = { "id_str" : "112112", "user" : {"name" : "MauricioOK", "id_str" : "451325"}, "entities" : {"hashtags" : ["#DonaldNoMeDejes"], "user_mentions" : ["@donaldTrump", "@G20"]}, "created_at" : "Sun Mar 20 21:08:01 +0000 2018",}
		tweet3 = { "id_str" : "112545", "user" : {"name" : "MauricioOK", "id_str" : "451325"}, "entities" : {"hashtags" : ["#DonaldNoMeDejes"], "user_mentions" : ["@donaldTrump", "@G20"]}, "created_at" : "Mon Mar 21 23:08:01 +0000 2018",}
		#Para pasarlos a un objeto Tweet: T1=Tweet(tweet1)
		#Para pasar estos objetos Tweet a Json usando el metodo to_json del objeto Tweet: t1=T1.to_json()
		
		#Lo que me llegaría de Connector().returnTweetsbyIDC(idC):
		tweets = [tweet1,tweet2,tweet3]

		#Inicializamos un objeto campaign a partir de un diccionario c_
		c = {"id":"1234", "email":"donaldTrump@gmail.com","hashtags": ["#donaldTrump", "#G20"], "mentions": ["@donaldTrump", "@miauricioOK"], "startDate":"28 11 2018 18:02:00", "finDate":"02 12 2018 19:26:22"}
		self.campaign = Campaign(c["id"], c["email"], c["hashtags"], c["mentions"], c["startDate"], c["finDate"])

		summary = {
			"campaign" : self.campaign.to_dict(), #como diccionario para que se pueda acceder a los campos mas facil
			"cant_tweets" : len(tweets),
			"moreTwUser" : self.getUserWithMoreTw(tweets), #Autor con mas tweets
			"userQuantity": self.getUserQuantity(tweets), #Cantidad diferente de usuarios
		}
		return (summary)

	#Dados tweets testeamos retornar el usuario con mayor cantidad de tweets:
	def test_getUserWithMoreTw(self,tweets): #OK (falta el caso en que sean varios users en el 1er puesto)
		
		#Inicializamos los Tweets diccionarios:
		tweet1 = { "id_str" : "123456", "user" : {"name" : "NASAOk", "id_str" : "789456"}, "entities" : {"hashtags" : ["#mars","#venus","#earth"],"user_mentions" : ["@NASA", "@planets"]}, "created_at" : "Sun Mar 20 15:11:01 +0000 2018", }
		tweet2 = { "id_str" : "112112", "user" : {"name" : "MauricioOK", "id_str" : "451325"}, "entities" : {"hashtags" : ["#DonaldNoMeDejes"], "user_mentions" : ["@donaldTrump", "@G20"]}, "created_at" : "Sun Mar 20 21:08:01 +0000 2018",}
		tweet3 = { "id_str" : "112545", "user" : {"name" : "MauricioOK", "id_str" : "451325"}, "entities" : {"hashtags" : ["#DonaldNoMeDejes"], "user_mentions" : ["@donaldTrump", "@G20"]}, "created_at" : "Mon Mar 21 23:08:01 +0000 2018",}
		#Para pasarlos a un objeto Tweet: T1=Tweet(tweet1)
		#Para pasar estos objetos Tweet a Json usando el metodo to_json del objeto Tweet: t1=T1.to_json()
		
		#Lo que me llegaría de Connector().returnTweetsbyIDC(idC):
		tweets = [tweet1,tweet2,tweet3]
		mostTwUser = Reporter().getUserWithMoreTw(tweets)
		return mostTwUser
		#asserts....

	#Testeamos retornar el usuario con mayor cantidad de menciones:
	def test_getUserQuantity(self): #OK
		#VEr--> dictTweets=
		userQuantity = (Reporter().getUserQuantity(self, dictTweets))
		return userQuantity
		#assert userQuantity == NUMERO
	
	#Testeamos retornamos todos los usuarios:
	def test_getUsersList(self): #OK
		#VEr--> dictTweets=
		usersList = (Reporter().getUsersList(self, dictTweets))
		return usersList
		#asserts....