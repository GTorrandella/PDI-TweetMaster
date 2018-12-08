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
	startDate = Column(String(10))
	finDate = Column(String(10))
	email = Column(String(40))
    # hook = Column(String(10))

	def __repr__(self):
   	    return "<Campaign(startDate='%s', finDate='%s', email='%s')>" % (self.startDate, self.finDate, self.email)

class HashTag(BD):
	__tablename__ = 'hashTag'
	
	idH = Column(Integer, primary_key=True)
	hashtag = Column(String(10))
	idCampaign = Column(Integer, ForeignKey('campaign.idC'))
	
	def __repr__(self):
		return "<HashTag(hashtag='%s', idCampaign='%s')>" % (self.hashtag, self.idCampaign)

class Mencion(BD):
	__tablename__ = 'mencion'
	
	idU = Column(Integer, primary_key=True)
	user_mencion = Column(String(10))
	idCampaign = Column(Integer, ForeignKey('campaign.idC'))
	
	def __repr__(self):
		return "<Mencion(user_mencion='%s', idCampaign='%s')>" % (self.usuario, self.idCampaign)





