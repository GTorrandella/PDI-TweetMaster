'''
Created on Jul 11, 2019

@author: Gabriel Torrandella
'''
from io import BytesIO
from rdbtools import RdbParser, JSONCallback
import json
from Tweet.Tweet import Tweet
from DataBaseConnector.Connector import Connector
from Logger.Rsyslog import createLogger

DUMP_PATH = '/data/dump.rdb'

class Parser():
    
    def __init__(self, context='standar'):
        
        if context == 'test':
            self.connector = Connector(context='test')
            self.log = createLogger(context='test_outside', name='RedisParser')
            
        else:
            self.connector = Connector()
            self.log = createLogger(name='RedisParser')
        
        self.log.info("Starting service")
    
    def get_campaign_ids(self, RedisKeys):
        campaignIDs = []
        for key in RedisKeys:
            if ':tweets' in key:
                campaignIDs.append(key)
        return campaignIDs
    
    def make_tweet(self, tweetID, RedisData):
        tweetDict = {
            'id_str': int(tweetID),
            'text': RedisData[tweetID]['text'],
            'entities':{
                'hashtags':[],
                'user_mentions':[]
                },
            'user':{
                'id_str':RedisData[tweetID]['user_id_str'],
                'name':RedisData[tweetID]['name']
                },
            'created_at':RedisData[tweetID]['created_at']
            }
        try:
            tweetDict['entities']['hashtags'] = RedisData[tweetID+':hastags']
        except:
            pass
        try:
            tweetDict['entities']['user_mentions'] = RedisData[tweetID+':mentions']
        except:
            pass
        return Tweet(tweetDict)
    
    def parse_redisRDB(self):
        B = BytesIO()
        parser = RdbParser(JSONCallback(out=B))
        parser.parse(DUMP_PATH)
        self.log.info("Redis dump loaded")
        return json.loads(B.getvalue().decode())[0]
    
    def save_to_database(self):
        self.log.info("Starting MySQL transfer")
        
        try:
            RedisData = self.parse_redisRDB()
            RedisKeys = RedisData.keys()
            campaignIDs = self.get_campaign_ids(RedisKeys)
            for campaignID in campaignIDs:
                for tweetID in RedisData[campaignID]:
                    realCampaignID = int(campaignID.split(':')[0])
                    self.connector.insertTweet(self.make_tweet(tweetID, RedisData), realCampaignID)
        
        except:
            self.log.error("Failed transfer to MySQL")
        
if __name__ == '__main__':
    Parser().save_to_database()
        
