import sys
sys.path.append("..")
import json
from Campaign import Campaign
from Tweet.Tweet import *
from datetime import date
from DataBaseConnector import Connector

#Lo que el usuario ingresa en la Interfaz Web en Alta Campaña (en formato JSON llegaria):
userInputs= '{"email":"donaldTrump@gmail.com","hashtags": ["#donaldTrump", "#G20"], "mentions": ["@donaldTrump", "@miauricioOK"], "sDate":"28-11-2018", "eDate":"02-12-2018"}'

def insertCampaign(userInputs):
	fields = json.loads(userInputs) #De json a diccionario
	startDate = StringToIntArray(fields["sDate"])
	endDate = StringToIntArray(fields["eDate"])
	
	#Con los nombres de los campos correspondientes a los del json que nos llegan armamos un objeto campaña.
	#Pero antes de esto como fields["hashtags"] y fields["mentions"] son LISTAS, tenemos que pasarlas a un string para poder añadirlo a la BD como un varchar: 
	stringHashtag = listaAString(fields["hashtags"]) # #donaldTrump - #G20
	stringMention = listaAString(fields["mentions"]) # @donaldTrump - @miauricioOK

	ObjetoCampaign = Campaign(1, fields["email"], stringHashtag, stringMention, startDate, endDate)
	
	print("Strings:")
	print(stringHashtag)
	print(stringMention)

	print("Objeto Campaign:")
	print(ObjetoCampaign)
	
	#Llamamos a un metodo de Connector para agregar la campaña a la BD junto con las mentions y los hashtags:
	Connector.insertarCampaignBD(ObjetoCampaign)

def deleteCampaignporuser(email_user):
	#Hay que ver que la campaña NO haya iniciado (que la fecha de hoy sea anterior a la fecha de inicio).
	Connector.eliminarCampaignBDxUser(email_user)

def deleteCampaignporid(idCampaign):
	#Hay que ver que la campaña NO haya iniciado (que la fecha de hoy sea anterior a la fecha de inicio).
	Connector.eliminarCampaignBDxID(idCampaign)

def returnCampaign(idCampaign):
	#Hay que ver que la campaña HAYA TERMINADO (que la fecha se la fecha de fin)
	#Y hay que mandarla al Reporter.
	Connector.retornarCampaignBD(idCampaign)

def modifyCampaign(idCampaign, columna, inputUser):
	#Hay que ver que la campaña NO haya iniciado (que la fecha de hoy sea anterior a la fecha de inicio).
	Connector.modificarCampaignBD(idCampaign, columna, inputUser)

#Ejemplo de los lista de diccionario de tweets en formato JSON que el Fetcher le manda a Manager (tweetsJson). 
tweet1 = {
	"id": "789456",
	"userID": "123456",
	"userName": "NASAOk",
	"email": "lanasaoficialamigonofeik@algo.com",
	"hashtags": ["mars","venus","earth"],
	"mentions": ["NASA", "planets"]
}
tweet2 = {
	"id": "98976",
	"userID": "61558",
	"userName": "miauricioOK",
	"email": "macri@whiskas.cat",
	"hashtags": ["DonaldVolveNoMeDejes"],
	"mentions": ["donaldTrump", "(?"],
	"date": "Sun Mar 20 15:11:01 2018"
}

tweetsJson = json.dumps([tweet1,tweet2])	

def insertTweets(tweetsJson):
	tweets = json.loads(tweetsJson)
	#Los separamos en tweets separados y llamamos a insertTweet para agregarlo uno por uno:
	for tuit in tweets:
		insertTweet(tuit)

def insertTweet(TweetInput):
	Connector.insertTweet(TweetInput)

def StringToIntArray(str_date):
	#Arrays con las fechas de inicio y fin de la campania. Formato de la fecha en "fields": dd-mm-yyyy
	date_array=[]
	date_array.append(int(str_date[6:10])) 		#Año
	date_array.append(int(str_date[3:5]))		#Mes
	date_array.append(int(str_date[0:2]))		#Dia
	return date_array

def listaAString(lista):
	string = "-".join(lista)
	return string