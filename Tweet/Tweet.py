import json
from datetime import datetime

DATE_FORMAT_STR = "%Y-%m-%d %X"
DATE_FORMAT_TWITTER = "%a %b %d %X %z %Y"

class Tweet(object):
    '''classdocs'''
    def __init__(self, tweet, raw=False):
        ''' Constructor '''
        if raw:
            self._rawConstrucctor(tweet)
        else:
            self._nonRawConstrucctor(tweet)
    
    def _rawConstrucctor(self, tweet):
        self.ID = tweet['id_str']
        self.text = tweet['text']
        self.hashtags = tweet['entities']['hashtags']
        self.mentions = tweet['entities']['user_mentions']
        self.userID = tweet['user']['id_str']
        self.userName = tweet['user']['name']
        self.date = datetime.strptime(tweet['created_at'], DATE_FORMAT_TWITTER)

    def _nonRawConstrucctor(self, tweet):
        self.ID = tweet['id_str']
        user = tweet['user']
        entities = tweet['entities'] #diccionario con 2 listas (hashtags y mentions)
        self.userName = user['name']
        self.userID = user['id_str']
        
        self.hashtags = []
        if type(entities['hashtags']) == dict:
            self.hashtags.append('#'+entities['hashtags']['text'])
        else:
            for d in entities['hashtags']:
                if type(d) == dict:
                    self.hashtags.append('#'+d['text'])
                else:
                    self.hashtags.append(d)
        
        self.mentions = []
        if type(entities['user_mentions']) == dict:
            self.mentions.append('@'+entities['user_mentions']['screen_name'])
        else:
            if type(entities['user_mentions']) == list:
                for d in entities['user_mentions']:
                    if type(d) == dict:
                        self.mentions.append('@'+d['screen_name'])
                    else:
                        self.mentions.append(d)
                        
        self.date = datetime.strptime(tweet['created_at'], DATE_FORMAT_STR)
        #Sun Mar 20 21:08:01 2018"
        
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.ID == other.ID and self.userID == other.userID and self.text == self.text and self.userName == self.userName and self.hashtags == other.hashtags and self.mentions == other.mentions
        return False
    
    def to_json(self):
        dictionary = {
            "id_str" : self.ID,
            "name" : self.userName,
            "user_id_str" : self.userID,
            "hashtags" : self.hashtags,
            "user_mentions" : self.mentions,
            "created_at" : datetime.strftime(self.date, DATE_FORMAT_STR),
            "text": self.text
        }
        tweet_json = json.dumps(dictionary) 
        return tweet_json
    
    def to_dict(self):
        dictionary = {
            "id_str" : self.ID,
            "name" : self.userName,
            "user_id_str" : self.userID,
            "hashtags" : self.hashtags,
            "user_mentions" : self.mentions,
            "created_at" : datetime.strftime(self.date, DATE_FORMAT_STR),
            "text" : self.text
        }
        return dictionary
