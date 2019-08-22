'''
Created on Jul 5, 2019

@author: Gabriel Torrandella
'''
from Fetcher.fetcher import Fetcher
from Logger.Rsyslog import createLogger
from Campaign.Campaign import Campaign
import pika
import json
from time import sleep


class fetcherConsumer():
    
    def __init__(self, context='standar'):
        if context=='test':
            self.log = createLogger(context='test_outside', name="Fetcher.fetcher_consumer")
            self.fetcher = Fetcher(context='test')
        else:
            self.log = createLogger(name="Fetcher.fetcher_consumer")
            self.fetcher = Fetcher()
        
        self.log.info('Fetcher service started')
        self.context = context

    def open_connection(self):
        
        try:
            if self.context == 'test':
                self.connection = pika.BlockingConnection(
                    pika.ConnectionParameters(host='localhost', heartbeat=5))
                self.channel = self.connection.channel()
            else:
                self.connection = pika.BlockingConnection(
                    pika.ConnectionParameters(host='rabbitTweetMaster', heartbeat=5))
                self.channel = self.connection.channel()
            
            self.channel.exchange_declare(exchange="fetcher", exchange_type="direct", durable=True)
            self.channel.queue_declare(queue="campaign")
            self.channel.queue_bind(queue='campaign', exchange='fetcher', routing_key='fetcher.campaign')
            self.log.info('Connection with queue ready')
            return True
            
        except:
            return False
        
    def callback(self, channel, method, properties, body):
        self.log.info('Message recived')
        
        campaignData = json.loads(body.decode())
        campaign = Campaign(campaignData['id'],
                            campaignData['email'],
                            campaignData['hashtags'],
                            campaignData['mentions'],
                            campaignData['startDate'],
                            campaignData['finDate'])
        try:
            self.fetcher.fetchTweets(campaign)
        except:
            self.log.info('Falied fetch for '+str(campaign.idC))
        self.channel.basic_ack(delivery_tag = method.delivery_tag)
    
    
    def close_connection(self):
        self.log.info('Exiting Fetcher service')
        self.channel.close()
        self.connection.close()
        self.log.info('Fetcher service exited without problems')
    
    def consume(self):
        self.log.info('Starting to consume')
        self.channel.basic_consume(queue='campaign', on_message_callback=self.callback)
        self.channel.start_consuming()
        
    def stop_consuming(self):
        self.log.info('Stoping the consuming')
        self.channel.stop_consuming()


if __name__ == "__main__":
    consumer = fetcherConsumer()
    
    while(not consumer.open_connection()):
        sleep(0.5)
    
    print(' [*] Waiting for messages. To exit press CTRL+C')
    try:
        consumer.consume()
    except KeyboardInterrupt:
        consumer.stop_consuming()
    consumer.close_connection()