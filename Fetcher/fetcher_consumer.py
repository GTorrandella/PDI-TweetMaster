'''
Created on Jul 5, 2019

@author: Gabriel Torrandella
'''
from Fetcher.fetcher import Fetcher
from Logger.Rsyslog import createLogger
import pika


class fetcherConsumer():
    
    def __init__(self, context='standar'):
        if context=='test':
            self.log = createLogger(context='test_outside', name="Fetcher.fetcher_consumer")
            self.fetcher = Fetcher(context='test')
        else:
            self.log = createLogger(name="Fetcher.fetcher_consumer")
            self.fetcher = Fetcher()
        self.log.info('Fetcher service started')
        
    
    def start_connection(self, context='standar'):
        try:
            if context == 'test':
                self.connection = pika.BlockingConnection(
                    pika.ConnectionParameters(host='localhost', heartbeat=5))
            else:
                self.connection = pika.BlockingConnection(
                    pika.ConnectionParameters(host='rabbitTweetMaster', heartbeat=5))
            self.channel = self.connection.channel()
            self.channel.exchange_declare(exchange="fetcher", exchange_type="direct", durable=True)
            self.channel.queue_declare(queue="TweetQueue", durable=True)
            self.log.info('Connection with queue ready')
        except:
            self.log.error('Cannot connect with queue')
            
            
    def callback(self, channel, method, properties, body):
        self.log.info('Message recived')
        CampaignsInProgress = body
        for campaign in CampaignsInProgress:
            try:
                self.fetcher.fetchTweets(campaign)
            except:
                self.log.info('Falied fetch for '+campaign.idC)        
        self.channel.basic_ack()

    
    def close_connection(self):
        self.log.info('Exiting Fetcher service')
        self.channel.close()
        self.connection.close()
        self.log.info('Fetcher service exited without problems')
    
    def consume(self):
        self.log.info('Starting to consume')
        self.channel.basic_consume(queue='TweetQueue', on_message_callback=self.callback)
        
    def stop_consuming(self):
        self.log.info('Stoping the consuming')
        self.channel.stop_consuming()

if __name__ == '__main__':
    consumer = fetcherConsumer()
    consumer.start_connection()
    try:
        consumer.consume()
    except KeyboardInterrupt:
        consumer.stop_consuming()
    consumer.close_connection()