from datetime import date
import json
import sys
import unittest
from Campaign.Campaign import *
from Tweet.Tweet import *
from datetime import date
from DataBaseConnector.Connector
from Manager import manager

#Testeamos que los tweets que llegan se agregen correctamente a la BD.
#import test_manager
#test_manager.testinsertTweets()
def testinsertTweets():
    #Ejemplo de los lista de diccionario de tweets en formato JSON que el Fetcher le manda a Manager (tweetsJson). 
    tweet1 = {
        "id_str" : "123456",
        "user" : {"name" : "NASAOk", "id_str" : "789456"},
        "entities" : {"hashtags" : ["#mars","#venus","#earth"],"user_mentions" : ["@NASA", "@planets"]},
        "created_at" : "Sun Mar 20 15:11:01 +0000 2018",
    }
    tweet2 = {
        "id_str" : "112112",
        "user" : {"name" : "MiauricioOK", "id_str" : "451325"},
        "entities" : {"hashtags" : ["#DonaldNoMeDejes"], "user_mentions" : ["@donaldTrump", "@G20"]},
        "created_at" : "Sun Mar 20 21:08:01 +0000 2018",
    }

    tweetsJson = json.dumps([tweet1,tweet2])
    #INsertamos un tweet con ID campaign 2.
    manager.Manager().insertTweets(tweetsJson, 2)
    #Obtengo el 2do Tweet:
    tweetEspecificoRetornado = Connector.returnTweetByIDT("112112")
    #Asserto los datos del 2do Tweet:
    #print(tweetEspecificoRetornado.ID)
    #assert tweetEspecificoRetornado.ID == 112112
    #assert tweetEspecificoRetornado.userName == "MiauricioOK"
    #assert tweetEspecificoRetornado.userid ==  "451325"
    #assert tweetEspecificoRetornado.hashtags ==  "#DonaldNoMeDejes"
    #assert tweetEspecificoRetornado.mentions == "@donaldTrump-@G20"
    #assert tweetEspecificoRetornado.date == "2018-03-20 21:08:01"

#Testeamos que se cree la campaña correctamente en la BD y que sea retornada sin modificaciones.
#import test_manager
#test_manager.testInsertCampaign()
def testInsertCampaign():
    #Entrada de ejemplo, lo que el usuario ingresa en la Interfaz Web en Alta Campaña (en formato JSON llegaria):
    userInputs= '{"email":"test@gmail.com","hashtags": ["#test", "#mock"], "mentions": ["@testCampaign", "@mockOK"], "startDate":"28 11 2018 18:02:00", "endDate":"02 12 2018 19:26:22"}'
    fields = json.loads(userInputs) #Pasa de json a diccionario, esto lo hace flask por eso no hace falta hacerlo en el insertCampaign() del manager. 
    idCampaign=manager.Manager().insertCampaign(fields)
    #Obtengo la campaña por nombre de email:
    #campaignEspecifica = configTables.session.query(configTables.Campaign).filter_by(email="test@gmail.com").first()
    campaignEspecificaRetornada = Connector.retornarCampaignBD(idCampaign)
    #print (campaignEspecificaRetornada.email)
    #print (campaignEspecificaRetornada.id)
    #assert campaignEspecificaRetornada.email == "test@gmail.com"
    #assert campaignEspecificaRetornada.hashtags == "#test-#mock"
    #assert campaignEspecificaRetornada.mentions == "@testCampaign-@mockOK"
    #<assert campaignEspecificaRetornada.startDate == "2018-11-28 18:02:00"
    #assert campaignEspecificaRetornada.endDate == "2018-12-02 19:26:22"
    #manager.returnCampaign(campaignEspecifica.id)

def testReturnCampaignBD():
    #Le pasamos la ID de Campaign 2
    Connector.retornarCampaignBD(2)

def testReturnTweetsByIDC():
    #Retornamos los tuits con IDC 2 (de la 2da campaña)
    Connector.returnTweetsByIDC(2)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()