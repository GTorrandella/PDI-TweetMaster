from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import relationship

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

	id = Column(Integer, primary_key=True)
	startDate = Column(String(10))
	finDate = Column(String(10))
	email = Column(String(40))
	hashtags = Column(String(40))
	mentions = Column(String(40))
    # hook = Column(String(10))

	def __repr__(self):
   	    return "<Campaign(idC='%s', startDate='%s', finDate='%s', email='%s', hashtags='%s', mentions='%s')>" % (self.id, self.startDate, self.finDate, self.email, self.hashtags, self.mentions)

class Tweets(BD):
	__tablename__ = 'tweets'
	
	id = Column(Integer, primary_key=True)
	fechaPublicacion = Column(String(50))
	autor=Column(String(10))
	mensaje=Column(String(10))
	macheo=Column(String(10))

	def __repr__(self):
		return "<Tweets(idT='%s', fechaPublicacion='%s',autor='%s',mensaje='%s',macheo='%s')>" % (self.idT, self.fechaPublicacion, self.autor, self.mensaje, self.macheo)






