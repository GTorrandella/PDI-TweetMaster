import unittest
from Tweet.Tweet import Tweet 
from Campaign.Campaign import Campaign
from datetime import datetime
from DataBaseConnector import Connector
from Manager import manager
import json

class test_manager(unittest.TestCase):
    #Testeamos que los tweets que llegan se agregen correctamente a la BD.
    def test_InsertTweets(self):
        #Precondición: deben haber 3 campañas creadas e insertadas en la BD.
        userInputs= '{"email":"test@gmail.com","hashtags": ["#test", "#mock"], "mentions": ["@testCampaign", "@mockOK"], "startDate":"28 11 2018 18:02:00", "endDate":"02 12 2018 19:26:22"}'
        fields = json.loads(userInputs) #Pasa de json a diccionario, esto lo hace flask por eso no hace falta hacerlo en el insertCampaign() del manager.
        idCampaign=manager.Manager().insertCampaign(fields)
        idCampaign=manager.Manager().insertCampaign(fields)
        idCampaign=manager.Manager().insertCampaign(fields)

        #Ejemplo de los lista de diccionario de tweets en formato JSON que el Fetcher le manda a Manager (tweetsJson).
        self.tweet1 = {
            "id_str" : "123456",
            "user" : {"name" : "NASAOk", "id_str" : "789456"},
            "entities" : {"hashtags" : ["#mars","#venus","#earth"],"user_mentions" : ["@NASA", "@planets"]},
            "created_at" : "Sun Mar 20 15:11:01 +0000 2018",
        }
        self.tweet2 = {
            "id_str" : "112112",
            "user" : {"name" : "MiauricioOK", "id_str" : "451325"},
            "entities" : {"hashtags" : ["#DonaldNoMeDejes"], "user_mentions" : ["@donaldTrump", "@G20"]},
            "created_at" : "Sun Mar 20 21:08:01 +0000 2018",
        }
        tweetsJson = json.dumps([self.tweet1,self.tweet2])
        #Insertamos un tweet con ID campaign 3.
        manager.Manager().insertTweets(tweetsJson, 3)
        #Obtengo el 2do Tweet:
        tweetEspecificoRetornado = Connector.returnTweetByIDT("112112")
        #Asserto los datos del 2do Tweet:
        assert tweetEspecificoRetornado.ID == 112112
        assert tweetEspecificoRetornado.userName == "MiauricioOK"
        assert tweetEspecificoRetornado.userid ==  "451325"
        assert tweetEspecificoRetornado.hashtags ==  "#DonaldNoMeDejes"
        assert tweetEspecificoRetornado.mentions == "@donaldTrump-@G20"
        assert tweetEspecificoRetornado.date == "2018-03-20 21:08:01"

    #Testeamos que se cree la campaña correctamente en la BD y que sea retornada sin modificaciones.
    def test_InsertCampaign(self):
        #Entrada de ejemplo, lo que el usuario ingresa en la Interfaz Web en Alta Campaña (en formato JSON llegaria):
        userInputs= '{"email":"test@gmail.com","hashtags": ["#test", "#mock"], "mentions": ["@testCampaign", "@mockOK"], "startDate":"28 11 2018 18:02:00", "endDate":"02 12 2018 19:26:22"}'
        fields = json.loads(userInputs) #Pasa de json a diccionario, esto lo hace flask por eso no hace falta hacerlo en el insertCampaign() del manager.
        idCampaign=manager.Manager().insertCampaign(fields)
        campaignEspecificaRetornada = Connector.retornarCampaignBD(idCampaign)

        #Asserto todos los atributos del objeto Campaign:
        assert (campaignEspecificaRetornada.emailDueño) == "test@gmail.com"
        assert campaignEspecificaRetornada.hashtags == "#test-#mock"
        assert campaignEspecificaRetornada.mentions == "@testCampaign-@mockOK"
        assert campaignEspecificaRetornada.startDate == datetime(2018, 11, 28, 18, 2)
        assert campaignEspecificaRetornada.finDate == datetime(2018, 12, 2, 19, 26, 22)

    #Pruebas de metodos:
    def test_ReturnCampaignBD(self):
        #Le pasamos la ID de Campaign 2
        objetoCampaign = Connector.retornarCampaignBD(2)
        print (objetoCampaign)
        #Imprime esto:
        # <idC:2 emailDueño:test@gmail.com hashtags:#test-#mock mentions:@testCampaign-@mockOK startDate:2018-11-28 18:02:00 finDate:2018-12-02 19:26:22> 

    def test_ReturnTweetsByIDC(self):
        #Retornamos los tuits con IDC 3 (de la 3ra campaña)
        tweets = Connector.returnTweetsByIDC(3)
        print(tweets)
        #Esto me devuelve, una lista de diccionarios tweets. La clave es tweetN y el valor es otro diccionario con los atributos del tweet:
        #{'tweet0': [{'id_str': 112112, 'user': {'name': 'MiauricioOK', 'id_str': '451325'}, 'entities': {'hashtags': '#DonaldNoMeDejes',
        # 'user_mentions': '@donaldTrump-@G20'}, 'created_at': '2018-03-20 21:08:01'}], 
        #'tweet1': [{'id_str': 123456, 'user': {'name': 'NASAOk', 'id_str': '789456'}, 'entities': {'hashtags': '#mars-#venus-#earth', 
        #'user_mentions': '@NASA-@planets'}, 'created_at': '2018-03-20 15:11:01'}]}