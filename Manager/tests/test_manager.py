from datetime import date
import json
import sys
import unittest
from Campaign.Campaign import *
from Tweet.Tweet import *
from datetime import date
from DataBaseConnector import Connector, configTables
import manager

sys.path.append("..")

#Testeamos que los tweets que llegan se agregen correctamente a la BD.
#import test_manager
#test_manager.testinsertTweets()
def testinsertTweets():
    #Ejemplo de los lista de diccionario de tweets en formato JSON que el Fetcher le manda a Manager (tweetsJson). 
    tweet1 = {
        "id_str" : "123456",
        "user" : {"name" : "NASAOk", "id_str" : "789456"},
        "entities" : {"hashtags" : ["#mars","#venus","#earth"],"mentions" : ["@NASA", "@planets"]},
        "created_at" : "Sun Mar 20 15:11:01 +0000 2018",
    }
    tweet2 = {
        "id_str" : "112112",
        "user" : {"name" : "MiauricioOK", "id_str" : "451325"},
        "entities" : {"hashtags" : ["#DonaldNoMeDejes"], "mentions" : ["@donaldTrump", "@G20"]},
        "created_at" : "Sun Mar 20 21:08:01 +0000 2018",
    }

    tweetsJson = json.dumps([tweet1,tweet2])
    manager.Manager().insertTweets(tweetsJson)
    #Obtengo el 2do Tweet:
    tweetEspecificoRetornado = Connector.returnTweetByIDT("112112")
    #Asserto los datos del 2do Tweet:
    #print(tweetEspecificoRetornado.ID)
    assert tweetEspecificoRetornado.ID == 112112
    assert tweetEspecificoRetornado.userName == "MiauricioOK"
    assert tweetEspecificoRetornado.userid ==  "451325"
    assert tweetEspecificoRetornado.hashtags ==  "#DonaldNoMeDejes"
    assert tweetEspecificoRetornado.mentions == "@donaldTrump-@G20"
    assert tweetEspecificoRetornado.date == "2018-03-20 21:08:01"

#Testeamos que se cree la campaña correctamente en la BD y que sea retornada sin modificaciones.
#import test_manager
#test_manager.testInsertCampaign()
def testInsertCampaign():
    #Entrada de ejemplo, lo que el usuario ingresa en la Interfaz Web en Alta Campaña (en formato JSON llegaria):
    userInputs= '{"email":"test@gmail.com","hashtags": ["#test", "#mock"], "mentions": ["@testCampaign", "@mockOK"], "startDate":"28 11 2018 18:02:00", "endDate":"02 12 2018 19:26:22"}'
    idCampaign=manager.Manager().insertCampaign(userInputs)
    #Obtengo la campaña por nombre de email:
    #campaignEspecifica = configTables.session.query(configTables.Campaign).filter_by(email="test@gmail.com").first()
    campaignEspecificaRetornada = Connector.retornarCampaignBD(idCampaign)
    #print (campaignEspecificaRetornada.email)
    #print (campaignEspecificaRetornada.id)
    assert campaignEspecificaRetornada.email == "test@gmail.com"
    assert campaignEspecificaRetornada.hashtags == "#test-#mock"
    assert campaignEspecificaRetornada.mentions == "@testCampaign-@mockOK"
    assert campaignEspecificaRetornada.startDate == "2018-11-28 18:02:00"
    assert campaignEspecificaRetornada.endDate == "2018-12-02 19:26:22"
    manager.returnCampaign(campaignEspecifica.id)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()