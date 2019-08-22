'''
Created on Dec 20, 2018

@author: Gabriel Torrandella
'''
import unittest

from DataBaseConnector.Connector import Connector
import DataBaseConnector.configTables as configTables

from Reporter import reporter_flask
from Reporter.tests.test_reporter_base import test_reporter_base

from Tweet.Tweet import Tweet

from datetime import datetime

class test_reporter_flask(test_reporter_base):

    def setUp(self):
        test_reporter_base.setUp(self)
        
        self.connector = Connector(context='test')
        self.idCampaingList = []
        for campaign in self.initialCampaigns:
            self.idCampaingList.append(self.connector.insertCampaign(campaign))

        for tweet in self.initialTweetsRaw:
            idCampaign = self.idCampaingList[tweet['idCampaign'] - 1]
            tweetToInsert = Tweet(tweet, raw=True)
            self.connector.insertTweet(tweetToInsert, idCampaign)


        reporter_flask.defineContext('test')

        self.test_app = reporter_flask.app.test_client()

    def tearDown(self):
        reporter_flask.reporter.database.database.session.query(configTables.Tweet).delete()
        reporter_flask.reporter.database.database.session.query(configTables.Campaign).delete()
        reporter_flask.reporter.database.database.session.commit()



    def test_GET_json_200(self):
        initialCampaignNumber = len(reporter_flask.reporter.database.database.session.query(configTables.Campaign).all())
        self.assertEqual(initialCampaignNumber, 3)
        
        initialTweetNumber = len(reporter_flask.reporter.database.database.session.query(configTables.Tweet).all())
        self.assertEqual(initialTweetNumber, 16)
        
        idCampaingToGet = str(self.idCampaingList[0])
        url = '/Reporter/ReporterJSON/' + idCampaingToGet

        response = self.test_app.get(url)
        self.assertEqual(response.status, '200 OK')
        
        summary = response.json
        self.assertEqual(summary['moreTwUser'],'uno')
        self.assertEqual(summary['userQuantity'], 3)
        self.assertEqual(summary['cant_tweets'], 4)
        
        afterCampaignNumber = len(reporter_flask.reporter.database.database.session.query(configTables.Campaign).all())
        self.assertEqual(afterCampaignNumber, 3)
        
        afterTweetNumber = len(reporter_flask.reporter.database.database.session.query(configTables.Tweet).all())
        self.assertEqual(afterTweetNumber, 16)

    def test_GET_json_404(self):
        initialCampaignNumber = len(reporter_flask.reporter.database.database.session.query(configTables.Campaign).all())
        self.assertEqual(initialCampaignNumber, 3)
        
        initialTweetNumber = len(reporter_flask.reporter.database.database.session.query(configTables.Tweet).all())
        self.assertEqual(initialTweetNumber, 16)
        
        idCampaingToGet = str(self.idCampaingList[2] + 1)
        url = '/Reporter/ReporterJSON/' + idCampaingToGet

        response = self.test_app.get(url)
        self.assertEqual(response.status, '404 NOT FOUND')
        
        afterCampaignNumber = len(reporter_flask.reporter.database.database.session.query(configTables.Campaign).all())
        self.assertEqual(afterCampaignNumber, 3)
        
        afterTweetNumber = len(reporter_flask.reporter.database.database.session.query(configTables.Tweet).all())
        self.assertEqual(afterTweetNumber, 16) 
    
    def test_GET_raw_200(self):
        initialCampaignNumber = len(reporter_flask.reporter.database.database.session.query(configTables.Campaign).all())
        self.assertEqual(initialCampaignNumber, 3)
        
        initialTweetNumber = len(reporter_flask.reporter.database.database.session.query(configTables.Tweet).all())
        self.assertEqual(initialTweetNumber, 16)
        
        idCampaingToGet = str(self.idCampaingList[2])
        url = '/Reporter/ReporterRAW/' + idCampaingToGet

        response = self.test_app.get(url)
        self.assertEqual(response.status, '200 OK')
        
        raw = response.json
        
        self.assertTrue('campaign' in raw.keys())
        rawCampaign = raw['campaign']
        self.assertEqual(rawCampaign['id'], self.idCampaingList[2])
        self.assertEqual(rawCampaign['email'], "c@example.com")
        self.assertEqual(rawCampaign['hashtags'], "#nintendo-#SMASH")
        self.assertEqual(rawCampaign['mentions'], "@Sora_Sakurai-@nintendo")
        self.assertEqual(rawCampaign['startDate'], "25 02 2018 18:00:00")
        self.assertEqual(rawCampaign['finDate'], "25 02 2018 18:30:00")
        
        self.assertTrue('tweets' in raw.keys())
        self.assertEqual(len(raw['tweets']), 9)
        
        afterCampaignNumber = len(reporter_flask.reporter.database.database.session.query(configTables.Campaign).all())
        self.assertEqual(afterCampaignNumber, 3)
        
        afterTweetNumber = len(reporter_flask.reporter.database.database.session.query(configTables.Tweet).all())
        self.assertEqual(afterTweetNumber, 16) 
    
    def test_GET_raw_404(self):
        initialCampaignNumber = len(reporter_flask.reporter.database.database.session.query(configTables.Campaign).all())
        self.assertEqual(initialCampaignNumber, 3)
        
        initialTweetNumber = len(reporter_flask.reporter.database.database.session.query(configTables.Tweet).all())
        self.assertEqual(initialTweetNumber, 16)
        
        idCampaingToGet = str(self.idCampaingList[2] + 1)
        url = '/Reporter/ReporterRAW/' + idCampaingToGet

        response = self.test_app.get(url)
        self.assertEqual(response.status, '404 NOT FOUND')
        
        afterCampaignNumber = len(reporter_flask.reporter.database.database.session.query(configTables.Campaign).all())
        self.assertEqual(afterCampaignNumber, 3)
        
        afterTweetNumber = len(reporter_flask.reporter.database.database.session.query(configTables.Tweet).all())
        self.assertEqual(afterTweetNumber, 16)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()