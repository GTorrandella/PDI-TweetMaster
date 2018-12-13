'''
Created on Dec 12, 2018

@author: Gabriel Torrandella
'''
import unittest

from Campaign import Campaign


class test_manager_base(unittest.TestCase):


    def setUp(self):
        self.campaignCreationDate = {'email':'hype@example.com', 
                                     'hashtags':'#JOKER-#smash', 
                                     'mentions':'@Sora_Sakurai',
                                     'startDate':"06 12 2018 23:20:00",
                                     'endDate':"07 12 2018 00:30:00"}


    def tearDown(self):
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()