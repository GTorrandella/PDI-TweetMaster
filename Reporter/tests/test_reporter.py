from Campaign.Campaign import Campaign as Campaign
from Manager.manager import Manager as Manager
from Reporter.Reporter import Reporter as Reporter
from Tweet.Tweet import Tweet as Tweet
import unittest

class test_reporter(unittest.TestCase):
	"""Hardcodeanding"""
	"""tweets diccionario"""
	tweet1 = {
        "id_str" : "123456",
        "user" : {"name" : "NASAOk", "id_str" : "789456"},
        "entities" : {"hashtags" : ["#mars","#venus","#earth"],"user_mentions" : ["@NASA", "@planets"]},
        "created_at" : "Sun Mar 20 15:11:01 +0000 2018",
    }
	tweet2 = {
		"id_str" : "112112",
		"user" : {"name" : "MiauricioOK", "id_str" : "451325"},
		"entities" : {"hashtags" : ["#DonaldNoMeDejes"], "user_mentions" : ["@donaldTrump", "@G20"]},
		"created_at" : "Sun Mar 20 21:08:01 +0000 2018",}	
	"""Objetos Tweet"""
	T1=Tweet(tweet1)
	T2=Tweet(tweet2)
	"""Tweet().to_json()"""
	t1=T1.to_json()
	t2=T2.to_json()
	"""lista de Tweet().to_json()"""
	tweets = [t1,t2]	#esto me llega de Connector().returnTweetsbyIDC(idC)
	"""c: diccionario / campaign:objeto"""
	c = {"id":"1234", "email":"donaldTrump@gmail.com","hashtags": ["#donaldTrump", "#G20"], "mentions": ["@donaldTrump", "@miauricioOK"], "startDate":"28 11 2018 18:02:00", "finDate":"02 12 2018 19:26:22"}
	campaign = Campaign(c["id"], c["email"], c["hashtags"], c["mentions"], c["startDate"], c["finDate"])

	def getCampaign_test(self, c, campaign):
		#c_dict = Connector.retornarCampaignBD(idC)	#Traer campaña de la BD (diccionario)
		cCreated= Campaign(c["id"], c["email"], c["hashtags"], c["mentions"], c["startDate"], c["finDate"])
		self.assertIsInstance(cCreated,Campaign)
		self.assertEqual(campaign,cCreated)
	
if __name__ == '__main__':
    unittest.main()