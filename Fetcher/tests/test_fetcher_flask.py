'''
Created on Nov 20, 2018

@author: Gabriel Torrandella
'''
import unittest
from tests.test_fetcher_base import test_fetcher_base

import fetcher_flask

class test_fetcher_flask(test_fetcher_base):


    def setUp(self):
        test_fetcher_base.setUp(self)
        
        self.test_app = fetcher_flask.app.test_client()
        self.test_app
        self.ctx = fetcher_flask.app.app_context()
        self.ctx.push()

    def tearDown(self):
        self.ctx.pop()


    def test_GET_200(self):
        response = self.test_app.get('/fetcher',json=self.resquest_get_200_content, content_type = 'application/json')
        
        self.assertEqual(response.status, '200 OK')
        
    def test_GET_400(self):
        response = self.test_app.get('/fetcher', content_type = 'application/json')
        
        self.assertEqual(response.status, '400 BAD REQUEST')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_correctPut']
    unittest.main()