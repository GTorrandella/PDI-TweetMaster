'''
Created on Nov 20, 2018

@author: Gabriel Torrandella
'''

import twitter

class Fetcher():
    api = twitter.Api()
    
    def fetchByHashtag(self, hashtag, lastId):
        rawTweet = []
        return rawTweet
    
    def fetchByMention(self, hashtag, lastId):
        rawTweet = []
        return rawTweet
    
    def fetchTweets(self, campaign, lastId):
        tweets = []
        #Separate hashtags from campaign
        #Separate metions from campaign
        #For each
            #Call the fetchers
        #Make the Tweet object list
        return tweets