'''
Created on Dec 20, 2018

@author: Gabriel Torrandella
'''
import unittest

from DataBaseConnector import test_database
import DataBaseConnector.configTables as configTables

from Reporter import reporter_flask
from Reporter.tests.test_reporter_base import test_reporter_base

from datetime import datetime
from flask import jsonify

class test_reporter_flask(test_reporter_base):


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
        
        for t in self.initialTweets:
            configTables.session.add(configTables.Tweet(idCampaign=t['idCampaign'], ID=t['ID'], userName=t['userName'], userid=t['userid'], hashtags=t['hashtags'],mentions=t['mentions'], date=t['date']))
        configTables.session.new
        configTables.session.dirty
        configTables.session.commit()

    def setUp(self):
        test_reporter_base.setUp(self)
        
        self.databaseSetUp()
        
        self.test_app = reporter_flask.app.test_client()

    def tearDown(self):
        
        configTables.BD.metadata.drop_all(configTables.engine)


    def test_GET_json_200(self):
        initialCampaignNumber = len(configTables.session.query(configTables.Campaign).all())
        self.assertEqual(initialCampaignNumber, 3)
        
        initialTweetNumber = len(configTables.session.query(configTables.Tweet).all())
        self.assertEqual(initialTweetNumber, 16)
        
        response = self.test_app.get('/Reporter/ReporterJSON/1')
        self.assertEqual(response.status, '200 OK')
        
        summary = response.json
        self.assertEqual(summary['moreTwUser'],'@uno')
        self.assertEqual(summary['userQuantity'], 3)
        self.assertEqual(summary['cant_tweets'], 4)
        
        afterCampaignNumber = len(configTables.session.query(configTables.Campaign).all())
        self.assertEqual(afterCampaignNumber, 3)
        
        afterTweetNumber = len(configTables.session.query(configTables.Tweet).all())
        self.assertEqual(afterTweetNumber, 16)

    def test_GET_json_404(self):
        initialCampaignNumber = len(configTables.session.query(configTables.Campaign).all())
        self.assertEqual(initialCampaignNumber, 3)
        
        initialTweetNumber = len(configTables.session.query(configTables.Tweet).all())
        self.assertEqual(initialTweetNumber, 16)
        
        response = self.test_app.get('/Reporter/ReporterJSON/4')
        self.assertEqual(response.status, '404 NOT FOUND')
        
        afterCampaignNumber = len(configTables.session.query(configTables.Campaign).all())
        self.assertEqual(afterCampaignNumber, 3)
        
        afterTweetNumber = len(configTables.session.query(configTables.Tweet).all())
        self.assertEqual(afterTweetNumber, 16) 
    
    def test_GET_raw_200(self):
        initialCampaignNumber = len(configTables.session.query(configTables.Campaign).all())
        self.assertEqual(initialCampaignNumber, 3)
        
        initialTweetNumber = len(configTables.session.query(configTables.Tweet).all())
        self.assertEqual(initialTweetNumber, 16)
        
        response = self.test_app.get('/Reporter/ReporterRAW/3')
        self.assertEqual(response.status, '200 OK')
        
        raw = response.json
        
        self.assertTrue('campaign' in raw.keys())
        rawCampaign = raw['campaign']
        self.assertEqual(rawCampaign['id'], 3)
        self.assertEqual(rawCampaign['email'], "c@example.com")
        self.assertEqual(rawCampaign['hashtags'], "#nintendo-#SMASH")
        self.assertEqual(rawCampaign['mentions'], "@Sora_Sakurai-@nintendo")
        self.assertEqual(rawCampaign['startDate'], "25 02 2018 18:00:00")
        self.assertEqual(rawCampaign['finDate'], "25 02 2018 18:30:00")
        
        self.assertTrue('tweets' in raw.keys())
        self.assertEqual(len(raw['tweets']), 9)
        
        afterCampaignNumber = len(configTables.session.query(configTables.Campaign).all())
        self.assertEqual(afterCampaignNumber, 3)
        
        afterTweetNumber = len(configTables.session.query(configTables.Tweet).all())
        self.assertEqual(afterTweetNumber, 16) 
    
    def test_GET_raw_404(self):
        initialCampaignNumber = len(configTables.session.query(configTables.Campaign).all())
        self.assertEqual(initialCampaignNumber, 3)
        
        initialTweetNumber = len(configTables.session.query(configTables.Tweet).all())
        self.assertEqual(initialTweetNumber, 16)
        
        response = self.test_app.get('/Reporter/ReporterRAW/8')
        self.assertEqual(response.status, '404 NOT FOUND')
        
        afterCampaignNumber = len(configTables.session.query(configTables.Campaign).all())
        self.assertEqual(afterCampaignNumber, 3)
        
        afterTweetNumber = len(configTables.session.query(configTables.Tweet).all())
        self.assertEqual(afterTweetNumber, 16)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()