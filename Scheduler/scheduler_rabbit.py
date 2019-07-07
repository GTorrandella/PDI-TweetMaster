'''
Created on Jul 6, 2019

@author: Gabriel Torrandella
'''
from DataBaseConnector import Connector
import pika

def start_connection(context='standar'):
    if context == 'test':
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost', heartbeat=5))
    else:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='rabbitTweetMaster', heartbeat=5))
    channel = connection.channel()
    channel.exchange_declare(exchange="fetcher", exchange_type="direct", durable=True)

if __name__ == '__main__':
    pass