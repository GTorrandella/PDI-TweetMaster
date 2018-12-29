'''
Created on Dec 29, 2018

@author: Gabriel Torrandella
'''
import sys
from os import path
from time import sleep 

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from Manager.manager import Manager

if __name__ == '__main__':
    while True:
        Manager().fetchCampaings()
        sleep(270)