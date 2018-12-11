import sys
sys.path.append("..")
import json
from Campaign.Campaign import *
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

#El Fetcher le manda a Manager una lista de tweets para que únicamente lo inserte en la BD (en formato JSON llegaria):
#Gaby dijo que es una lista de diccionarios de la forma TweettoJson()
#EJemplo del objeto Tweet: en TweettoJson en la rama Fetcher (que es la versión final.), va a llegar 
#una lista de esos en el response. 
#Fecha según lo que devuelve TW es → “Sun Feb 25 17:11:02 +0000 2018”.

#def insertTweet(TweetInput):
#	ObjetoTweet=Tweet(VERESTEOBJETO)
#	Connector.insertTweet(TweetInput)

#def insertarTweets(TweetsInput):
	#La descomprimo en Tweets separados y llamo a insertTweet y lo agrego uno por uno.

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