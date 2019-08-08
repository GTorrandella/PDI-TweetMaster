'''
Created on Dec 12, 2018

@author: Gabriel Torrandella
'''
import unittest

from DataBaseConnector import test_database
from DataBaseConnector.Connector import Connector
import DataBaseConnector.configTables as configTables

from Manager import manager_flask
from Manager.tests.test_manager_base import test_manager_base

from datetime import datetime
from flask import json


class test_manager_flask(test_manager_base):

    def setUp(self):
        test_manager_base.setUp(self)
        
        self.connector = Connector(context='test')
        self.idCampaingList = []
        for campaign in self.initialCampaigns:
            self.idCampaingList.append(self.connector.insertCampaign(campaign))

        manager_flask.defineContext('test')

        self.test_app = manager_flask.app.test_client()
        self.test_app.testing = True

    def tearDown(self):
        manager_flask.manager.database.database.session.query(configTables.Tweet).delete()
        manager_flask.manager.database.database.session.query(configTables.Campaign).delete()
        manager_flask.manager.database.database.session.commit()

    def test_POST_201(self):
        
        initialCampaignNumber = len(manager_flask.manager.database.database.session.query(configTables.Campaign).all())
        self.assertEqual(initialCampaignNumber, 3)
        
        response = self.test_app.post('/Campaing', json = self.campaignCreationData, content_type='application/json')
        

        self.assertEqual(response.status, '201 CREATED')
           
        afterCampaigns = manager_flask.manager.database.database.session.query(configTables.Campaign).all()

        self.assertEqual(len(afterCampaigns), 4)

        newCampaign = afterCampaigns[3]
        self.assertEqual(str(newCampaign.id), response.get_etag()[0])
        self.assertEqual(newCampaign.email, 'hype@example.com')
        self.assertEqual(newCampaign.hashtags, '#JOKER-#SMASH')
        self.assertEqual(newCampaign.mentions, '@Sora_Sakurai')
        self.assertEqual(datetime.strftime(newCampaign.startDate, "%d %m %Y %X"), "31 12 2018 23:20:00")
        self.assertEqual(datetime.strftime(newCampaign.finDate, "%d %m %Y %X"), "01 01 2019 00:30:00")

    def test_POST_412(self):

        initialCampaignNumber = len(manager_flask.manager.database.database.session.query(configTables.Campaign).all())
        self.assertEqual(initialCampaignNumber, 3)
        
        response = self.test_app.post('/Campaing', json = self.campaignCreationDataError, content_type='application/json')
        
        self.assertEqual(response.status, '412 PRECONDITION FAILED')
        
        afterCampaigns = manager_flask.manager.database.database.session.query(configTables.Campaign).all()
        self.assertEqual(len(afterCampaigns), 3)

    def test_DELETE_by_id_200(self):
        initialCampaignNumber = len(manager_flask.manager.database.database.session.query(configTables.Campaign).all())
        self.assertEqual(initialCampaignNumber, 3)
        
        campaignDeleteByIDCData = {'idC' : str(self.idCampaingList[0])}

        response = self.test_app.delete('/Campaing', json = campaignDeleteByIDCData, content_type='application/json')
        
        self.assertEqual(response.status, '200 OK')
        
        afterCampaigns = manager_flask.manager.database.database.session.query(configTables.Campaign).all()
        self.assertEqual(len(afterCampaigns), 2)
        self.assertFalse(1 in [afterCampaigns[0].id,afterCampaigns[1].id])
        
    def test_DELETE_by_email_200(self):
        initialCampaignNumber = len(manager_flask.manager.database.database.session.query(configTables.Campaign).all())
        self.assertEqual(initialCampaignNumber, 3)
        
        response = self.test_app.delete('/Campaing', json = self.campaignDeleteByEmailData, content_type='application/json')
        
        self.assertEqual(response.status, '200 OK')
        
        afterCampaigns = manager_flask.manager.database.database.session.query(configTables.Campaign).all()
        self.assertEqual(len(afterCampaigns), 2)
        self.assertFalse(2 in [afterCampaigns[0].id,afterCampaigns[1].id])
    
    def test_DELETE_412(self):
        initialCampaignNumber = len(manager_flask.manager.database.database.session.query(configTables.Campaign).all())
        self.assertEqual(initialCampaignNumber, 3)
        
        response = self.test_app.delete('/Campaing', json = self.campaignDeleteDataError, content_type='application/json')
        
        self.assertEqual(response.status, '412 PRECONDITION FAILED')
        
        afterCampaigns = manager_flask.manager.database.database.session.query(configTables.Campaign).all()
        self.assertEqual(len(afterCampaigns), 3)
    
    def test_GET_200(self):
        initialCampaignNumber = len(manager_flask.manager.database.database.session.query(configTables.Campaign).all())
        self.assertEqual(initialCampaignNumber, 3)
        
        idCampaingToGet = str(self.idCampaingList[2])
        url = '/Campaing/' + idCampaingToGet

        response = self.test_app.get(url)
        self.assertEqual(response.status, '200 OK')
        
        responseCampaign = json.loads(response.json)
        self.assertEqual(str(responseCampaign['id']), idCampaingToGet)
        self.assertEqual(responseCampaign['email'], 'c@example.com')
        self.assertEqual(responseCampaign['hashtags'], ['#nintendo','#SMASH'])
        self.assertEqual(responseCampaign['mentions'], ['@Sora_Sakurai','@nintendo'])
        self.assertEqual(responseCampaign['startDate'], "31 12 2018 23:20:00")
        self.assertEqual(responseCampaign['finDate'], "01 01 2019 00:30:00")
        
        afterCampaigns = manager_flask.manager.database.database.session.query(configTables.Campaign).all()
        self.assertEqual(len(afterCampaigns), 3)
    
    def test_GET_404(self):
        initialCampaignNumber = len(manager_flask.manager.database.database.session.query(configTables.Campaign).all())
        self.assertEqual(initialCampaignNumber, 3)
        
        response = self.test_app.get('/Campaing/8')
        self.assertEqual(response.status, '404 NOT FOUND')
    
    def test_PACTH_202(self):
        initialCampaign = manager_flask.manager.database.database.session.query(configTables.Campaign).all()
        self.assertEqual(len(initialCampaign), 3)
        
        idCampaingToPatch = str(self.idCampaingList[2])

        campaignToPatch = initialCampaign[2]
        url = '/Campaing/' + idCampaingToPatch

        self.assertEqual(str(campaignToPatch.id), idCampaingToPatch)
        self.assertEqual(campaignToPatch.email, 'c@example.com')
        self.assertEqual(campaignToPatch.hashtags, '#nintendo-#SMASH')
        self.assertEqual(campaignToPatch.mentions, '@Sora_Sakurai-@nintendo')
        self.assertEqual(datetime.strftime(campaignToPatch.startDate, "%d %m %Y %X"), "31 12 2018 23:20:00")
        self.assertEqual(datetime.strftime(campaignToPatch.finDate, "%d %m %Y %X"), "01 01 2019 00:30:00")

        response = self.test_app.patch(url, json=self.campaignPatchHashtagsData, content_type='application/json')
        self.assertEqual(response.status, "202 ACCEPTED")
        
        patchedCampaigns = manager_flask.manager.database.database.session.query(configTables.Campaign).all()
        self.assertEqual(len(patchedCampaigns), 3)
        
        patchedHashtagsCampaign = patchedCampaigns[2]
        self.assertEqual(str(patchedHashtagsCampaign.id), idCampaingToPatch)
        self.assertEqual(patchedHashtagsCampaign.email, 'c@example.com')
        self.assertEqual(patchedHashtagsCampaign.hashtags, '#qatherine-#katherine-#catherine')
        self.assertEqual(patchedHashtagsCampaign.mentions, '@Sora_Sakurai-@nintendo')
        self.assertEqual(datetime.strftime(patchedHashtagsCampaign.startDate, "%d %m %Y %X"), "31 12 2018 23:20:00")
        self.assertEqual(datetime.strftime(patchedHashtagsCampaign.finDate, "%d %m %Y %X"), "01 01 2019 00:30:00")
        
        response = self.test_app.patch(url, json=self.campaignPatchMentionsData, content_type='application/json')
        self.assertEqual(response.status, "202 ACCEPTED")
        
        patchedCampaigns = manager_flask.manager.database.database.session.query(configTables.Campaign).all()
        self.assertEqual(len(patchedCampaigns), 3)
        
        patchedHashtagsCampaign = patchedCampaigns[2]
        self.assertEqual(str(patchedHashtagsCampaign.id), idCampaingToPatch)
        self.assertEqual(patchedHashtagsCampaign.email, 'c@example.com')
        self.assertEqual(patchedHashtagsCampaign.hashtags, '#qatherine-#katherine-#catherine')
        self.assertEqual(patchedHashtagsCampaign.mentions, '@atlususa-@stud_zero')
        self.assertEqual(datetime.strftime(patchedHashtagsCampaign.startDate, "%d %m %Y %X"), "31 12 2018 23:20:00")
        self.assertEqual(datetime.strftime(patchedHashtagsCampaign.finDate, "%d %m %Y %X"), "01 01 2019 00:30:00")
        
    def test_PACTH_404(self):
        initialCampaignNumber = len(manager_flask.manager.database.database.session.query(configTables.Campaign).all())
        self.assertEqual(initialCampaignNumber, 3)

        url = '/Campaing/' + str(self.idCampaingList[2] + 1)

        response = self.test_app.patch(url, json=self.campaignPatchHashtagsData, content_type='application/json')
        self.assertEqual(response.status, '404 NOT FOUND')

    def test_PACTH_412(self):
        initialCampaignNumber = len(manager_flask.manager.database.database.session.query(configTables.Campaign).all())
        self.assertEqual(initialCampaignNumber, 3)
        
        url = '/Campaing/' + str(self.idCampaingList[2])

        response = self.test_app.patch(url, json=self.campaignPatchErrorData, content_type='application/json')
        self.assertEqual(response.status, '412 PRECONDITION FAILED')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()