import sys
sys.path.append("..")
import json
<<<<<<< HEAD
from Campaign.Campaign import Campaign
from Tweet.Tweet import Tweet
from datetime import date
from DataBaseConnector import Connector
import urllib.request

=======
from Campaign import Campaign
from Tweet import Tweet
import Connector
import urllib.request

#Lo que el usuario ingresa en la Interfaz Web en Alta Campaña (en formato JSON llegaria):
#userInputs= '{"email":"donaldTrump@gmail.com","hashtags": ["#donaldTrump", "#G20"], "mentions": ["@donaldTrump", "@miauricioOK"], "startDate":"28 11 2018 18:02:00", "endDate":"02 12 2018 19:26:22"}'
>>>>>>> 136fb2ed907eca7e7c3029c9e7570502155e8b28
class Manager():
	def insertCampaign(self, userInputs):
		fields = userInputs
		#Con los nombres de los campos correspondientes a los del json que nos llegan armamos un objeto campaña.
		#Pero antes de esto como fields["hashtags"] y fields["mentions"] son LISTAS, tenemos que pasarlas a un string para poder añadirlo a la BD como un varchar: 
		stringHashtag = self.listaAString(fields["hashtags"]) # #donaldTrump-#G20
		stringMention = self.listaAString(fields["mentions"]) # @donaldTrump-@miauricioOK
	
		ObjetoCampaign = Campaign(1, fields["email"], stringHashtag, stringMention, fields["startDate"], fields["endDate"])
		
		#Llamamos a un metodo de Connector para agregar la campaña a la BD junto con las mentions y los hashtags:
		return Connector.insertarCampaignBD(ObjetoCampaign)
	
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
	def insertTweets(self, tweetsJson):
		tweets = json.loads(tweetsJson)
		#Los separamos en tweets separados y llamamos a insertTweet para agregarlo uno por uno:
		for i in range(len(tweets)):
			t = Tweet(tweets[i])
			self.insertTweet(t) #Le pasamos el objeto Tweet instanciado.

	def insertTweet(self, TweetInput):
		Connector.insertTweet(TweetInput)
	
	def listaAString(self, lista):
		string = "-".join(lista)
		return string
	
	def fetchCampaings(self, campaignsToFetch):
		for idC in campaignsToFetch:
			camp = self.returnCampaign(idC).to_json()
			request = urllib.request.Request("locahost/fetcher", data = camp, method = 'GET')
			request.add_header("Content-Type", "application/json")
			response = urllib.request.urlopen(request)
			self.insertTweets(str(response.read()).split(','))
			
			
			
			
			
			
			
			
			
			
			
		