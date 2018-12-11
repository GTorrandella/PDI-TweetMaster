import sys
sys.path.append("..")
import json
from Campaign.Campaign import *
from Tweet.Tweet import *
from datetime import date
from DataBaseConnector import Connector
import manager
from DataBaseConnector import configTables
import unittest

#Para probar el ingreso a BD:
#def makeCampaign():
	#ObjetoCampaign2=Campaign(1,"calongefederico@gmail.com", "Boca", "Carlitos" , "28-11-2018", "28-12-2018")
	#Connector.insertarCampaignBD(ObjetoCampaign2)

#Testeamos que se cree la campaña correctamente en la BD y que sea retornada sin modificaciones.
#test_manager.testInsertCampaign()
def testInsertCampaign():
    #Entrada de ejemplo:
    userInputs = '{"email":"test@gmail.com","hashtags": ["#test", "#mock"], "mentions": ["@testCampaign", "@mockOK"], "sDate":"28-11-2018", "eDate":"02-12-2018"}'
    manager.insertCampaign(userInputs)
    
    #Obtengo la campaña por nombre de email:
    campaignEspecifica = configTables.session.query(configTables.Campaign).filter_by(email="test@gmail.com").first()
    idC=campaignEspecifica.id
    campaignEspecificaRetornada = Connector.retornarCampaignBD(idC)
    print(campaignEspecificaRetornada)
    assert campaignEspecificaRetornada.email == "test@gmail.com"
    #assert campaignEspecificaRetornada.hashtags == "#test-#mock"
    #assert campaignEspecificaRetornada.mentions == "@testCampaign-@mockOK"
    #assert campaignEspecificaRetornada.startDate == "28-11-2018"
    #assert campaignEspecificaRetornada.endDate == "02-12-2018"
    #manager.returnCampaign(campaignEspecifica.id)
    #assert campaignEspecifica == 200
    #Despues eliminamos esa campaña y vemos si no está mas?

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()