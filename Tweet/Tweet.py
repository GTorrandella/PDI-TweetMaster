import json

class Tweet(object):
    '''classdocs'''
    def __init__(self, tweet):
        ''' Constructor '''
        self.ID = tweet['id_str']
        user = tweet['user'];
        entities = tweet['entities'] #diccionario con 2 listas (hashtags y mentions)
        self.userName = user['name']
        self.userID = user['id_str']
        
        if type(entities['hashtags']) == dict:
            self.hashtags = []
            for d in entities['hashtags']:
                self.hashtags.append('#'+d['text'])
        else:
            self.hashtags = entities['hashtags']
            
        if type(entities['user_mentions']) == dict:
            self.mentions = []
            for d in entities['user_mentions']:
                self.mentions.append('@'+d['screen_name'])
        else:
            self.mentions = entities['user_mentions']
                
        self.date = tweet['created_at']
        #Sun Mar 20 21:08:01 2018"


    def to_json(self):
        dictionary = {
            "id_str" : self.ID,
            "user" : {"name" : self.userName, "id_str" : self.userID},
            "entities" : {"hashtags" : self.hashtags,
            "user_mentions" : self.mentions},
            "created_at" : str(self.date)
        }
        tweet_json = json.dumps(dictionary) 
        return tweet_json
