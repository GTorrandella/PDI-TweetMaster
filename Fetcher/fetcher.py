'''
Created on Nov 20, 2018

@author: Gabriel Torrandella
'''

import twitter
import Tweet

class Fetcher():
    api = twitter.Api()
    
    def fetchByHashtag(self, hashtag, lastId):
        rawTweet = []
        return rawTweet
    
    def fetchByMention(self, mention, lastId):
        rawTweet = []
        return rawTweet
    
    def makeTweet(self, tweetContent):
        return Tweet.Tweet(tweetContent)
    
    def fetchTweets(self, campaign, lastId):
        rawTweets = []
        hashtags = campaign.get_hastags() #Separate hashtags from campaign
        mentions = campaign.get_mentions()#Separate metions from campaign
        
        for hashtag in hashtags:
            rawTweets.append(self.fetchByHashtag(hashtag, lastId))
        for mention in mentions:
            rawTweets.append(self.fetchByMention(mention, lastId))
            
        tweets = []
        for tweetContent in rawTweets:
            tweets.add(self.makeTweet(tweetContent))
            
        return tweets