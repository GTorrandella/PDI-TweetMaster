'''
Created on Jul 11, 2019

@author: Gabriel Torrandella
'''
from io import BytesIO
from rdbtools import RdbParser, JSONCallback
import json
from Tweet.Tweet import Tweet
from DataBaseConnector import Connector

def get_campaign_ids(RedisKeys):
    campaignIDs = []
    for key in RedisKeys:
        if ':tweets' in key:
            campaignIDs.append(key)
    return campaignIDs

def make_tweet(tweetID, RedisData):
    tweetDict = {
        'id_str': tweetID,
        'text':'lala',#RedisData[tweetID]['text'],
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

def parse_redisRDB():
    B = BytesIO()
    parser = RdbParser(JSONCallback(out=B))
    parser.parse('/media/gabo/Puente/Programación/eclipse-workspace/PDI-TweetMaster/Fetcher/dump.rdb')
    return json.loads(B.getvalue().decode())[0]

def save_to_database(RedisData):
    RedisKeys = RedisData.keys()
    campaignIDs = get_campaign_ids(RedisKeys)
    for campaignID in campaignIDs:
        for tweetID in RedisData[campaignID]:
            Connector.insertTweet(make_tweet(tweetID, RedisData), campaignID)
        
        