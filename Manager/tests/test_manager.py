import unittest
from Tweet.Tweet import Tweet 
from Campaign.Campaign import Campaign
from datetime import datetime
from DataBaseConnector.Connector import Connector
from DataBaseConnector import configTables
from Manager.manager import Manager
from datetime import datetime
import json

class test_manager(unittest.TestCase):

    def setUp(self):
        self.manager = Manager(context='test')
        self.connector = Connector(context='test')

    def tearDown(self):
        self.manager.database.database.session.query(configTables.Tweet).delete()
        self.manager.database.database.session.query(configTables.Campaign).delete()
        self.manager.database.database.session.commit()

    #Testeamos que se cree la campaña correctamente en la BD y que sea retornada sin modificaciones.
    def test_InsertCampaign(self):
        #Entrada de ejemplo, lo que el usuario ingresa en la Interfaz Web en Alta Campaña (en formato JSON llegaria):
        userInputs = '{"email":"test@gmail.com","hashtags": ["#test", "#mock"], "mentions": ["@testCampaign", "@mockOK"], "startDate":"2018-11-28 18:02:00", "endDate":"2018-12-25 19:26:22"}'
        fields = json.loads(userInputs) #Pasa de json a diccionario, esto lo hace flask por eso no hace falta hacerlo en el insertCampaign() del manager.
        idCampaign = self.manager.insertCampaign(fields)
        campaignRetornada = self.connector.selectCampaign(idCampaign)

        #Asserto todos los atributos del objeto Campaign:
        self.assertEqual(campaignRetornada.emailDueño, "test@gmail.com")
        self.assertEqual(campaignRetornada.hashtags, "#test-#mock")
        self.assertEqual(campaignRetornada.mentions, "@testCampaign-@mockOK")
        self.assertEqual(campaignRetornada.startDate , datetime(2018, 11, 28, 18, 2))
        self.assertEqual(campaignRetornada.finDate , datetime(2018, 12, 25, 19, 26, 22))

    #Testeamos que se pueda modificar una campaña (siempre y cuando la campaña NO haya iniciado: 
    #la fecha de inicio de campaign start_date debe ser MENOR a la fecha actual) 
    #y que la columna a modificar se haya sobreescrito satisfactoriamente.
    def test_ModifyCampaign(self):
        #Precondicion: tener 1 campaign en la BD.
        userInputs= '{"email":"test@gmail.com","hashtags": ["#test", "#mock"], "mentions": ["@testCampaign", "@mockOK"], "startDate":"2018-12-18 18:02:00", "endDate":"2018-12-02 19:26:22"}'
        fields = json.loads(userInputs) #Pasa de json a diccionario, esto lo hace flask por eso no hace falta hacerlo en el insertCampaign() del manager.
        idCampaign = self.manager.insertCampaign(fields)
        
        #Comfirmamos el email antes de la modificación
        campaignOriginal = self.connector.selectCampaign(idCampaign)
        self.assertEqual(campaignOriginal.emailDueño, "test@gmail.com")

        #Datos que ingresara el usuario (además de la id2daCampaign):
        columna="email"
        inputUser="pepito@gmail.com"
        
        resultado = self.manager.modifyCampaign(idCampaign, columna, inputUser)
        campaignRetornada = self.connector.selectCampaign(idCampaign)
        #Si imprimo (campaignRetornada.startDate) me imprime: 2018-11-28 18:02:00.
        #Pero si lo retorno es este tipo de dato--> datetime.datetime(2018, 11, 28, 18, 2)
        self.assertEqual(campaignRetornada.emailDueño, "pepito@gmail.com")
        self.assertEqual(resultado, 200)
 
    #Pruebas en los metodos de manager:
    def test_ReturnCampaignBD(self):
        #Le pasamos la ID de Campaign 2
        objetoCampaign = self.connector.selectCampaign(2)
        print (objetoCampaign)
        #Imprime esto:
        # <idC:2 emailDueño:test@gmail.com hashtags:#test-#mock mentions:@testCampaign-@mockOK startDate:2018-11-28 18:02:00 finDate:2018-12-02 19:26:22> 

    def test_DeleteCampaignPorUser(self):
        email="test@gmail.com"
        self.manager.deleteCampaignsByEmail(email)

    def test_ReturnCampaignsInProgress(self):
        self.manager.returnCampaignsInProgress()

  