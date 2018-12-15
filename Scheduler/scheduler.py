'''
Created on Dec 10, 2018

@author: Gabriel Torrandella
'''
from DataBseConnector.Connector import returnCampaingsInProgress
from Manager.manager import Manager
from _datetime import datetime

class Scheduler():
    
    def getTime(self):
        return datetime.now().strftime("%d %m %Y %X")
    
    def getCampaings(self, date):
        return returnCampaingsInProgress(date)
    
    def wakeManager(self, campaigns):
        Manager.fetchCampaings(campaigns)
        
    def keepSchedule(self):
        date = self.getTime()
        camps = self.getCampaings(date)
        if not len(camps) == 0:
            self.wakeManager(camps)

Scheduler.keepSchedule()