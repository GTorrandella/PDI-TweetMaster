import unittest
from Tweet.Tweet import Tweet
from DataBaseConnector import Connector, configTables
from Reporter.Reporter import Reporter
from Reporter.tests.test_reporter_base import test_reporter_base as base

class test_reporter(unittest.TestCase):

    def setUp(self):
        self.reporter = Reporter(context='test')
        self.idCampaingList = []

        for c in base.initialCampaigns:
            insertedCampaignID = self.reporter.database.insertCampaign(c)
            c.idC = insertedCampaignID
            self.idCampaingList.append(insertedCampaignID)

        self.reporter.database.insertTweetsList(base.tweetsCampaign1, self.idCampaingList[0])
        self.reporter.database.insertTweetsList(base.tweetsCampaign2, self.idCampaingList[1])
        self.reporter.database.insertTweetsList(base.tweetsCampaign3, self.idCampaingList[2])

    def tearDown(self):
        self.reporter.database.database.session.query(configTables.Tweet).delete()
        self.reporter.database.database.session.query(configTables.Campaign).delete()
        self.reporter.database.database.session.commit()
        pass

    def test_reportSummary(self):  # OK
        summaryCampaign1 = self.reporter.reportSummary(self.idCampaingList[0])
        summaryCampaign2 = self.reporter.reportSummary(self.idCampaingList[1])
        summaryCampaign3 = self.reporter.reportSummary(self.idCampaingList[2])
        summaryActiveCampaign = self.reporter.reportSummary(self.idCampaingList[3])
        summaryCampaignWithoutTweets = self.reporter.reportSummary(self.idCampaingList[4])
        summaryCampaignNotFound = self.reporter.reportSummary(4956)

        expectedSummaryCampaign1 = {
            'campaign': {'id': self.idCampaingList[0], 'email': 'a@example.com', 'hashtags': '#NothingBreaksLikeAHeart', 'mentions': '',
                         'startDate': '25 02 2018 18:00:00', 'finDate': '25 02 2018 18:30:00'}, 'cant_tweets': 4,
            'moreTwUser': 'uno', 'userQuantity': 3}
        expectedSummaryCampaign2 = {
            'campaign': {'id': self.idCampaingList[1], 'email': 'b@example.com', 'hashtags': '', 'mentions': '@atlususa',
                         'startDate': '25 02 2018 18:00:00', 'finDate': '25 02 2018 18:30:00'}, 'cant_tweets': 3,
            'moreTwUser': 'cuatro', 'userQuantity': 2}
        expectedSummaryCampaign3 = {'campaign': {'id': self.idCampaingList[2], 'email': 'c@example.com', 'hashtags': '#nintendo-#SMASH',
                                                 'mentions': '@Sora_Sakurai-@nintendo',
                                                 'startDate': '25 02 2018 18:00:00', 'finDate': '25 02 2018 18:30:00'},
                                    'cant_tweets': 9, 'moreTwUser': 'cinco', 'userQuantity': 3}
        expectedSummaryCampaignWithoutTweets = {
            'campaign': {'id': self.idCampaingList[4], 'email': 'noTweets@example.com', 'hashtags': '#NoTweetsEnded',
                         'mentions': '@noActive', 'startDate': '25 02 2018 18:00:00', 'finDate': '25 02 2019 18:30:00'},
            'message': 'No se obtuvieron Tweets con la campaña designada!'}

        self.assertEqual(summaryCampaign1, expectedSummaryCampaign1)
        self.assertEqual(summaryCampaign2, expectedSummaryCampaign2)
        self.assertEqual(summaryCampaign3, expectedSummaryCampaign3)
        self.assertEqual(summaryActiveCampaign, 412)
        self.assertEqual(summaryCampaignWithoutTweets, expectedSummaryCampaignWithoutTweets)
        self.assertEqual(summaryCampaignNotFound, 404)

    # Dada la campaña y tweets testeamos si los datos raw son retornados correctamente:
    def test_reportRawData(self):
        rawDataCampaign1 = self.reporter.reportRawData(self.idCampaingList[0])
        rawDataCampaign2 = self.reporter.reportRawData(self.idCampaingList[1])
        rawDataCampaign3 = self.reporter.reportRawData(self.idCampaingList[2])
        rawDataActiveCampaign = self.reporter.reportRawData(self.idCampaingList[3])
        rawDataCampaignWithoutTweets = self.reporter.reportRawData(self.idCampaingList[4])
        rawDataCampaignNotFound = self.reporter.reportRawData(404665)

        campaignRawInfoExpected1 = base.initialCampaigns[0].to_dict()
        campaignRawInfoExpected2 = base.initialCampaigns[1].to_dict()
        campaignRawInfoExpected3 = base.initialCampaigns[2].to_dict()
        rawTweetsDataExpected1 = [{'id_str': '1000', 'user': {'name': 'uno', 'id_str': '10001'},
                                   'entities': {'hashtags': '#NothingBreaksLikeAHeart', 'user_mentions': '@mileycyrus'},
                                   'created_at': '2018-02-25 18:11:01'},
                                  {'id_str': '1001', 'user': {'name': 'uno', 'id_str': '10001'},
                                   'entities': {'hashtags': '#NothingBreaksLikeAHeart-#feminism',
                                                'user_mentions': '@mileycyrus'}, 'created_at': '2018-02-25 18:11:01'},
                                  {'id_str': '1002', 'user': {'name': 'dos', 'id_str': '10002'},
                                   'entities': {'hashtags': '#NothingBreaksLikeAHeart-#shit',
                                                'user_mentions': '@mileycyrus'}, 'created_at': '2018-02-25 18:11:01'},
                                  {'id_str': '1003', 'user': {'name': 'tres', 'id_str': '10003'},
                                   'entities': {'hashtags': '#NothingBreaksLikeAHeart-#ThankYouNext',
                                                'user_mentions': '@mileycyrus-@arianagrande'},
                                   'created_at': '2018-02-25 18:11:01'}]
        rawTweetsDataExpected2 = [{'id_str': '1004', 'user': {'name': 'uno', 'id_str': '10001'},
                                   'entities': {'hashtags': '#feminism-#catherine', 'user_mentions': '@atlususa'},
                                   'created_at': '2018-02-25 18:11:01'},
                                  {'id_str': '1005', 'user': {'name': 'cuatro', 'id_str': '10004'},
                                   'entities': {'hashtags': '#JOKER-#HYPE-#SMASH', 'user_mentions': '@atlususa'},
                                   'created_at': '2018-02-25 18:11:01'},
                                  {'id_str': '1006', 'user': {'name': 'cuatro', 'id_str': '10004'},
                                   'entities': {'hashtags': '#catherine-#katherine-#qatherine-#HYPE-#SMASH',
                                                'user_mentions': '@atlususa'}, 'created_at': '2018-02-25 18:11:01'}]
        rawTweetsDataExpected3 = [{'id_str': '2000', 'user': {'name': 'cuatro', 'id_str': '10004'},
                                   'entities': {'hashtags': '#JOKER-#HYPE-#SMASH', 'user_mentions': '@atlususa'},
                                   'created_at': '2018-02-25 18:11:01'},
                                  {'id_str': '2001', 'user': {'name': 'cuatro', 'id_str': '10004'},
                                   'entities': {'hashtags': '#catherine-#katherine-#qatherine-#HYPE-#SMASH',
                                                'user_mentions': '@atlususa'}, 'created_at': '2018-02-25 18:11:01'},
                                  {'id_str': '2002', 'user': {'name': 'cinco', 'id_str': '10005'},
                                   'entities': {'hashtags': '#nintendo-#waluigi-#SMASH', 'user_mentions': ''},
                                   'created_at': '2018-02-25 18:11:01'},
                                  {'id_str': '2003', 'user': {'name': 'cinco', 'id_str': '10005'},
                                   'entities': {'hashtags': '#waluigi', 'user_mentions': '@Sora_Sakurai'},
                                   'created_at': '2018-02-25 18:11:01'},
                                  {'id_str': '2004', 'user': {'name': 'seis', 'id_str': '10006'},
                                   'entities': {'hashtags': '#PleaseGoToSleep', 'user_mentions': '@Sora_Sakurai'},
                                   'created_at': '2018-02-25 18:11:01'},
                                  {'id_str': '2005', 'user': {'name': 'cuatro', 'id_str': '10004'},
                                   'entities': {'hashtags': '#PleaseGoToSleep-#HYPE', 'user_mentions': '@Sora_Sakurai'},
                                   'created_at': '2018-02-25 18:11:01'},
                                  {'id_str': '2006', 'user': {'name': 'cinco', 'id_str': '10005'},
                                   'entities': {'hashtags': '#nintendo-#waluigi-#SMASH',
                                                'user_mentions': '@Sora_Sakurai'}, 'created_at': '2018-02-25 18:11:01'},
                                  {'id_str': '2007', 'user': {'name': 'cinco', 'id_str': '10005'},
                                   'entities': {'hashtags': '#CRY-#waluigi', 'user_mentions': '@Sora_Sakurai'},
                                   'created_at': '2018-02-25 18:11:01'},
                                  {'id_str': '2008', 'user': {'name': 'cinco', 'id_str': '10005'},
                                   'entities': {'hashtags': '#NERVERFORGET-#waluigi-#SMASH',
                                                'user_mentions': '@nintendo'}, 'created_at': '2018-02-25 18:11:01'}]
        rawDataCampaignWithoutTweetsExpected = {
            'campaign': {'id': self.idCampaingList[4], 'email': 'noTweets@example.com', 'hashtags': '#NoTweetsEnded',
                         'mentions': '@noActive', 'startDate': '25 02 2018 18:00:00', 'finDate': '25 02 2019 18:30:00'},
            'tweets': []}

        self.assertEqual(rawDataCampaign1['campaign'], campaignRawInfoExpected1)
        self.assertEqual(rawDataCampaign2['campaign'], campaignRawInfoExpected2)
        self.assertEqual(rawDataCampaign3['campaign'], campaignRawInfoExpected3)
        self.assertEqual(rawDataCampaign1['tweets'], rawTweetsDataExpected1)
        self.assertEqual(rawDataCampaign2['tweets'], rawTweetsDataExpected2)
        self.assertEqual(rawDataCampaign3['tweets'], rawTweetsDataExpected3)

        self.assertEqual(rawDataActiveCampaign, 412)
        self.assertEqual(rawDataCampaignWithoutTweets, rawDataCampaignWithoutTweetsExpected)
        self.assertEqual(rawDataCampaignNotFound, 404)

    # Dados tweets testeamos retornar el usuario con mayor cantidad de tweets:
    def test_getUserWithMoreTw(self):
        mostTwUserInCampaign1 = self.reporter.getUserWithMoreTw(base.tweetsRawCampaign1)
        mostTwUserInCampaign2 = self.reporter.getUserWithMoreTw(base.tweetsRawCampaign2)
        mostTwUserInCampaign3 = self.reporter.getUserWithMoreTw(base.tweetsRawCampaign3)
        self.assertEqual(mostTwUserInCampaign1, 'uno')
        self.assertEqual(mostTwUserInCampaign2, 'cuatro')
        self.assertEqual(mostTwUserInCampaign3, 'cinco')

    # Testeamos retornar el usuario con mayor cantidad de tweets para cada campaign:
    def test_getUserQuantity(self):
        userQuantityInCampaign1 = (self.reporter.getUserQuantity(base.tweetsRawCampaign1))
        userQuantityInCampaign2 = (self.reporter.getUserQuantity(base.tweetsRawCampaign2))
        userQuantityInCampaign3 = (self.reporter.getUserQuantity(base.tweetsRawCampaign3))
        self.assertEqual(userQuantityInCampaign1, 3)
        self.assertEqual(userQuantityInCampaign2, 2)
        self.assertEqual(userQuantityInCampaign3, 3)

    # Testeamos retornamos una lista con todos los usuarios para una lista de tweets dada:
    def test_getUsersList(self):  # OK
        usersListForTweetsInCampaign1 = (self.reporter.getUsersList(base.tweetsRawCampaign1))
        usersListForTweetsInCampaign2 = (self.reporter.getUsersList(base.tweetsRawCampaign2))
        usersListForTweetsInCampaign3 = (self.reporter.getUsersList(base.tweetsRawCampaign3))

        expectedUsersForCampaign1 = ['uno', 'dos', 'tres']
        expectedUsersForCampaign2 = ['cuatro', 'uno']
        expectedUsersForCampaign3 = ['cuatro', 'cinco', 'seis']

        self.assertElementsInList(usersListForTweetsInCampaign1, expectedUsersForCampaign1)
        self.assertElementsInList(usersListForTweetsInCampaign2, expectedUsersForCampaign2)
        self.assertElementsInList(usersListForTweetsInCampaign3, expectedUsersForCampaign3)

    def assertElementsInList(self, actualList, expectedElementsList):
        for expectedUser in expectedElementsList:
            assert expectedUser in actualList
