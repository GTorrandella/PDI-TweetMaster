'''
Created on Jul 6, 2019

@author: Gabriel Torrandella
'''
from DataBaseConnector.Connector import Connector
from Logger.Rsyslog import createLogger
import pika

def start_connection(context='standar'):
    
    if context == 'test':
        log = createLogger(context='test_outside', name='Scheduler')
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost', heartbeat=5))
        connector = Connector(context='test')
    else:
        log = createLogger(name='Scheduler')
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='rabbitTweetMaster', heartbeat=5))
        connector = Connector()

    channel = connection.channel()
    channel.exchange_declare(exchange="fetcher", exchange_type="direct", durable=True)
    log.info("Connection to RabbitMQ ready")
    
    try:
        campaignsOnProgress = connector.selectCampaignsInProgress()
        log.info("Recived Campaigns on progress")
        
        for campaign in campaignsOnProgress:
            channel.basic_publish(exchange='fetcher', routing_key='fetcher.campaign', body=campaign.to_json())
            
    except:
        log.error("Failed to get Campaigns on progress")

    channel.close()
    connection.close()
    log.info("Exited successfully")
    
if __name__ == '__main__':
    start_connection()