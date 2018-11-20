'''
Created on Nov 20, 2018

@author: gabo
'''
from _datetime import date


class Campaign(object):
    '''
    classdocs
    '''


    def __init__(self, idAutor, hashtags, mentions, startDate, finDate):
        '''
        Constructor
        '''
        self.autor = idAutor
        self.hastags = hashtags
        self.mentions = mentions
        self.startDate = date(startDate)
        self.finDate = date(finDate)

    def get_autor(self):
        return self.__autor


    def get_hastags(self):
        return self.__hastags


    def get_mentions(self):
        return self.__mentions


    def get_start_date(self):
        return self.__startDate


    def get_fin_date(self):
        return self.__finDate


    def set_autor(self, value):
        self.__autor = value


    def set_hastags(self, value):
        self.__hastags = value


    def set_mentions(self, value):
        self.__mentions = value


    def set_start_date(self, value):
        self.__startDate = value


    def set_fin_date(self, value):
        self.__finDate = value
        
    autor = property(get_autor, set_autor, "autor's docstring")
    hastags = property(get_hastags, set_hastags, "hastags's docstring")
    mentions = property(get_mentions, set_mentions, "mentions's docstring")
    startDate = property(get_start_date, set_start_date, "startDate's docstring")
    finDate = property(get_fin_date, set_fin_date, "finDate's docstring")
        
    