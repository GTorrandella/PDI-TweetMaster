import flask_sqlalchemy
from DataBaseConnector import configTables

def insertarCampaignBD(CampaignReceived):
	#Insertamos la campaña
	configTables.BD.metadata.create_all(configTables.engine) #Se crea la BD.
	#Insertamos fecha inicio, fecha fin, email dueño, hashtags y mentions en la tabla Campaign de la BD:
	new_campaignBD=configTables.Campaign(startDate=(CampaignReceived.get_start_date()), finDate=(CampaignReceived.get_fin_date()), email=(CampaignReceived.get_emailDueño()))
	configTables.session.add(new_campaignBD)

	#Insertamos los HashTags de la campaña (tabla HashTag de la BD):
	new_HashTagBD=configTables.HashTag()
	configTables.session.add(new_HashTagBD)

	#INsertamos las mentions de la campaña (tabla Mention de la BD):
	new_MentionBD=configTables.Mention()
	configTables.session.add(new_MentionBD)

	#Y finalmente las agregamos a la BD con estas 3 lineas:
	configTables.session.new
	configTables.session.dirty
	configTables.session.commit()

#def eliminarCampaignBD(Campaign):
#	print(Campaign.get_idC())

#def modificarCampaignBD(Campaign):
#	print(Campaign.get_idC())

def retornarCampaignBD(idCampaign):
	print("Campaña retornada:")
	print(session.query(Campaign).filter(Campaign.idCampaign).all())

"""def insertarTweets(TweetReceived):
	configTables.BD.metadata.create_all(configTables.engine) #Se crea la BD
	#Insertamos fecha publicacion, autor, mensaje y macheo en la tabla Tweet de la BD:
	new_TweetBD=configTables.Tweet(startDate=(TweetReceived.get_start_date()), finDate=(TweetReceived.get_fin_date()), email=(TweetReceived.get_emailDueño()), hashtags=(TweetReceived.get_hashtags()))
	configTables.session.add(new_TweetBD)

	#Y finalmente las agregamos a la BD con estas 3 lineas:
	configTables.session.new
	configTables.session.dirty
	configTables.session.commit()
"""