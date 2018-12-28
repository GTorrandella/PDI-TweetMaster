
from Manager.manager import Manager
from _datetime import datetime

class Scheduler():
    
    def wakeManager(self, campaigns):
        Manager.fetchCampaings(campaigns)
        
    def keepSchedule(self):
        camps = self.returnCampaignsInProgress()
        if not len(camps) == 0:
            self.wakeManager(camps)

Scheduler.keepSchedule()