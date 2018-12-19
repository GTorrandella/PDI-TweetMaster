'''
Created on Dec 12, 2018

@author: Gabriel Torrandella
'''
import unittest
from unittest.mock import MagicMock

import DataBaseConnector.configTables as configTables
from Manager.manager import Manager
from Manager import manager_flask
from Manager.tests.test_manager_base import test_manager_base

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database


class test_manager_flask(test_manager_base):


    def setUp(self):
        global BD, engine, Session, session
        
        test_manager_base.setUp(self)
        
        configTables.engine = create_engine("sqlite://")
        create_database(configTables.engine.url)
        configTables.BD = declarative_base()
        Session = sessionmaker(bind=configTables.engine)
        configTables.session = Session()
        
        self.test_app = manager_flask.app.test_client()

    def tearDown(self):
        pass


    def test_POST_201(self):
        response = self.test_app.post('/Campaing', json = self.campaignCreationData, content_type='application/json')
        print(response)
    
    def test_POST_412(self):
        pass

    def test_DELETE_200(self):
        pass
    
    def test_DELETE_404(self):
        pass
    
    def test_DELETE_412(self):
        pass
    
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