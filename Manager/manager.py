import json
from Campaign.Campaign import Campaign
from DataBaseConnector import configTables
from DataBaseConnector.Connector import Connector
from Tweet.Tweet import Tweet
import requests

class Manager():
	
	def __init__(self, context='standar'):
		
		if context == 'test':
			self.database = Connector(context='test')
		
		else:
			self.database = Connector()
	
	def insertCampaign(self, userInputs):
		stringHashtag = self.listaAString(userInputs["hashtags"]) # #donaldTrump-#G20
		stringMention = self.listaAString(userInputs["mentions"]) # @donaldTrump-@miauricioOK
		campaign = Campaign(1, userInputs["email"], stringHashtag, stringMention, userInputs["startDate"], userInputs["endDate"])
		return self.database.insertCampaign(campaign)

	def listaAString(self, lista):
		string = "-".join(lista)
		return string

	# Postman OK: 200 (1, multiples, mezclado, con y sin tweets), 404, 412 (1 y multiples)
	def deleteCampaignsByEmail(self, email_user):
		campaigns = self.database.selectCampaignsByEmail(email_user)

		if campaigns == []:	#No hubo campaigns con ese e-mail
			return 404

		haveDeleted = False		#flag
		for c in campaigns:
			if not c.isActive():
				self.database.deleteTweetsByIDC(c.idC)
				self.database.deleteCampaignByID(c.idC)
				haveDeleted = True

		if haveDeleted: #Borro una o mas campaigns
			return 200
		else:
			return 412	#No borro nada porque todas estaban activas

	# Postman OK: 200(con y sin tweets), 412, 404
	def deleteCampaignByID(self, idCampaign):
		#Se puede eliminar la campaña sólo si esta NO está iniciada:
		campaignRetornada = self.database.selectCampaign(idCampaign)

		if campaignRetornada == []: 
			return 404
		if campaignRetornada.isActive(): 
			return 412
		else: 
			self.database.deleteTweetsByIDC(idCampaign)
			self.database.deleteCampaignByID(idCampaign)
			return 200

	# Postman OK
	def returnCampaign(self, idCampaign):
		return self.database.selectCampaign(idCampaign)

	def returnCampaignsInProgress(self):
		return self.database.selectCampaignsInProgress()

	# Postman OK: 200,400,404,412
	def modifyCampaign(self, idCampaign, columna, inputUser):
		c = self.database.selectCampaign(idCampaign)
		if c == []:
			return 404		# No existe
		if c.isActive():	
			return 412		# Campaign activa
		# Existe y NO esta activa:
		wasModified = self.database.updateCampaign(idCampaign, columna, inputUser)
		if wasModified: 
			return 200	# OK
		return 400		# Columna inexistente
	
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