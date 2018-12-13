import flask_sqlalchemy
import configTables

#Primero insertar si o si una campaig así se ejecuta la linea configTables.BD.metadata.create_all(configTables.engine) que crea la BD.
#manager.insertCampaign('{"email":"donaldTrump@gmail.com","hashtags": ["#donaldTrump", "#G20"], "mentions": ["@donaldTrump", "@miauricioOK"], "sDate":"28-11-2018", "eDate":"02-12-2018"}')
def insertarCampaignBD(CampaignReceived):
	#Insertamos la campaña
	configTables.BD.metadata.create_all(configTables.engine) #Se crea la BD (o no, dependiendo si se ejecutó antes).
	#Insertamos fecha inicio, fecha fin, email dueño, hashtags y mentions en la tabla Campaign de la BD:
	new_campaignBD=configTables.Campaign(startDate=(CampaignReceived.get_start_date()), finDate=(CampaignReceived.get_fin_date()), email=(CampaignReceived.get_emailDueño()), hashtags=(CampaignReceived.get_hashtags()), mentions=(CampaignReceived.get_mentions()))
	configTables.session.add(new_campaignBD)

	#Y finalmente las agregamos a la BD con estas 3 lineas:
	configTables.session.new
	configTables.session.dirty
	configTables.session.commit() #Para que los cambios se efectivicen en la BD
	return new_campaignBD.id

#manager.deleteCampaignporuser("donaldTrump@gmail.com")
def eliminarCampaignBDxUser(email_user):
	#Pueden ser 1 o mas campañas asociadas a un usuario, elimina TODAS:
	configTables.session.query(configTables.Campaign).filter_by(email=email_user).delete()
	configTables.session.commit()

#manager.deleteCampaignporid(1)
def eliminarCampaignBDxID(idC):
	campaignespecifica = configTables.session.query(configTables.Campaign).get(idC) #Obtengo al camaña con id especifico idC.
	configTables.session.delete(campaignespecifica)
	configTables.session.commit()

#manager.returnCampaign(1)
def retornarCampaignBD(idC):
	print("Campaña retornada:")
	campaignespecifica = configTables.session.query(configTables.Campaign).get(idC)
	return campaignespecifica
	#Que viaje en JSON, no como objeto. 
	#print(campaignespecifica.id, campaignespecifica.email, campaignespecifica.hashtags, campaignespecifica.mentions, campaignespecifica.startDate, campaignespecifica.finDate) 
    #Devuelve esto: 2 donaldTrump@gmail.com hasgtags mentions 2018-11-28 2018-12-02 --> con print envés de return se ve.

#manager.modifyCampaign(2, "email", "calonshi@gmail.com")
#Desde la Interfaz (en ModifCampaign) le llegaría al manager la columna a modificar, el campo para esa columna (inputUser) y el id de campaña.
def modificarCampaignBD(idC, inputColumn, inputUser):
	#Lenguaje MYSQL: UPDATE Campaign SET columna = "inputuser" WHERE id = "idC".
	campaignespecifica = configTables.session.query(configTables.Campaign).get(idC)
	#Hice esto de abajo porque no podía poner campaignespecifica.inputColumn = inputUser, no me toma inputColumn.
	if (inputColumn=="email"):
		campaignespecifica.email = inputUser
		configTables.session.commit()
	
	if (inputColumn=="startDate"):
		campaignespecifica.startDate = inputUser
		configTables.session.commit()
	
	if (inputColumn=="finDate"):
		campaignespecifica.finDate = inputUser
		configTables.session.commit()
	
	if (inputColumn=="hashtags"):
		campaignespecifica.hashtags = inputUser
		configTables.session.commit()
	
	if (inputColumn=="mentions"):
		campaignespecifica.mentions = inputUser
		configTables.session.commit()
	
	#print(campaignespecifica.id, campaignespecifica.email, campaignespecifica.hashtags, campaignespecifica.mentions, campaignespecifica.startDate, campaignespecifica.finDate) 

def insertTweet(TweetInput):
	configTables.BD.metadata.create_all(configTables.engine) #Se crea la BD
	#Insertamos fecha publicacion, autor, mensaje y macheo en la tabla Tweet de la BD:
	new_TweetBD=configTables.Tweet(ID=(TweetInput.ID), userName=(TweetInput.userName), userID=(TweetInput.userID), hashtags=(TweetInput.hashtags),mentions=(TweetInput.mentions), date=(TweetInput.date))
	configTables.session.add(new_TweetBD)

	#Y finalmente las agregamos a la BD con estas 3 lineas:
	configTables.session.new
	configTables.session.dirty
	configTables.session.commit()

#def retornarTweet(idT):