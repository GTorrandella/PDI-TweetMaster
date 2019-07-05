'''
Created on Jul 4, 2019

@author: Gabriel Torrandella
'''
import logging
import logging.handlers

def createLogger(level='INFO', context='standar', name=__name__):
    """
    create logging object with logging to RSYSLOG
    :param level Logging log level, default INFO
    :return: logging object
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    if context == 'test':
        handler = logging.FileHandler('test.log')
        formater = logging.Formatter(fmt='%(name)s - <FechaYHora>: %(levelname)s: %(message)s, from %(funcName)s')
    else:
        handler = logging.handlers.SysLogHandler(address=('rsyslog',514))
        formater = logging.Formatter(fmt='%(name)s - %(asctime)s: %(levelname)s: %(message)s, from %(funcName)s', datefmt='%Y-%m-%d %H:%M:%S')
            
    handler.setLevel('INFO')
    handler.setFormatter(formater)
    logger.addHandler(handler)            
    
    return logger