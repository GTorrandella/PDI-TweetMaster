import sys
sys.path.append("..")
import json
from Campaign.Campaign import *
from datetime import date
from DataBaseConnector import *
#Antes: 
#import configTables
#from Campaign import Campaign.Campaign

#Fetcher a campaign le manda una lista de tweets. Y tenemos que resolverla. 
#Tarea juan:lo del json. Y hacer test para que se cree bien la campaña a partir del json recibido.
#Tarea fede: Guardar en la BD y TESTEAR esto. Para esto ver la clase DBConnector. 
#Fecha según lo que devuelve TW es → “Sun Feb 25 17:11:02 +0000 2018”.
userInputs= '{"email":"donaldTrump@worlddomination.com","hashtags": ["#donaldTrump", "#G20"], "mentions": ["@donaldTrump", "@miauricioOK"], "sDate":"28-11-2018", "eDate":"02-12-2018"}'

def makeCampaign(userInputs):
	fields = json.loads(userInputs) #De json a diccionario
	startDate = StringToIntArray(fields["sDate"])
	endDate = StringToIntArray(fields["eDate"])
	
	#Con los nombres de los campos correspondientes a los del json que nos llegan armamos un objeto campaña:
	ObjetoCampaign = Campaign(1, fields["email"], fields["hashtags"], fields["mentions"], startDate, endDate)

	return ObjetoCampaign

	#Llamamos a un metodo de Connector para agregar la campaña a la BD:
	#Connector.insertarCampaignBD(ObjetoCampaign)

#Para probar el ingreso a BD:
"""def makeCampaign():
	ObjetoCampaign2=Campaign(1,"calongefederico@gmail.com", "Boca", "Carlitos" , "28-11-2018", "28-12-2018")
	Connector.insertarCampaignBD(ObjetoCampaign2)"""


def deleteCampaign(InputNombreCampaña):
	Connector.eliminarCampaignBD(InputNombreCampaña)

def StringToIntArray(str_date):
	#Arrays con las fechas de inicio y fin de la campania. Formato de la fecha en "fields": dd-mm-yyyy
	date_array=[]
	date_array.append(int(str_date[6:10])) 		#Año
	date_array.append(int(str_date[3:5]))		#Mes
	date_array.append(int(str_date[0:2]))		#Dia
	return date_array