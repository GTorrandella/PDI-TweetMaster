'''
Created on Dec 20, 2018

@author: Gabriel Torrandella
'''
import unittest

from Campaign.Campaign import Campaign

class test_reporter_base(unittest.TestCase):
    
    initialCampaigns = [Campaign(1, "a@example.com", '#NothingBreaksLikeAHeart', "", "2018-02-25 18:00:00", "2018-02-25 18:30:00"),
                        Campaign(2, "b@example.com", "", '@atlususa', "2018-02-25 18:00:00", "2018-02-25 18:30:00"),
                        Campaign(3, "c@example.com", '#nintendo-#SMASH', '@Sora_Sakurai-@nintendo', "2018-02-25 18:00:00", "2018-02-25 18:30:00")]
    
    initialTweets = [{'ID':'1000',
                      'userName':'@uno',
                      'userid':'10001',
                      'hashtags':'#NothingBreaksLikeAHeart',
                      'mentions':'@mileycyrus',
                      'date':'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign':1},
                      {'ID':'1001',
                      'userName':'@uno',
                      'userid':'10001',
                      'hashtags':'#NothingBreaksLikeAHeart-#feminism',
                      'mentions':'',
                      'date':'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign':1},
                      {'ID':'1002',
                      'userName':'@dos',
                      'userid':'10002',
                      'hashtags':'#NothingBreaksLikeAHeart-#shit',
                      'mentions':'@mileycyrus',
                      'date':'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign':1},
                      {'ID':'1003',
                      'userName':'@tres',
                      'userid':'10003',
                      'hashtags':'#NothingBreaksLikeAHeart-#ThankYouNext',
                      'mentions':'@mileycyrus-@arianagrande',
                      'date':'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign':1},
                      {'ID':'1004',
                      'userName':'@uno',
                      'userid':'10001',
                      'hashtags':'#feminism-#catherine',
                      'mentions':'@atlususa',
                      'date':'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign':2},
                      {'ID':'1005',
                      'userName':'@cuatro',
                      'userid':'10004',
                      'hashtags':'#HYPE-#SMASH-#JOKER',
                      'mentions':'@atlususa',
                      'date':'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign':2},
                      {'ID':'1006',
                      'userName':'@cuatro',
                      'userid':'10004',
                      'hashtags':'#catherine-#katherine-#qatherine-#HYPE-#SMASH',
                      'mentions':'@atlususa',
                      'date':'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign':2},
                      {'ID':'2000',
                      'userName':'@cuatro',
                      'userid':'10004',
                      'hashtags':'#HYPE-#SMASH-#JOKER',
                      'mentions':'@atlususa',
                      'date':'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign':3},
                      {'ID':'2001',
                      'userName':'@cuatro',
                      'userid':'10004',
                      'hashtags':'#catherine-#katherine-#qatherine-#HYPE-#SMASH',
                      'mentions':'@atlususa',
                      'date':'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign':3},
                      {'ID':'2002',
                      'userName':'@cinco',
                      'userid':'10005',
                      'hashtags':'#SMASH-#nintendo-#waluigi',
                      'mentions':'',
                      'date':'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign':3},
                      {'ID':'2003',
                      'userName':'@cinco',
                      'userid':'10005',
                      'hashtags':'#waluigi',
                      'mentions':'@Sora_Sakurai',
                      'date':'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign':3},
                      {'ID':'2004',
                      'userName':'@seis',
                      'userid':'10005',
                      'hashtags':'#PleaseGoToSleep',
                      'mentions':'@Sora_Sakurai',
                      'date':'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign':3},
                      {'ID':'2005',
                      'userName':'@cuatro',
                      'userid':'10004',
                      'hashtags':'#PleaseGoToSleep-#HYPE',
                      'mentions':'@Sora_Sakurai',
                      'date':'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign':3},
                      {'ID':'2006',
                      'userName':'@cinco',
                      'userid':'10005',
                      'hashtags':'#waluigi-#SMASH-#nintendo',
                      'mentions':'@Sora_Sakurai',
                      'date':'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign':3},
                      {'ID':'2007',
                      'userName':'@cinco',
                      'userid':'10005',
                      'hashtags':'#waluigi-#CRY',
                      'mentions':'@Sora_Sakurai',
                      'date':'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign':3},
                      {'ID':'2008',
                      'userName':'@cinco',
                      'userid':'10005',
                      'hashtags':'#waluigi-#SMASH-#NEVERFORGET',
                      'mentions':'@nintendo',
                      'date':'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign':3}]
    

    def setUp(self):
        pass


    def tearDown(self):
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()