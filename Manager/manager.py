import json
from Campaign.Campaign import Campaign
from DataBaseConnector import configTables 
from datetime import datetime
from DataBaseConnector import Connector
from Tweet.Tweet import Tweet
import requests

class Manager():
	def insertCampaign(self, userInputs):
		configTables.BD.metadata.create_all(configTables.engine)
		#Con los nombres de los campos correspondientes a los del json que nos llegan armamos un objeto campaña.
		#Pero antes de esto como fields["hashtags"] y fields["mentions"] son LISTAS, tenemos que pasarlas a un string para poder añadirlo a la BD como un varchar: 
		stringHashtag = self.listaAString(userInputs["hashtags"]) # #donaldTrump-#G20
		stringMention = self.listaAString(userInputs["mentions"]) # @donaldTrump-@miauricioOK
	
		campaign = Campaign(1, userInputs["email"], stringHashtag, stringMention, userInputs["startDate"], userInputs["endDate"])
		#Llamamos a un metodo de Connector para agregar la campaña a la BD junto con las mentions y los hashtags:
		return Connector.insertarCampaignBD(campaign)

	def listaAString(self, lista):
		string = "-".join(lista)
		return string
	
	def deleteCampaignporuser(self, email_user):
		campaigns = Connector.retornarCampaignsBDxEmail(email_user)

		if campaigns == []:	#No hubo campaigns con ese e-mail
			return 404

		haveDeleted = False		#flag
		for c in campaigns:
			if not c.isActive():
				Connector.eliminarTweetsxIDC(c.idC)
				Connector.eliminarCampaignBDxID(c.idC)
				haveDeleted = True

		if haveDeleted: #Borro una o mas campaigns
			return 200
		else:
			return 412	#No borro nada porque todas estaban activas

	def deleteCampaignporid(self, idCampaign):
		#Se puede eliminar la campaña sólo si esta NO está iniciada:
		campaignRetornada = Connector.retornarCampaignBD(idCampaign)

		if campaignRetornada == []: 
			return 404
		if campaignRetornada.isActive(): 
			return 412
		else: 
			Connector.eliminarTweetsxIDC(idCampaign)
			Connector.eliminarCampaignBDxID(idCampaign)
			return 200
				
	def returnCampaign(self, idCampaign):
		return Connector.retornarCampaignBD(idCampaign)

	def returnCampaignsInProgress(self):
		return Connector.returnCampaignsInProgress()

	def modifyCampaign(self, idCampaign, columna, inputUser):
		c = Connector.retornarCampaignBD(idCampaign)
		if c == []:
			return 404		# No existe
		if c.isActive():	
			return 412		# Campaign activa
		# Campaign NO esta activa:
		wasModified = Connector.modificarCampaignBD(idCampaign, columna, inputUser)
		if wasModified: 
			return 200	# OK
		return 400		# Columna inexistente

	# Fijarse en test_manager que sería este tweetsJson que recibe.
	def insertTweets(self, tweetsJson, idC):
		configTables.BD.metadata.create_all(configTables.engine)
		#Los separamos en tweets separados y llamamos a insertTweet para agregarlo uno por uno:
		for tweet in tweetsJson:
			t = Tweet(json.loads(tweet))
			print ("Tweet en manager")
			print (tweet)
			print (t)
			self.insertTweet(t,idC) #Le pasamos el objeto Tweet instanciado.

	def insertTweet(self, TweetInput, idC):
		Connector.insertTweet(TweetInput, idC)
	
	#Arregla el desastre de #-# y @-@
	def _campaignStringToList(self, c):
		c.hashtags = c.hashtags.split("-")
		c.mentions = c.mentions.split("-")
		return c
	
	#POR QUË NO LO HACE EL CONECTOR
	def _dbCampaignToCampaign(self, dbC):
		return Campaign(dbC.id, dbC.email, dbC.hashtags, dbC.mentions, dbC.startDate, dbC.finDate)
		
	#Comunicacion entre Fetcher y Manager. Cada campaña se codifica a json:
	def fetchCampaings(self):
		campaignsToFetch = self.returnCampaignsInProgress()
		for campaign in campaignsToFetch:
			c = self._campaignStringToList(self._dbCampaignToCampaign(campaign))
			jsonCampaign = c.to_json()
			url = "http://127.0.0.1:5001/fetcher"
			headers = {"Content-Type":"application/json"}			
			response = requests.get(url, json=jsonCampaign, headers=headers)
			self.insertTweets(response.json()["Tweets"],c.idC)