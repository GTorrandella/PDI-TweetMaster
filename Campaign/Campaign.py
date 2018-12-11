from datetime import date
from _datetime import date
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

    def get_idC(self):
        return self.__idC

    def get_emailDueño(self):
        return self.__emailDueño

    def get_hashtags(self):
        return self.__hashtags

    def get_mentions(self):
        return self.__mentions

    def get_start_date(self):
        return self.__startDate

    def get_fin_date(self):
        return self.__finDate

    def set_idC(self, value):
        self.__idC = value

    def set_emailDueño(self, value):
        self.__emailDueño = value

    def set_hashtags(self, value):
        self.__hashtags = value

    def set_mentions(self, value):
        self.__mentions = value

    def set_start_date(self, value):
        self.__startDate = value

    def set_fin_date(self, value):
        self.__finDate = value

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
    
    idC = property(get_idC, set_idC, "idC's docstring")
    emailDueño = property(get_emailDueño, set_emailDueño, "emailDueño's docstring")
    hashtags = property(get_hashtags, set_hashtags, "hashtags's docstring")
    mentions = property(get_mentions, set_mentions, "mentions's docstring")
    startDate = property(get_start_date, set_start_date, "startDate's docstring")
    finDate = property(get_fin_date, set_fin_date, "finDate's docstring")
        
    