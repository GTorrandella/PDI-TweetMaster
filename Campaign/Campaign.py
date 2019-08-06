from datetime import datetime
from _datetime import datetime
import json

DATE_FORMAT_STR = "%d %m %Y %X"  # yyyy-mm-dd hh:mm:ss


class Campaign(object):

    def __init__(self, idC, emailDueño, hashtags, mentions, startDate, finDate):
        '''  Constructor '''
        self.idC = idC
        self.emailDueño = emailDueño
        self.hashtags = hashtags
        self.mentions = mentions

        if type(startDate) == str:
            self.startDate = datetime.strptime(startDate, DATE_FORMAT_STR)
        else:
            self.startDate = startDate

        if type(finDate) == str:
            self.finDate = datetime.strptime(finDate, DATE_FORMAT_STR)
        else:
            self.finDate = finDate

    def to_json(self):
        dictionary = self.to_dict()  # Llamamos a la funcion de abajo
        camp_json = json.dumps(dictionary)
        return camp_json

    def to_dict(self):
        dictionary = {
            'id': self.idC,
            'email': self.emailDueño,
            'hashtags': self.hashtags,
            'mentions': self.mentions,
            'startDate': datetime.strftime(self.startDate, DATE_FORMAT_STR),
            'finDate': datetime.strftime(self.finDate, DATE_FORMAT_STR)
        }
        return dictionary

    def isActive(self):  # OK
        if (datetime.now() > self.startDate) and (datetime.now() < self.finDate):
            return True
        return False

    def isFinished(self):  # OK
        if datetime.now() > self.finDate:
            return True
        return False

    def __repr__(self):
        return "<idC:%s emailDueño:%s hashtags:%s mentions:%s startDate:%s finDate:%s> " % (
            self.idC, self.emailDueño, self.hashtags, self.mentions, self.startDate, self.finDate)
