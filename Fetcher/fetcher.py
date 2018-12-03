'''
Created on Nov 20, 2018

@author: Gabriel Torrandella
'''
import Tweet
from twython import Twython

APP_KEY = "7zCU1BgDeQ3G65MfwvpNUZm3a"
APP_SECRET = "0Kii63THccgKCKMvE396GgaieUld5HtADLeU98wJmlpiWzfP47"
ACCESS_TOKEN = "AAAAAAAAAAAAAAAAAAAAAHqS8wAAAAAAC%2FBQkp9ZMJ3igj1orr2ou%2BBzQKM%3DgodQO6bVl2TLlhjPZCm1hT2MbwTwXIdJj5Upc9oCPWE3mjBYIK"


class Fetcher():
    twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
    twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
    
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