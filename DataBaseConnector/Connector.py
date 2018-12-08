import flask_sqlalchemy
from DataBaseConnector import configTables

def insertarCampaignBD(CampaignReceived):
	configTables.BD.metadata.create_all(configTables.engine) #Se crea la BD.
	new_campaignBD=configTables.Campaign(startDate=(CampaignReceived.get_start_date()), finDate=(CampaignReceived.get_fin_date()), email=(CampaignReceived.get_emailDueño()))
	configTables.session.add(new_campaignBD)
	configTables.session.new
	configTables.session.dirty
	configTables.session.commit()

#def insertarHashtagBD(HashTag):
	#new_hashTagBD = configTables.HashTag(campaign1.get_hastags(), campaign1.get_idC())
	#configTables.session.add(new_hashTagBD)
	#configTables.session.new
	#configTables.session.dirty
	#configTables.session.commit()

#def insertarMencionBD(Mencion):
	#new_mencionBD = configTables.Mencion(campaign1.get_mentions(), campaign1.get_idC())
	#configTables.session.add(new_mencionBD)

#def eliminarCampaignBD(Campaign):

#def eliminarHashtagBD(HashTag):

#def eliminarMencionBD(Mencion):
	
	