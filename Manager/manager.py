import configTables
import json
import Campaign.Campaign

#Fetcher a campaign le manda una lista de tweets. Y tenemos que resolverla. 
#Tarea juan:lo del json. Tarea mia: en la BD. en COnnector. 

def makeCampaign():
	#def makeCampaign(userInputs):
	#Me llegan los datos del form que completa el usuario, ver que llegan en un json:
    #fields = json.loads(userInputs) #De json a diccionario
	#c = Campaign(fields["idAutor"], fields["hashtags"], fields["mentions", fields["startDate", fields["finDate")
	# ^ (Usar los nombres de los campos correspondientes a los del json)
	#Llamar a un metodo en Acceso a BD para agregar 

    #Testeamos que se cree bien la campaña a partir del json recibido o solo testeamos
    #la parte de agregarla a la BD?
	#Con estos datos armo un objeto campaña
	campaign1=Campaign(1,"calongefederico@gmail.com", "Boca", "Carlitos" , "2018-11-30", "2018-11-20")
	#campaign2=Campaign(1,"gaby@gmail.com", "Carlitos" , "2018,11-30", "2018-11-20")
	
	#Este objeto se lo mandamos a Connector para ingresarlo en la BD.
	configTables.BD.metadata.create_all(configTables.engine) #Se crea la BD.
	new_campaignBD=configTables.Campaign(startDate=(campaign1.get_start_date()), finDate=(campaign1.get_fin_date()), email=(campaign1.get_emailDueño()))
	configTables.session.add(new_campaignBD)

	#new_hashTagBD = configTables.HashTag(campaign1.get_hastags(), campaign1.get_idC())
	#configTables.session.add(new_hashTagBD)

	#new_mencionBD = configTables.Mencion(campaign1.get_mentions(), campaign1.get_idC())
	#configTables.session.add(new_mencionBD)

	configTables.session.new
	configTables.session.dirty
	configTables.session.commit()



