'''
Created on Nov 20, 2018

@author: Gabriel Torrandella
'''
import unittest
import Fetcher.fetcher.Fetcher as fetch
from unittest.mock import MagicMock



class Test(unittest.TestCase):


    def setUp(self):
        test = fetch()
        test.fetchByHashtag = MagicMock()
        test.fetchByHashtag.return_value = [""]
        pass


    def tearDown(self):
        pass

    
    def test_fetchByHashtag(self):
        test.fetchByHashtag.assert_not_called()
        pass
    
    def test_fetchByMentions(self):
        pass
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
