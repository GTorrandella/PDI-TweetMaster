import json
from Tweet.Tweet import Tweet as Tweet
from Campaign.Campaign import Campaign as Campaign
from datetime import date
from DataBaseConnector import Connector as Connector
import urllib.request

class Manager():
	def insertCampaign(self, userInputs):
		#Con los nombres de los campos correspondientes a los del json que nos llegan armamos un objeto campaña.
		#Pero antes de esto como fields["hashtags"] y fields["mentions"] son LISTAS, tenemos que pasarlas a un string para poder añadirlo a la BD como un varchar: 
		stringHashtag = self.listaAString(userInputs["hashtags"]) # #donaldTrump-#G20
		stringMention = self.listaAString(userInputs["mentions"]) # @donaldTrump-@miauricioOK
	
		ObjetoCampaign = Campaign(1, userInputs["email"], stringHashtag, stringMention, userInputs["startDate"], userInputs["endDate"])
		
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

	#Fijarse en test_manager que sería este tweetsJson que recibe.
	def insertTweets(self, tweetsJson, idC):
		tweets = json.loads(tweetsJson)
		#Los separamos en tweets separados y llamamos a insertTweet para agregarlo uno por uno:
		for i in range(len(tweets)):
			t = Tweet(tweets[i])
			self.insertTweet(t,idC) #Le pasamos el objeto Tweet instanciado.

	def insertTweet(self, TweetInput, idC):
		Connector.insertTweet(TweetInput, idC)
	
	#Comunicacion entre Fetcher y Manager. Cada campaña se codifica a json:
	def fetchCampaings(self, campaignsToFetch):
		for idC in campaignsToFetch:
			camp = self.returnCampaign(idC).to_json()
			request = urllib.request.Request("locahost/fetcher", data = camp, method = 'GET')
			request.add_header("Content-Type", "application/json")
			response = urllib.request.urlopen(request)
			self.insertTweets((str(response.read()).split(',')),(idC))
			
			
			
			
			
			
			
			
			
			
			
		