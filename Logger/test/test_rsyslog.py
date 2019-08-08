'''
Created on Jul 4, 2019

@author: Gabriel Torrandella
'''
import unittest
from os import remove
import Logger.Rsyslog

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        remove('test.log')

    def test_BaseLoggin(self):
        log = Logger.Rsyslog.createLogger(context='test')
        log.debug('1st')
        log.info('2nd')
        log.warning('3rd')
        log.error('4th')
        log.critical('5th')
        
        log_file = open('test.log')
        
        self.assertEqual(log_file.readline(), "Logger.Rsyslog - <FechaYHora>: INFO: 2nd, from test_BaseLoggin\n")
        self.assertEqual(log_file.readline(), "Logger.Rsyslog - <FechaYHora>: WARNING: 3rd, from test_BaseLoggin\n")
        self.assertEqual(log_file.readline(), "Logger.Rsyslog - <FechaYHora>: ERROR: 4th, from test_BaseLoggin\n")
        self.assertEqual(log_file.readline(), "Logger.Rsyslog - <FechaYHora>: CRITICAL: 5th, from test_BaseLoggin\n")
        
        log_file.close()
        
    def test_DiferentLevelLoggin(self):
        log = Logger.Rsyslog.createLogger(level='ERROR', context='test')
        log.debug('1st')
        log.info('2nd')
        log.warning('3rd')
        log.error('4th')
        log.critical('5th')
        
        log_file = open('test.log')
        
        self.assertEqual(log_file.readline(), "Logger.Rsyslog - <FechaYHora>: ERROR: 4th, from test_DiferentLevelLoggin\n")
        self.assertEqual(log_file.readline(), "Logger.Rsyslog - <FechaYHora>: CRITICAL: 5th, from test_DiferentLevelLoggin\n")
        
        log_file.close()
    
    def test_NoLoggin(self):
        log = Logger.Rsyslog.createLogger(context='test')
        log.debug('1st')
        
        log_file = open('test.log')
        
        self.assertEqual(log_file.readline(), '')
        
        log_file.close()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()