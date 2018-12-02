'''
Created on Nov 20, 2018

@author: Gabriel Torrandella
'''
import unittest
import fetcher as fetch
from unittest.mock import MagicMock
import tests.test_fetcher_init as responses



class test_fetcher(unittest.TestCase):

    def setUp(self):
        self.test = fetch.Fetcher()
        
        self.test.fetchByHashtag = MagicMock(return_value = responses.responseHastag)
        
        self.test.fetchByMention = MagicMock(return_value = responses.responseMention)
        
        self.lastId = responses.lastId


    def tearDown(self):
        pass
        
    
    def test_fetchByHashtag(self):
        result = self.test.fetchByHashtag("marth", self.lastId)
        self.test.fetchByHashtag.assert_any_call("marth", self.lastId)
        self.assertEqual(result, responses.responseHastag)

    
    def test_fetchByMentions(self):
        result = self.test.fetchByMention("lyn", self.lastId)
        self.test.fetchByMention.assert_any_call("lyn", self.lastId)
        self.assertEqual(result, responses.responseMention)
    
    def test_fetchCampagn(self):
        pass
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
