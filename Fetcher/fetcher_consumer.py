'''
Created on Jul 5, 2019

@author: Gabriel Torrandella
'''
from Fetcher.fetcher import Fetcher
from Logger.Rsyslog import createLogger
import pika

log = createLogger(context='test_outside', name="Fetcher.fetcher_consumer")
fetcher = Fetcher(context='test')
log.info('Fetcher service started')
    
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', heartbeat=5))
channel = connection.channel()
channel.queue_declare(queue="TweetQueue")
log.info('Connection with queue ready')        
        
def callback(channel, method, properties, body):
    log.info('Message recived')
    CampaignsInProgress = body
    for campaign in CampaignsInProgress:
        try:
            fetcher.fetchTweets(campaign)
        except:
            log.info('Falied fetch for '+campaign.idC)        
    channel.basic_ack(delivery_tag = method.delivery_tag)


def close_connection():
    log.info('Exiting Fetcher service')
    channel.close()
    connection.close()
    log.info('Fetcher service exited without problems')

def consume():
    log.info('Starting to consume')
    channel.basic_consume(queue='TweetQueue', on_message_callback=callback)
    
def stop_consuming():
    log.info('Stoping the consuming')
    channel.stop_consuming()

print(' [*] Waiting for messages. To exit press CTRL+C')

consume()

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
connection.close()