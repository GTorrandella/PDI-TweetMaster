'''
Created on Dec 20, 2018

@author: Gabriel Torrandella
'''
import unittest
from Tweet.Tweet import Tweet
from Campaign.Campaign import Campaign


class test_reporter_base(unittest.TestCase):
    initialCampaigns = [
        Campaign(1, "a@example.com", '#NothingBreaksLikeAHeart', "", "25 02 2018 18:00:00", "25 02 2018 18:30:00"),
        Campaign(2, "b@example.com", "", '@atlususa', "25 02 2018 18:00:00", "25 02 2018 18:30:00"),
        Campaign(3, "c@example.com", '#nintendo-#SMASH', '@Sora_Sakurai-@nintendo', "25 02 2018 18:00:00", "25 02 2018 18:30:00"),
        Campaign(4, "active@example.com", '#active', '@active', "25 02 2018 18:00:00", "25 02 2020 18:30:00"),
        Campaign(5, "noTweets@example.com", '#NoTweetsEnded', '@noActive', "25 02 2018 18:00:00", "25 02 2019 18:30:00")]

    initialTweetsRaw = [{'id_str': '1000',
                      'text': '#NothingBreaksLikeAHeart @mileycyrus',
                      'entities': {
                          'hashtags': ['#NothingBreaksLikeAHeart'],
                          'user_mentions': ['@mileycyrus'],
                      },
                      'user': {
                          'id_str': '10001',
                          'name': 'uno'
                      },
                      'created_at': 'Sun Feb 25 18:11:01 +0000 2018',
                         'idCampaign': 1},
                        {'id_str': '1001',
                      'text': '#NothingBreaksLikeAHeart #feminism @mileycyrus',
                      'entities': {
                          'hashtags': ['#NothingBreaksLikeAHeart', '#feminism'],
                          'user_mentions': ['@mileycyrus'],
                      },
                      'user': {
                          'id_str': '10001',
                          'name': 'uno'
                      },
                      'created_at': 'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign': 1},
                        {'id_str': '1002',
                      'text': '#NothingBreaksLikeAHeart #shit @mileycyrus',
                      'entities': {
                          'hashtags': ['#NothingBreaksLikeAHeart', '#shit'],
                          'user_mentions': ['@mileycyrus'],
                      },
                      'user': {
                          'id_str': '10002',
                          'name': 'dos'
                      },
                      'created_at': 'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign': 1},
                        {'id_str': '1003',
                      'text': '#NothingBreaksLikeAHeart #ThankYouNext @mileycyrus',
                      'entities': {
                          'hashtags': ['#NothingBreaksLikeAHeart', '#ThankYouNext'],
                          'user_mentions': ['@mileycyrus', '@arianagrande'],
                      },
                      'user': {
                          'id_str': '10003',
                          'name': 'tres'
                      },
                      'created_at': 'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign': 1},
                        {'id_str': '1004',
                      'text': '#feminism-#catherine @atlususa',
                      'entities': {
                          'hashtags': ['#feminism', '#catherine'],
                          'user_mentions': ['@atlususa'],
                      },
                      'user': {
                          'id_str': '10001',
                          'name': 'uno'
                      },
                      'created_at': 'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign': 2},
                        {'id_str': '1005',
                      'text': '#HYPE-#SMASH-#JOKER @atlususa',
                      'entities': {
                          'hashtags': ['#JOKER', '#HYPE', '#SMASH'],
                          'user_mentions': ['@atlususa'],
                      },
                      'user': {
                          'id_str': '10004',
                          'name': 'cuatro'
                      },
                      'created_at': 'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign': 2},
                        {'id_str': '1006',
                      'text': '#HYPE-#catherine-#katherine-#qatherine-#SMASH @atlususa',
                      'entities': {
                          'hashtags': ['#catherine', '#katherine', '#qatherine', '#HYPE', '#SMASH'],
                          'user_mentions': ['@atlususa'],
                      },
                      'user': {
                          'id_str': '10004',
                          'name': 'cuatro'
                      },
                      'created_at': 'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign': 2},
                        {'id_str': '2000',
                      'text': '#HYPE-#SMASH-#JOKER @atlususa',
                      'entities': {
                          'hashtags': ['#JOKER', '#HYPE', '#SMASH'],
                          'user_mentions': ['@atlususa'],
                      },
                      'user': {
                          'id_str': '10004',
                          'name': 'cuatro'
                      },
                      'created_at': 'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign': 3},
                        {'id_str': '2001',
                      'text': '#HYPE-#catherine-#katherine-#qatherine-#SMASH @atlususa',
                      'entities': {
                          'hashtags': ['#catherine', '#katherine', '#qatherine', '#HYPE', '#SMASH'],
                          'user_mentions': ['@atlususa'],
                      },
                      'user': {
                          'id_str': '10004',
                          'name': 'cuatro'
                      },
                      'created_at': 'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign': 3},
                        {'id_str': '2002',
                      'text': '#SMASH #nintendo #waluigi',
                      'entities': {
                          'hashtags': ['#nintendo', '#waluigi', '#SMASH'],
                          'user_mentions': [],
                      },
                      'user': {
                          'id_str': '10005',
                          'name': 'cinco'
                      },
                      'created_at': 'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign': 3},
                        {'id_str': '2003',
                      'text': '#waluigi',
                      'entities': {
                          'hashtags': ['#waluigi'],
                          'user_mentions': ['@Sora_Sakurai'],
                      },
                      'user': {
                          'id_str': '10005',
                          'name': 'cinco'
                      },
                      'created_at': 'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign': 3},
                        {'id_str': '2004',
                      'text': '#waluigi',
                      'entities': {
                          'hashtags': ['#PleaseGoToSleep'],
                          'user_mentions': ['@Sora_Sakurai'],
                      },
                      'user': {
                          'id_str': '10006',
                          'name': 'seis'
                      },
                      'created_at': 'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign': 3},
                        {'id_str': '2005',
                      'text': '',
                      'entities': {
                          'hashtags': ['#PleaseGoToSleep', '#HYPE'],
                          'user_mentions': ['@Sora_Sakurai'],
                      },
                      'user': {
                          'id_str': '10004',
                          'name': 'cuatro'
                      },
                      'created_at': 'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign': 3},
                        {'id_str': '2006',
                      'text': '#SMASH #nintendo #waluigi',
                      'entities': {
                          'hashtags': ['#nintendo', '#waluigi', '#SMASH'],
                          'user_mentions': ['@Sora_Sakurai'],
                      },
                      'user': {
                          'id_str': '10005',
                          'name': 'cinco'
                      },
                      'created_at': 'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign': 3},
                        {'id_str': '2007',
                      'text': '#SMASH #nintendo #waluigi',
                      'entities': {
                          'hashtags': ['#CRY', '#waluigi'],
                          'user_mentions': ['@Sora_Sakurai'],
                      },
                      'user': {
                          'id_str': '10005',
                          'name': 'cinco'
                      },
                      'created_at': 'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign': 3},
                        {'id_str': '2008',
                      'text': '#SMASH #NEVERFORGET #waluigi',
                      'entities': {
                          'hashtags': ['#NERVERFORGET', '#waluigi', "#SMASH"],
                          'user_mentions': ['@nintendo'],
                      },
                      'user': {
                          'id_str': '10005',
                          'name': 'cinco'
                      },
                      'created_at': 'Sun Feb 25 18:11:01 +0000 2018',
                      'idCampaign': 3}]

    tweetsRawCampaign1 = [initialTweetsRaw[0],
                       initialTweetsRaw[1],
                       initialTweetsRaw[2],
                       initialTweetsRaw[3]]
    tweetsRawCampaign2 = [initialTweetsRaw[4],
                       initialTweetsRaw[5],
                       initialTweetsRaw[6]]
    tweetsRawCampaign3 = [initialTweetsRaw[7],
                       initialTweetsRaw[8],
                       initialTweetsRaw[9],
                       initialTweetsRaw[10],
                       initialTweetsRaw[11],
                       initialTweetsRaw[12],
                       initialTweetsRaw[13],
                       initialTweetsRaw[14],
                       initialTweetsRaw[15]]

    tweetsCampaign1 = [Tweet(initialTweetsRaw[0], raw=True),
                       Tweet(initialTweetsRaw[1], raw=True),
                       Tweet(initialTweetsRaw[2], raw=True),
                       Tweet(initialTweetsRaw[3], raw=True)]
    tweetsCampaign2 = [Tweet(initialTweetsRaw[4], raw=True),
                       Tweet(initialTweetsRaw[5], raw=True),
                       Tweet(initialTweetsRaw[6], raw=True)]
    tweetsCampaign3 = [Tweet(initialTweetsRaw[7], raw=True),
                       Tweet(initialTweetsRaw[8], raw=True),
                       Tweet(initialTweetsRaw[9], raw=True),
                       Tweet(initialTweetsRaw[10], raw=True),
                       Tweet(initialTweetsRaw[11], raw=True),
                       Tweet(initialTweetsRaw[12], raw=True),
                       Tweet(initialTweetsRaw[13], raw=True),
                       Tweet(initialTweetsRaw[14], raw=True),
                       Tweet(initialTweetsRaw[15], raw=True)]

    def setUp(self):
        pass

    def tearDown(self):
        pass


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
