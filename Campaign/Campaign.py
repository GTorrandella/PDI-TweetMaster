'''
Created on Nov 20, 2018

@author: gabo
'''
from _datetime import date
import json

class Campaign(object):

    def __init__(self, idC, emailDueño, hashtags, mentions, startDate, finDate):
        '''  Constructor '''
        self.idC=idC
        self.emailDueño = emailDueño
        self.hastags = hashtags    
        self.mentions = mentions   
        self.startDate = date(startDate[0],startDate[1],startDate[2])
        self.finDate = date(finDate[0],finDate[1],finDate[2])


    def get_idC(self):
        return self.__idC

    def get_emailDueño(self):
        return self.__emailDueño

    def get_hastags(self):
        return self.__hastags

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

    def set_hastags(self, value):
        self.__hastags = value

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
            "hastags" : self.__hastags,
            "mentions" : self.__mentions,
            "startDate" : str(self.__startDate),
            "finDate" : str(self.__finDate),
        }
        camp_json = json.dumps(dictionary) 
        return camp_json

    idC = property(get_idC, set_idC, "idC's docstring")
    emailDueño = property(get_emailDueño, set_emailDueño, "emailDueño's docstring")
    hastags = property(get_hastags, set_hastags, "hastags's docstring")
    mentions = property(get_mentions, set_mentions, "mentions's docstring")
    startDate = property(get_start_date, set_start_date, "startDate's docstring")
    finDate = property(get_fin_date, set_fin_date, "finDate's docstring")
        
    