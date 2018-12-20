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
	
	#Dada la campaña y tweets testeamos si los datos summary son retornados correctamente:
	def test_reportSummary(self):  #OK
		#Precondicion: necesitamos una campaña con tweets asociados:
		campaign= '{"email":"test@gmail.com","hashtags": ["#test", "#mock"], "mentions": ["@testCampaign", "@mockOK"], "startDate":"28 11 2018 18:02:00", "endDate":"25 12 2018 19:26:22"}'
		fields = json.loads(campaign)
		manager.Manager().insertCampaign(fields)
		manager.Manager().insertCampaign(fields)
		#Inicializamos los Tweets diccionarios:
		tweet1 = { "id_str" : "345", "user" : {"name" : "NASAOk", "id_str" : "789456"}, "entities" : {"hashtags" : ["#mars","#venus","#earth"],"user_mentions" : ["@NASA", "@planets"]}, "created_at" : "Sun Mar 20 15:11:01 +0000 2018", }
		tweet2 = { "id_str" : "564", "user" : {"name" : "MauricioOK", "id_str" : "451325"}, "entities" : {"hashtags" : ["#DonaldNoMeDejes"], "user_mentions" : ["@donaldTrump", "@G20"]}, "created_at" : "Sun Mar 20 21:08:01 +0000 2018",}
		#Para pasarlos a un objeto Tweet: T1=Tweet(tweet1)
		#Para pasar estos objetos Tweet a Json usando el metodo to_json del objeto Tweet: t1=T1.to_json()
		tweetsJson = json.dumps([tweet1,tweet2])
		#Insertamos los tweets en la Campaign 3
		manager.Manager().insertTweets(tweetsJson, 2)
		summary = Reporter.Reporter().reportSummary(2)
		print(summary)
		#Devuelve esto: 
		#

	#Dada la campaña y tweets testeamos si los datos raw son retornados correctamente:
	def test_reportRawData(self):
		#Precondicion: necesitamos una campaña con tweets asociados:
		campaign= '{"email":"test@gmail.com","hashtags": ["#test", "#mock"], "mentions": ["@testCampaign", "@mockOK"], "startDate":"28 11 2018 18:02:00", "endDate":"25 12 2018 19:26:22"}'
		fields = json.loads(campaign)
		manager.Manager().insertCampaign(fields)
		manager.Manager().insertCampaign(fields)
		manager.Manager().insertCampaign(fields)
		#Inicializamos los Tweets diccionarios:
		tweet1 = { "id_str" : "123456", "user" : {"name" : "NASAOk", "id_str" : "789456"}, "entities" : {"hashtags" : ["#mars","#venus","#earth"],"user_mentions" : ["@NASA", "@planets"]}, "created_at" : "Sun Mar 20 15:11:01 +0000 2018", }
		tweet2 = { "id_str" : "112112", "user" : {"name" : "MauricioOK", "id_str" : "451325"}, "entities" : {"hashtags" : ["#DonaldNoMeDejes"], "user_mentions" : ["@donaldTrump", "@G20"]}, "created_at" : "Sun Mar 20 21:08:01 +0000 2018",}
		#Para pasarlos a un objeto Tweet: T1=Tweet(tweet1)
		#Para pasar estos objetos Tweet a Json usando el metodo to_json del objeto Tweet: t1=T1.to_json()
		tweetsJson = json.dumps([tweet1,tweet2])
		#Insertamos los tweets en la Campaign 3
		manager.Manager().insertTweets(tweetsJson, 3)

		raw_data = Reporter.Reporter().reportRawData(3)
		print(raw_data)
		#Devuelve esto: 
		#{'campaign': {'id': 3, 'email': 'test@gmail.com', 'hashtags': '#test-#mock', 'mentions': '@testCampaign-@mockOK', 'startDate': '28 11 2018 18:02:00', 'finDate': '25 12 2018 19:26:22'}, 'tweets': {'tweet0': [{'id_str': 112112, 'user': {'name': 'MauricioOK', 'id_str': '451325'}, 'entities': {'hashtags': '#DonaldNoMeDejes', 'user_mentions': '@donaldTrump-@G20'}, 'created_at': '2018-03-20 21:08:01'}], 'tweet1': [{'id_str': 123456, 'user': {'name': 'NASAOk', 'id_str': '789456'}, 'entities': {'hashtags': '#mars-#venus-#earth', 'user_mentions': '@NASA-@planets'}, 'created_at': '2018-03-20 15:11:01'}]}}

	#Dados tweets testeamos retornar el usuario con mayor cantidad de tweets:
	def test_getUserWithMoreTw(self): #OK (falta el caso en que sean varios users en el 1er puesto)
		
		#Inicializamos los Tweets diccionarios:
		tweet1 = { "id_str" : "123456", "user" : {"name" : "NASAOk", "id_str" : "789456"}, "entities" : {"hashtags" : ["#mars","#venus","#earth"],"user_mentions" : ["@NASA", "@planets"]}, "created_at" : "Sun Mar 20 15:11:01 +0000 2018", }
		tweet2 = { "id_str" : "112112", "user" : {"name" : "MauricioOK", "id_str" : "451325"}, "entities" : {"hashtags" : ["#DonaldNoMeDejes"], "user_mentions" : ["@donaldTrump", "@G20"]}, "created_at" : "Sun Mar 20 21:08:01 +0000 2018",}
		tweet3 = { "id_str" : "112545", "user" : {"name" : "MauricioOK", "id_str" : "451325"}, "entities" : {"hashtags" : ["#DonaldNoMeDejes"], "user_mentions" : ["@donaldTrump", "@G20"]}, "created_at" : "Mon Mar 21 23:08:01 +0000 2018",}
		#Para pasarlos a un objeto Tweet: T1=Tweet(tweet1)
		#Para pasar estos objetos Tweet a Json usando el metodo to_json del objeto Tweet: t1=T1.to_json()
		
		#Lo que me llegaría de Connector().returnTweetsbyIDC(idC):
		tweets = [tweet1,tweet2,tweet3]
		mostTwUser = Reporter.Reporter().getUserWithMoreTw(tweets)
		return mostTwUser
		#asserts....

	#Testeamos retornar el usuario con mayor cantidad de menciones:
	def test_getUserQuantity(self): #OK
		#VEr--> dictTweets=
		userQuantity = (Reporter.Reporter().getUserQuantity(self, dictTweets))
		return userQuantity
		#assert userQuantity == NUMERO
	
	#Testeamos retornamos todos los usuarios:
	def test_getUsersList(self): #OK
		#VEr--> dictTweets=
		usersList = (Reporter.Reporter().getUsersList(self, dictTweets))
		return usersList
		#asserts....