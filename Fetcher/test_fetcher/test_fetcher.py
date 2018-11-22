'''
Created on Nov 20, 2018

@author: Gabriel Torrandella
'''
import unittest
import Fetcher.fetcher.Fetcher as fetch
from unittest.mock import MagicMock, _return_values
import test_fetcher.test_fetcher_init as responses



class Test(unittest.TestCase):


    def setUp(self):
        self.test = fetch()
        
        self.test.fetchByHashtag = MagicMock(return_value = responses.responseHastag)
        
        self.test.fetchByMention() = MagicMock(return_value = responses.responseMention)


    def tearDown(self):
        
        self.test.fetchByHashtag().dispose()
        self.test.fetchByMention().dispose()
        
        self.test.dispose()
        
    
    def test_fetchByHashtag(self):
        result = self.test.fetchByHashtag("marth")
        self.assertAlmostEquals(result, responses.responseHastag)

    
    def test_fetchByMentions(self):
        pass
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
