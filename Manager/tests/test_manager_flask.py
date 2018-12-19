'''
Created on Dec 12, 2018

@author: Gabriel Torrandella
'''
import unittest
from unittest.mock import MagicMock

from DataBaseConnector import test_database

import DataBaseConnector.configTables as configTables
from Manager.manager import Manager
from Manager import manager_flask
from Manager.tests.test_manager_base import test_manager_base

from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from distutils.command.config import config


class test_manager_flask(test_manager_base):

    def databaseSetUp(self):
        configTables.engine = test_database.engine
        configTables.BD = test_database.BD
        configTables.session = test_database.session
        
        configTables.Campaign = test_database.Campaign
        configTables.Tweet = test_database.Tweet
        
        configTables.Campaign.metadata.create_all(configTables.engine)
        configTables.Tweet.metadata.create_all(configTables.engine)
        
        for c in self.initialCampaigns:
            configTables.session.add(configTables.Campaign(startDate=(datetime.strftime((c.startDate),"%d %m %Y %X")), finDate=(datetime.strftime((c.finDate),"%d %m %Y %X")), email=(c.emailDueño), hashtags=(c.hashtags), mentions=(c.mentions)))
        configTables.session.new
        configTables.session.dirty
        configTables.session.commit()
        


    def setUp(self):
        test_manager_base.setUp(self)
        
        self.databaseSetUp()
                
        self.test_app = manager_flask.app.test_client()

    def tearDown(self):
        
        configTables.BD.metadata.drop_all(configTables.engine)


    def test_POST_201(self):
        
        initialCampaignNumber = len(configTables.session.query(configTables.Campaign).all())
        self.assertEqual(initialCampaignNumber, 3)
        
        response = self.test_app.post('/Campaing', json = self.campaignCreationData, content_type='application/json')
        
        self.assertEqual(response.status, '201 CREATED')
        
        afterCampaigns = configTables.session.query(configTables.Campaign).all()
        newCampaign = afterCampaigns[3]
        
        self.assertEqual(len(afterCampaigns), 4)
        
        self.assertEqual(newCampaign.id, 4)
        self.assertEqual(newCampaign.email, 'hype@example.com')
        self.assertEqual(newCampaign.hashtags, '#JOKER-#SMASH')
        self.assertEqual(newCampaign.mentions, '@Sora_Sakurai')
        self.assertEqual(newCampaign.startDate, "06 12 2018 23:20:00")
        self.assertEqual(newCampaign.finDate, "07 12 2018 00:30:00"),
                                 
    
    def test_POST_412(self):
        initialCampaignNumber = len(configTables.session.query(configTables.Campaign).all())
        self.assertEqual(initialCampaignNumber, 3)
        
        response = self.test_app.post('/Campaing', json = self.campaignCreationDataError, content_type='application/json')
        
        self.assertEqual(response.status, '412 PRECONDITION FAILED')
        
        afterCampaigns = configTables.session.query(configTables.Campaign).all()
        self.assertEqual(len(afterCampaigns), 3)

    def test_DELETE_by_id_200(self):
        initialCampaignNumber = len(configTables.session.query(configTables.Campaign).all())
        self.assertEqual(initialCampaignNumber, 3)
        
        response = self.test_app.delete('/Campaing', json = self.campaignDeleteByIDCData, content_type='application/json')
        
        self.assertEqual(response.status, '200 OK')
        
        afterCampaigns = configTables.session.query(configTables.Campaign).all()
        self.assertEqual(len(afterCampaigns), 2)
        self.assertFalse(1 in [afterCampaigns[0].id,afterCampaigns[1].id])
        
    def test_DELETE_by_email_200(self):
        initialCampaignNumber = len(configTables.session.query(configTables.Campaign).all())
        self.assertEqual(initialCampaignNumber, 3)
        
        response = self.test_app.delete('/Campaing', json = self.campaignDeleteByEmailData, content_type='application/json')
        
        self.assertEqual(response.status, '200 OK')
        
        afterCampaigns = configTables.session.query(configTables.Campaign).all()
        self.assertEqual(len(afterCampaigns), 2)
        self.assertFalse(2 in [afterCampaigns[0].id,afterCampaigns[1].id])
            
    def test_DELETE_404(self):
        pass
    
    def test_DELETE_412(self):
        initialCampaignNumber = len(configTables.session.query(configTables.Campaign).all())
        self.assertEqual(initialCampaignNumber, 3)
        
        response = self.test_app.delete('/Campaing', json = self.campaignDeleteDataError, content_type='application/json')
        
        self.assertEqual(response.status, '412 PRECONDITION FAILED')
        
        afterCampaigns = configTables.session.query(configTables.Campaign).all()
        self.assertEqual(len(afterCampaigns), 3)
    
    def test_GET_200(self):
        pass
    
    def test_GET_404(self):
        pass
    
    def test_PACTH_202(self):
        pass
    
    def test_PACTH_404(self):
        pass

    def test_PACTH_412(self):
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()