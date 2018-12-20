'''
Created on Dec 20, 2018

@author: Gabriel Torrandella
'''
from Reporter import reporter_flask
from Reporter.tests.test_reporter_base import test_reporter_base

from DataBaseConnector import test_database
import DataBaseConnector.configTables as configTables

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

    def setUp(self):
        test_reporter_base.setUp(self)
        
        self.databaseSetUp()
                
        self.test_app = reporter_flask.app.test_client()

    def tearDown(self):
        
        configTables.BD.metadata.drop_all(configTables.engine)


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()