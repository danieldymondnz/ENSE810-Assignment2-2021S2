from sense_emu import SenseHat
import threading
import time

import MatrixDriver
import DataCollection
import DBAgent
import WiFiAgent

class Controller(object):
    def __init__(self):
        
        threading.Thread.__init__(self)
        
        self._matrixDriver = MatrixDriver
        self._dataCollection = DataCollection
        self.dataQueue = dataQueue
        self.flushQueue = flushQueue
        self._senseHAT = SenseHat()
        self.dbDataQueue = dbDataQueue
        
        self.isRunning = True
        
    def run(self):
        while self.isRunning:
            # collect data
            # generate flags
            
            # display data
            # transfer data to DBAgent
            
            # kms
        
    def terminate(self):
        self.isRunning = False
        
    def _flushQueue(self):
        pass
        
    
