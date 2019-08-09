import unittest
from Tweet.Tweet import Tweet 
from Campaign.Campaign import Campaign
from datetime import date
from DataBaseConnector import Connector, configTables
from Manager.manager import Manager
from Reporter.Reporter import Reporter
import json

class test_reporter(unittest.TestCase):
	
	def setUpInitialData(self):
		self.connector = Connector.Connector(context='test')
		
		testCampaign1 = Campaign(1, "test@gmail.com", "#test-#mock", "@testCampaign-@mockOK", "28 11 2018 18:02:00", "25 12 2018 19:26:22")
		
		testTweet1 = Tweet({ "id_str" : "345",
		 					"user" : {"name" : "NASAOk", "id_str" : "789456"}, 
							"entities" : {
								 "hashtags" : ["#mars","#venus","#earth"],
								 "user_mentions" : ["@NASA", "@planets"]
								 }, 
							"created_at" : "Sun Mar 20 15:11:01 +0000 2018",
							"text" : ""}, True)
		testTweet2 = Tweet({ "id_str" : "564",
							 "user" : {"name" : "MauricioOK", "id_str" : "451325"}, 
							 "entities" : {
								 "hashtags" : ["#DonaldNoMeDejes"], 
								 "user_mentions" : ["@donaldTrump", "@G20"]
								 }, 
							 "created_at" : "Sun Mar 20 21:08:01 +0000 2018",
							 "text" : ""}, True)

		self.idTestCampaign1 = self.connector.insertCampaign(testCampaign1)
		self.connector.insertTweet(testTweet1, self.idTestCampaign1)
		self.connector.insertTweet(testTweet2, self.idTestCampaign1)

	def setUp(self):
		self.manager = Manager('test')
		self.reporter = Reporter('test')

		self.setUpInitialData()


	def tearDown(self):
		self.connector.database.session.query(configTables.Tweet).delete()
		self.connector.database.session.query(configTables.Campaign).delete()
		self.connector.database.session.commit()

	#Dada la campaña y tweets testeamos si los datos summary son retornados correctamente:
	def test_reportSummary(self):  #OK
		summary = self.reporter.reportSummary(self.idTestCampaign1)
		print(summary)
		#Devuelve esto: 
		#

	#Dada la campaña y tweets testeamos si los datos raw son retornados correctamente:
	def test_reportRawData(self):
		"""
		#Precondicion: necesitamos una campaña con tweets asociados:
		campaign= '{"email":"test@gmail.com","hashtags": ["#test", "#mock"], "mentions": ["@testCampaign", "@mockOK"], "startDate":"28 11 2018 18:02:00", "endDate":"25 12 2018 19:26:22"}'
		fields = json.loads(campaign)
		self.manager.insertCampaign(fields)
		self.manager.insertCampaign(fields)
		self.manager.insertCampaign(fields)
		#Inicializamos los Tweets diccionarios:
		tweet1 = { "id_str" : "123456", "user" : {"name" : "NASAOk", "id_str" : "789456"}, "entities" : {"hashtags" : ["#mars","#venus","#earth"],"user_mentions" : ["@NASA", "@planets"]}, "created_at" : "Sun Mar 20 15:11:01 +0000 2018", }
		tweet2 = { "id_str" : "112112", "user" : {"name" : "MauricioOK", "id_str" : "451325"}, "entities" : {"hashtags" : ["#DonaldNoMeDejes"], "user_mentions" : ["@donaldTrump", "@G20"]}, "created_at" : "Sun Mar 20 21:08:01 +0000 2018",}
		#Para pasarlos a un objeto Tweet: T1=Tweet(tweet1)
		#Para pasar estos objetos Tweet a Json usando el metodo to_json del objeto Tweet: t1=T1.to_json()
		tweetsJson = json.dumps([tweet1,tweet2])
		#Insertamos los tweets en la Campaign 3
		self.manager.insertTweets(tweetsJson, 3)s
		"""

		raw_data = self.reporter.reportRawData(self.idTestCampaign1)
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
		
		mostTwUser = self.reporter.getUserWithMoreTw(tweets)
		return mostTwUser
		#asserts....

	#Testeamos retornar el usuario con mayor cantidad de menciones:
	def test_getUserQuantity(self): #OK
		#VEr--> dictTweets=
		userQuantity = (self.reporter.getUserQuantity(dictTweets))
		return userQuantity
		#assert userQuantity == NUMERO
	
	#Testeamos retornamos todos los usuarios:
	def test_getUsersList(self): #OK
		#VEr--> dictTweets=
		usersList = (self.reporter.getUsersList(dictTweets))
		return usersList
		#asserts....