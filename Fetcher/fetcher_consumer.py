'''
Created on Jul 5, 2019

@author: Gabriel Torrandella
'''
from Fetcher.fetcher import Fetcher
from Logger.Rsyslog import createLogger
import pika

def start_connection():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', heartbeat=5))
    channel = connection.channel()
    channel.exchange_declare('fetcher', exchange_type="direct")

def callback():
    pass

def close_connection():
    pass

def consume():
    pass

if __name__ == '__main__':
    pass