import json
from Tweet.Tweet import Tweet as Tweet
from Campaign.Campaign import Campaign as Campaign
from DataBaseConnector import configTables 
from datetime import datetime
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
		#Se puede eliminar la campaña sólo si esta NO está iniciada (esta logica la aplicamos en 
		#eliminarCampaignBDxUser)
		Connector.eliminarCampaignBDxUser(email_user)

	def deleteCampaignporid(self, idCampaign):
		#Se puede eliminar la campaña sólo si esta NO está iniciada:
		campaignRetornada = Connector.retornarCampaignBD(idCampaign)
		fecha_inicio_campaign = campaignRetornada.startDate
		fecha_actual = datetime.now()
		#La campaña inició (fecha de inicio de campaign es MENOR a fecha actual), no hacemos nada:
		if (fecha_inicio_campaign < fecha_actual):
			print("La campaña ya inició")
		#La campaña NO inició, eliminamos la campaña:
		else:
			Connector.eliminarCampaignBDxID(idCampaign)
			print("Campaign eliminada")
			
	def returnCampaign(self, idCampaign):
		return Connector.retornarCampaignBD(idCampaign)
	
	def modifyCampaign(self, idCampaign, columna, inputUser):
		#Se puede modificar la campaña sólo si esta NO está iniciada:
		campaignRetornada = Connector.retornarCampaignBD(idCampaign)
		fecha_inicio_campaign = campaignRetornada.startDate
		fecha_actual = datetime.now()
		#La campaña inició (fecha de inicio de campaign es MENOR a fecha actual), no hacemos nada:
		if (fecha_inicio_campaign < fecha_actual):
			print("La campaña ya inició")
		#La campaña NO inició, modificamos la campaña:
		else:
			Connector.modificarCampaignBD(idCampaign, columna, inputUser) 
			print("Datos modificados")

	def returnCampaignsInProgress(self):
		#Obtenemos TODAS las Campañas y vemos una por una si la fecha de inicio de campaign es MENOR a
		#la fecha actual y la fecha de fin de la campaña es MAYOR a la fecha actual. Y si sucede esto la agregamos a una nueva lista.
		listaCampaigns = configTables.session.query(configTables.Campaign).all()
		print (listaCampaigns)
		listaNuevaCampaigns=[]
		for c in listaCampaigns:
			#Cada c es un: <Campaign(idC='1', startDate='28 11 2018 18:02:00', finDate='02 12 2018 19:26:22', email='test@gmail.com', hashtags='#test-#mock', mentions='@testCampaign-@mockOK')>
			#Y accedo a los atributos con c.atributo (el atributo está en la tabla Campaign dentro de configTables), osea asi: print (c.id)
			idCampaign = c.id
			print (idCampaign)
			campaignRetornada = Connector.retornarCampaignBD(idCampaign)
			fecha_inicio_campaign = campaignRetornada.startDate
			fecha_fin_campaign = campaignRetornada.finDate
			fecha_actual=datetime.now()
			if ((fecha_inicio_campaign < fecha_actual) and (fecha_fin_campaign > fecha_actual)):  #La campaña está en curso. Agrego la campaña a la nueva lista a devolver.
				listaNuevaCampaigns.append(c)
			else:  #Si la campaña no inició no hago nada. 
				print ("Campaña no iniciada")

		return (listaNuevaCampaigns) #Devolvemos la lista de campañas en curso (que todavía no finalizaron)
		#[<Campaign(idC='15', startDate='28 11 2018 18:02:00', finDate='25 12 2018 19:26:22', email='test@gmail.com', hashtags='#test-#mock', mentions='@testCampaign-@mockOK')>, 
		#<Campaign(idC='16', startDate='28 11 2018 18:02:00', finDate='25 12 2018 19:26:22', email='test@gmail.com', hashtags='#test-#mock', mentions='@testCampaign-@mockOK')>]

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
			
			
			
			
			
			
			
			
			
			
			
		