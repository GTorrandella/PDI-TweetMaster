import sys
sys.path.append("..")
import json
from Campaign.Campaign import *
from Tweet.Tweet import *
from datetime import date
from DataBaseConnector import Connector

#Fecha según lo que devuelve TW es → “Sun Feb 25 17:11:02 +0000 2018”.
#Lo que el usuario ingresa en la Interfaz Web (en formato JSON llegaria):
userInputs= '{"email":"donaldTrump@gmail.com","hashtags": ["#donaldTrump", "#G20"], "mentions": ["@donaldTrump", "@miauricioOK"], "sDate":"28-11-2018", "eDate":"02-12-2018"}'
#Lo que el Fetcher le manda a manager (lista de tweets) para que manager solo la inserte en la BD (en formato JSON llegaria):
#Gaby dijo que es una lista de diccionarios de la forma TweettoJson()
#EJemplo del objeto Tweet: en TweettoJson en la rama Fetcher (que es la versión final.), va a llegar 
#una lista de esos ene l response. 

#manager.insertCampaign('{"email":"donaldTrump@gmail.com","hashtags": ["#donaldTrump", "#G20"], "mentions": ["@donaldTrump", "@miauricioOK"], "sDate":"28-11-2018", "eDate":"02-12-2018"}')
def insertCampaign(userInputs):
	fields = json.loads(userInputs) #De json a diccionario
	startDate = StringToIntArray(fields["sDate"])
	endDate = StringToIntArray(fields["eDate"])
	
	#Con los nombres de los campos correspondientes a los del json que nos llegan armamos un objeto campaña:
	ObjetoCampaign = Campaign(1, fields["email"], fields["hashtags"], fields["mentions"], startDate, endDate)
	#Arriba hay que sacar el 1 y que sea autoincrement (VER COMO). Creo que ni usa el 1 igual. 

	print("Objeto Campaign:")
	print(ObjetoCampaign)

	#Llamamos a un metodo de Connector para agregar la campaña a la BD junto con las mentions y los hashtags:
	#Connector.insertarCampaignBD(ObjetoCampaign)
	#Connector.insertarHashTagsBD(ObjetoCampaign)
	#Connector.insertarMentionsBD(ObjetoCampaign)

def modifyCampaign(ObjetoCampaign):
	#Hay que ver lo de la fecha que no supere la fecha de hoy.
	Connector.modificarCampaignBD(ObjetoCampaign)

def deleteCampaign(ObjetoCampaign):
	Connector.eliminarCampaignBD(ObjetoCampaign)

def returnCampaign(idCampaign):
	retornarCampaignBD(idCampaign)

#def insertTweet(TweetInput):
#	ObjetoTweet=Tweet(1,"calongefederico@gmail.com", "Boca", "Carlitos" , "28-11-2018", "28-12-2018")
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