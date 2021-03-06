'''
Created on Nov 20, 2018

@author: Gabriel Torrandella
'''
from os import path
from twython import Twython
from Tweet.Tweet import Tweet
from Logger.Rsyslog import createLogger

import redis

parentDir = path.dirname(path.abspath(__file__))
tokenPath = path.join(parentDir, 'tokens')
f = open(tokenPath)
APP_KEY = f.readline()
APP_SECRET = f.readline()
ACCESS_TOKEN = f.readline().rstrip()
f.close

class Fetcher():
    _twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
    _twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
    
    def __init__(self, context = "standar"):
        if context == "test":
            self.log = createLogger(context='test_outside', name=__name__)
            self._db = redis.from_url("redis://localhost:6379", db = 0)
        else:
            self.log = createLogger(name=__name__)
            self._db = redis.from_url("redis://redisfetcher:6379", db = 0)
    
    
    def fetchByHashtag(self, hashtag):
        rawTweet = self._twitter.cursor(self._twitter.search, q=hashtag, result_type="recent")
        return rawTweet
    
    def fetchByMention(self, mention):
        rawTweet = self._twitter.cursor(self._twitter.search, q=mention, result_type="recent")
        return rawTweet
    
    def makeTweet(self, rawTweets):
        tweets = []
        for tweet in rawTweets:
            tweets.append(Tweet(tweet, raw=True))
        return tweets
            
    def fetchTweets(self, campaign):
        self.log.info("Fetching for "+str(campaign.idC))
        rawTweets = []
        
        for hashtag in campaign.hashtags:
            rawTweets = rawTweets + self.fetchByHashtag(hashtag)
            
        for mention in campaign.mentions:
            rawTweets = rawTweets + self.fetchByMention(mention)
            
        self.log.info("Finished fetching "+str(campaign.idC))
        tweets = self.makeTweet(rawTweets)
        
        self.saveTweets(campaign.idC, tweets)
    
    def saveTweets(self, idCampain, tweets):
        self.log.info("Saving to DB "+str(idCampain))
        try:
            for tweet in tweets:
                tweet = tweet.to_dict()
                self._db.sadd(idCampain+":tweets", tweet['id_str'])           
                self._db.hset(tweet['id_str'], 'name', tweet['name'])         
                self._db.hset(tweet['id_str'], 'user_id_str', tweet['user_id_str'])         
                self._db.hset(tweet['id_str'], 'created_at', tweet['created_at'])
                self._db.hset(tweet['id_str'], 'text', tweet['text'])
                
                for hashtag in tweet['hashtags']:
                    self._db.sadd(tweet['id_str']+":hastags", hashtag)
                for ment in tweet['user_mentions']:
                    self._db.sadd(tweet['id_str']+":mentions", ment)
        except:
            self.log.error("Failed to save for " + str(idCampain))