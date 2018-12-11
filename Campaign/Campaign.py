from datetime import datetime
import json

class Campaign(object):

    def __init__(self, idC, emailDueño, hashtags, mentions, startDate, finDate):
        '''  Constructor '''
        self.idC=idC
        self.emailDueño = emailDueño
        self.hashtags = hashtags  
        self.mentions = mentions  
        self.startDate = datetime.strptime(startDate, "%d %m %Y %X") #dd mm yyyy hh:mm:ss
        self.finDate = datetime.strptime(finDate, "%d %m %Y %X") #dd mm yyyy hh:mm:ss

    def to_json(self):
        dictionary = {
            "id" : self.__idC,
            "email" : self.__emailDueño,
            "hashtags" : self.__hashtags,
            "mentions" : self.__mentions,
            "startDate" : str(self.__startDate),
            "finDate" : str(self.__finDate),
        }
        camp_json = json.dumps(dictionary) 
        return camp_json

    def __repr__(self):
        return "<idC:%s emailDueño:%s hashtags:%s mentions:%s startDate:%s finDate:%s> " % (self.idC, self.emailDueño, self.hashtags, self.mentions, self.startDate, self.finDate)
        
    