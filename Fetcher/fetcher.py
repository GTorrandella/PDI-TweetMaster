'''
Created on Nov 20, 2018

@author: Gabriel Torrandella
'''
from Tweet import Tweet
from twython import Twython
from os import path

parentDir = path.dirname(path.abspath(__file__))
tokenPath = path.join(parentDir, 'tokens')
f = open(tokenPath)
APP_KEY = f.readline()
APP_SECRET = f.readline()
ACCESS_TOKEN = f.readline()
f.close

class Fetcher():
    twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
    twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
    
    def fetchByHashtag(self, hashtag, lastId):
        rawTweet = self.twitter.cursor(self.twitter.search, q=hashtag, result_type="recent", since_id=lastId)
        return rawTweet
    
    def fetchByMention(self, mention, lastId):
        rawTweet = self.twitter.cursor(self.twitter.search, q=mention, result_type="recent", since_id=lastId)
        return rawTweet
    
    def makeTweet(self, rawTweets):
        tweets = []
        for tweetContent in rawTweets:
            for tweet in tweetContent:
                tweets.append(Tweet(tweet).to_json())
        return tweets
            
    def fetchTweets(self, campaign, lastId):
        rawTweets = []
        
        for hashtag in campaign.get_hastags():
            rawTweets.append(self.fetchByHashtag(hashtag, lastId))
            
        for mention in campaign.get_mentions():
            rawTweets.append(self.fetchByMention(mention, lastId))
               
        return self.makeTweet(rawTweets)