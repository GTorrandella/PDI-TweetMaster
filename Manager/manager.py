#import configTables
import sys
sys.path.append("..")
import json
import Campaign

#Fetcher a campaign le manda una lista de tweets. Y tenemos que resolverla. 
#Tarea juan:lo del json. Tarea mia: en la BD. en COnnector. 
userInputs= '{"email":"donaldTrump@worlddomination.com","hashtags": "#donaldTrump", "mentions": "@donaldTrump", "sDate":"28-11-2018", "eDate":"02-12-2018"}'
def makeCampaign(userInputs):

	fields = json.loads(userInputs) #De json a diccionario
	#c = Campaign(idC=None, fields["email"], fields["hashtags"], fields["mentions"], fields["sDate"], fields["eDate"])
	# ^ (Usar los nombres de los campos correspondientes a los del json)
	
	#Llamar a un metodo en Acceso a BD para agregar 

    #Testeamos que se cree bien la campaña a partir del json recibido o solo testeamos
    #la parte de agregarla a la BD?
	#Con estos datos armo un objeto campaña
	#campaign1=Campaign(1,"calongefederico@gmail.com", "Boca", "Carlitos" , "2018-11-30", "2018-11-20")
	#campaign2=Campaign(1,"gaby@gmail.com", "Carlitos" , "2018,11-30", "2018-11-20")
	
	#Este objeto se lo mandamos a Connector para ingresarlo en la BD.
	'''configTables.BD.metadata.create_all(configTables.engine) #Se crea la BD.
	new_campaignBD=configTables.Campaign(startDate=(campaign1.get_start_date()), finDate=(campaign1.get_fin_date()), email=(campaign1.get_emailDueño()))
	configTables.session.add(new_campaignBD)

	#new_hashTagBD = configTables.HashTag(campaign1.get_hastags(), campaign1.get_idC())
	#configTables.session.add(new_hashTagBD)

	#new_mencionBD = configTables.Mencion(campaign1.get_mentions(), campaign1.get_idC())
	#configTables.session.add(new_mencionBD)

	configTables.session.new
	configTables.session.dirty
	configTables.session.commit()'''



