'''
Created on Nov 20, 2018

@author: Gabriel Torrandella
'''
from twython import Twython

APP_KEY = "7zCU1BgDeQ3G65MfwvpNUZm3a"
APP_SECRET = "0Kii63THccgKCKMvE396GgaieUld5HtADLeU98wJmlpiWzfP47"
ACCESS_TOKEN = "AAAAAAAAAAAAAAAAAAAAAHqS8wAAAAAAC%2FBQkp9ZMJ3igj1orr2ou%2BBzQKM%3DgodQO6bVl2TLlhjPZCm1hT2MbwTwXIdJj5Upc9oCPWE3mjBYIK"


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
                tweets.append(tweet.to_json())
        return tweets
            
    def fetchTweets(self, campaign, lastId):
        rawTweets = []
        
        for hashtag in campaign.get_hastags():
            rawTweets.append(self.fetchByHashtag(hashtag, lastId))
            
        for mention in campaign.get_mentions():
            rawTweets.append(self.fetchByMention(mention, lastId))
               
        return self.makeTweet(rawTweets)