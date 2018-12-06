import sys
sys.path.append("..")
import json
from Campaign import *
from datetime import date
from DataBaseConnector import *
#Antes: 
#import configTables
#from Campaign import Campaign.Campaign

#Fetcher a campaign le manda una lista de tweets. Y tenemos que resolverla. 
#Tarea juan:lo del json. Y hacer test para que se cree bien la campaña a partir del json recibido.
#Tarea fede: Guardar en la BD y TESTEAR esto. Para esto ver la clase DBConnector. 
#Fecha según lo que devuelve TW es → “Sun Feb 25 17:11:02 +0000 2018”.
userInputs= '{"email":"donaldTrump@worlddomination.com","hashtags": "#donaldTrump", "mentions": "@donaldTrump", "sDate":"28-11-2018", "eDate":"02-12-2018"}'

def hola(numero):
	numero=numero+1
	print (numero)


def makeCampaign(userInputs):
	fields = json.loads(userInputs) #De json a diccionario

	#Arrays con las fechas de inicio y fin de la campania. Formato de la fecha en "fields": dd-mm-yyyy
	startDate=[]
	endDate=[]
	startDate.append(int(fields["sDate"][6:10])) 
	startDate.append(int(fields["sDate"][3:5]))
	startDate.append(int(fields["sDate"][0:2]))
	endDate.append(int(fields["eDate"][6:10]))
	endDate.append(int(fields["eDate"][3:5]))
	endDate.append(int(fields["eDate"][0:2]))
	
	#Con los nombres de los campos correspondientes a los del json que nos llegan armamos un objeto campaña:
	ObjetoCampaign = Campaign(1, fields["email"], fields["hashtags"], fields["mentions"], startDate, endDate)
	#Ejemplo de un objeto campaign: 
	#campaign1=Campaign(1,"calongefederico@gmail.com", "Boca", "Carlitos" , "2018-11-30", "2018-11-20")
	
	print (ObjetoCampaign)
	print(c.get_start_date()) 
	print(c.get_fin_date())

	#Llamamos a un metodo de Connector para agregar la campaña a la BD:
	Connector.insertarCampaignBD(ObjetoCampaign)


#Para probar el ingreso a BD:
def makeCampaign():
	ObjetoCampaign=Campaign(1,"calongefederico@gmail.com", "Boca", "Carlitos" , "2018-11-30", "2018-11-20")
	Connector.insertarCampaignBD(ObjetoCampaign)

def deleteCampaign(InputNombreCampaña):
	Connector.eliminarCampaignBD(InputNombreCampaña)

	


