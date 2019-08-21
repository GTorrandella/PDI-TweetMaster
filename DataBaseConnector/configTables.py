from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import relationship

#Este objeto va a contener la meta-informacion de nuestros mapeos:
BD = declarative_base()

class MySQLConfiguration():
    
    def __init__(self, context='standar'):
        if context=='test':
            #Es nuestra abstraccion de la base de datos:
            self.engine = create_engine("mysql+pymysql://root:4236@localhost:3306/BDTweetMaster?charset=utf8mb4",echo=True)
            if not database_exists(self.engine.url):
                create_database(self.engine.url)
        
        else:
            #Es nuestra abstraccion de la base de datos:
            self.engine = create_engine("mysql+pymysql://root:4236@mysqlTweetMaster:3306/BDTweetMaster?charset=utf8mb4",echo=True)
            if not database_exists(self.engine.url):
                create_database(self.engine.url)
        #Este objeto session va a ser nuestro contrato con el ORM, va a ser el objeto por el cual nos vamos a comunicar:
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        BD.metadata.create_all(self.engine)

class Campaign(BD):
    __tablename__ = 'campaign'
    
    id = Column(Integer, primary_key=True)
    startDate = Column(DateTime())
    finDate = Column(DateTime())
    email = Column(String(30))
    hashtags = Column(String(50))
    mentions = Column(String(50))
    tuits = relationship("Tweet",cascade="all, delete")
    
    def __repr__(self):
        return "<Campaign(idC='%s', startDate='%s', finDate='%s', email='%s', hashtags='%s', mentions='%s')>" % (self.id, self.startDate, self.finDate, self.email, self.hashtags, self.mentions)

class Tweet(BD):
    __tablename__ = 'tweets'
    
    ID = Column(String(50), primary_key=True)
    userName = Column(String(50))
    userid = Column(String(50))
    hashtags = Column(String(1500))
    mentions = Column(String(1500))
    date = Column(DateTime)
    idCampaign = Column(Integer, ForeignKey('campaign.id'))
    
    def __repr__(self):
        return "<Tweets(ID='%s', userName='%s',userid='%s',hashtags='%s',mentions='%s',date='%s',idCampaign='%s')>" % (self.ID, self.userName, self.userid, self.hashtags, self.mentions, self.date, self.idCampaign)

