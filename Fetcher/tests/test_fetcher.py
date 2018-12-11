'''
Created on Nov 20, 2018

@author: Gabriel Torrandella
'''
import unittest
import fetcher as fetch
from unittest.mock import MagicMock
from tests.test_fetcher_base import test_fetcher_base



class test_fetcher(test_fetcher_base):

    def setUp(self):
        test_fetcher_base.setUp(self)
        self.test = fetch.Fetcher()
        
        self.test.fetchByHashtag = MagicMock(return_value = self.responseHastag)
        
        self.test.fetchByMention = MagicMock(return_value = self.responseMention)


    def tearDown(self):
        pass
        
    
    def test_fetchByHashtag(self):
        result = self.test.fetchByHashtag("mars", self.lastId)
        
        self.test.fetchByHashtag.assert_any_call("mars", self.lastId)
        self.assertEqual(result, self.responseHastag)

    
    def test_fetchByMentions(self):
        result = self.test.fetchByMention("mars", self.lastId)
        
        self.test.fetchByMention.assert_any_call("mars", self.lastId)
        self.assertEqual(result, self.responseMention)
    
    def test_fetchCampagn(self):
        result = self.test.fetchTweets(self.campaign, self.lastId)
        
        self.test.fetchByHashtag.assert_called_once_with("mars", self.lastId)
        self.test.fetchByMention.assert_called_once_with("mars", self.lastId)
        
        self.assertEqual(result, self.response_fetchTweets)
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
