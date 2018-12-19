import json
from Tweet.Tweet import Tweet as Tweet
from Campaign.Campaign import Campaign as Campaign
from datetime import date
from DataBaseConnector import Connector as Connector
import requests

class Manager():
	def insertCampaign(self, userInputs):
		#Con los nombres de los campos correspondientes a los del json que nos llegan armamos un objeto campaña.
		#Pero antes de esto como fields["hashtags"] y fields["mentions"] son LISTAS, tenemos que pasarlas a un string para poder añadirlo a la BD como un varchar: 
		stringHashtag = self.listaAString(userInputs["hashtags"]) # #donaldTrump-#G20
		stringMention = self.listaAString(userInputs["mentions"]) # @donaldTrump-@miauricioOK
	
		ObjetoCampaign = Campaign(1, userInputs["email"], stringHashtag, stringMention, userInputs["startDate"], userInputs["endDate"])
		print("manager.Manager().insertCampaign()")
		#Llamamos a un metodo de Connector para agregar la campaña a la BD junto con las mentions y los hashtags:
		return Connector.insertarCampaignBD(ObjetoCampaign)

	def listaAString(self, lista):
		string = "-".join(lista)
		return string
	
	def deleteCampaignporuser(self, email_user):
		#Hay que ver que la campaña NO haya iniciado (que la fecha de hoy sea anterior a la fecha de inicio).
		Connector.eliminarCampaignBDxUser(email_user)
	
	def deleteCampaignporid(self, idCampaign):
		#Hay que ver que la campaña NO haya iniciado (que la fecha de hoy sea anterior a la fecha de inicio).
		Connector.eliminarCampaignBDxID(idCampaign)
	
	def returnCampaign(self, idCampaign):
		#Hay que ver que la campaña HAYA TERMINADO (que la fecha se la fecha de fin)
		#Y hay que mandarla al Reporter.
		return Connector.retornarCampaignBD(idCampaign)
	
	def modifyCampaign(self, idCampaign, columna, inputUser):
		#Hay que ver que la campaña NO haya iniciado (que la fecha de hoy sea anterior a la fecha de inicio).
		Connector.modificarCampaignBD(idCampaign, columna, inputUser)	
	
	#exec(open("manager.py").read())
	#Fijarse en test_manager que sería este tweetsJson que recibe.
	def insertTweets(self, tweetsJson, idC):
		tweets = json.loads(tweetsJson)
		#Los separamos en tweets separados y llamamos a insertTweet para agregarlo uno por uno:
		for i in range(len(tweets)):
			t = Tweet(tweets[i])
			self.insertTweet(t,idC) #Le pasamos el objeto Tweet instanciado.

	def insertTweet(self, TweetInput, idC):
		Connector.insertTweet(TweetInput, idC)
	
	def fetchCampaings(self, campaignsToFetch):
		for idC in campaignsToFetch:
			jsonCampaign = {"Campaign":self.returnCampaign(idC).to_json()}
			url = "http://127.0.0.1:5001/fetcher"
			headers = {"Content-Type":"application/json"}			
			response = requests.get(url, json=jsonCampaign, headers=headers)
			self.insertTweets(response.json()["Tweets"],idC)
			
			
			
			
			
			
			
			
			
			
			
		