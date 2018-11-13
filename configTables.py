from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

#Es nuestra abstraccion de la base de datos:
engine = create_engine("mysql+pymysql://root:4236@localhost:3306/BDTweetMaster", echo=True)
if not database_exists(engine.url):
    create_database(engine.url)
#Este objeto va a contener la meta-informacion de nuestros mapeos:
BD = declarative_base()
#Este objeto session va a ser nuestro contrato con el ORM, va a ser el objeto por el cual nos vamos a comunicar:
Session = sessionmaker(bind=engine)
session = Session()

class Campaign(BD):
	__tablename__ = 'campaign'

	idC = Column(Integer, primary_key=True)
	fechaInicio = Column(String(10))
	fechaFin = Column(String(10))
	email = Column(String(30))
    # hook = Column(String(10))

	def __repr__(self):
   	    return "<Campaign(fechaInicio='%s', fechaFin='%s', email='%s')>" % (self.fechaInicio, self.fechaFin, self.email)

class HashTag(BD):
	__tablename__ = 'hashTag'
	
	idH = Column(Integer, primary_key=True)
	hashtag = Column(String(10))
	idCampaign = Column(Integer, ForeignKey('campaign.idC'))
	
	def __repr__(self):
		return "<HashTag(hashtag='%s', idCampaign='%s')>" % (self.hashtag, self.idCampaign)

class User(BD):
	__tablename__ = 'user'
	
	idU = Column(Integer, primary_key=True)
	usuario = Column(String(10))
	idCampaign = Column(Integer, ForeignKey('campaign.idC'))
	
	def __repr__(self):
		return "<User(usuario='%s', idCampaign='%s')>" % (self.usuario, self.idCampaign)

#Creamos la BD desde la consola ejecutando:
#configTables.BD.metadata.create_all(configTables.engine)

#new_campaign = configTables.Campaign(fechaInicio='01/04/1996', fechaFin='01/04/2000', email='federicktailor@gmail.com')
#configTables.session.add(new_campaign)

#new_hashTag = configTables.HashTag(hashtag='#bocaXFox', idCampaign=1)
#configTables.session.add(new_hashTag)

#new_user = configTables.User(usuario='federicio', idCampaign=1)
#configTables.session.add(new_user)

#configTables.session.new
#configTables.session.dirty
#configTables.session.commit()





