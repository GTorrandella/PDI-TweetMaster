import schedule
import time
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from Manager.manager import Manager

def job():
    Manager().fetchCampaings()

schedule.every(5).minutes.do(job)

while True:
    schedule.run_all()
    #time.sleep(1)
