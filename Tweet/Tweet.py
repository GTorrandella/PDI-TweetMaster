import json
from datetime import datetime

class Tweet(object):
    '''classdocs'''
    def __init__(self, tweet):
        ''' Constructor '''
        self.ID = tweet['id_str']
        user = tweet['user'];
        entities = tweet['entities'] #diccionario con 2 listas (hashtags y mentions)
        self.userName = user['name']
        self.userID = user['id_str']
        self.hashtags = entities['hashtags']
        self.mentions = entities['user_mentions']
        Ymd, Xz = tweet['created_at'].split(' ')
        Y,m,d = Ymd.split('-')
        X = Xz[:8]
        z = Xz[8:].replace(':','')
        self.date = datetime.strptime(Y+" "+m+" "+d+" "+X+" "+z, "%Y %m %d %X %z")
        #Sun Mar 20 21:08:01 2018"
        '2018-12-28 22:07:42+00:00'


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
