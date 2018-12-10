'''
Created on Nov 20, 2018

@author: Gabriel Torrandella
'''
import json

class Tweet(object):
    '''
    classdocs
    '''

    def __init__(self, tweet):
        '''
        Constructor
        '''
        self.ID = tweet["id_str"];
        user = tweet["user"];
        entities = tweet["entities"]
        self.userID = user["id_str"]
        self.userName = user["name"]
        self.userID = tweet["id_str"];
        self.hashtags = entities["hashtags"]
        self.mentions = entities["user_mentions"]

    def get_id(self):
        return self.__ID


    def get_user(self):
        return self.__user


    def get_user_id(self):
        return self.__userID


    def get_hashtags(self):
        return self.__hashtags


    def get_mentions(self):
        return self.__mentions


    def get_text(self):
        return self.__text


    def set_id(self, value):
        self.__ID = value


    def set_user(self, value):
        self.__user = value


    def set_user_id(self, value):
        self.__userID = value


    def set_hashtags(self, value):
        self.__hashtags = value


    def set_mentions(self, value):
        self.__mentions = value


    def set_text(self, value):
        self.__text = value


    def del_id(self):
        del self.__ID


    def del_user(self):
        del self.__user


    def del_user_id(self):
        del self.__userID


    def del_hashtags(self):
        del self.__hashtags


    def del_mentions(self):
        del self.__mentions


    def del_text(self):
        del self.__text


    def to_json(self):
        dictionary = {
            "id" : self.__ID,
            "email" : self.__user,
            "hastags" : self.__userID,
            "mentions" : self.__hashtags,
            "startDate" : self.__mentions,
            "finDate" : self.__text,
        }
        tweet_json = json.dumps(dictionary) 
        return tweet_json

    ID = property(get_id, set_id, del_id, "ID's docstring")
    user = property(get_user, set_user, del_user, "user's docstring")
    userID = property(get_user_id, set_user_id, del_user_id, "userID's docstring")
    hashtags = property(get_hashtags, set_hashtags, del_hashtags, "hashtags's docstring")
    mentions = property(get_mentions, set_mentions, del_mentions, "mentions's docstring")
    text = property(get_text, set_text, del_text, "text's docstring")
