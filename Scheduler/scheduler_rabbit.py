'''
Created on Jul 6, 2019

@author: Gabriel Torrandella
'''
#from DataBaseConnector import Connector
from Campaign.Campaign import Campaign
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
    
    c = Campaign("idC", "emailDueño", ["#mars"], ["@mars"], "2018-12-6 23:20:00", "2018-12-7 00:00:30")
    
    channel.basic_publish(exchange='fetcher', routing_key='fetcher.campaign', body=c.to_json())
    print(" [x] Sent Campaign")


if __name__ == '__main__':
    start_connection(context='test')