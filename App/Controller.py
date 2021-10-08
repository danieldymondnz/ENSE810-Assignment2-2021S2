from sense_emu import SenseHat
import threading
import time
import queue

import MatrixDriver
import DataCollection
import DBAgent

class Controller(object):
    def __init__(self):
        
        threading.Thread.__init__(self)
        
        self._matrixDriver = MatrixDriver
        self._dataCollection = DataCollection
        self.dataQueue = dataQueue
        self.flushQueue = flushQueue
        self._senseHAT = SenseHat()
        self.dbDataQueue = dbDataQueue
        
        self.__dataUseDict = {}
        
        self.isRunning = True
        
    def run(self):
        while self.isRunning:
            # collect data
            if DataCollection._DCDataQueue.qsize() > 0:
                self.__dataUseDict = self._DCDataQueue.get_nowait()
            
            # display data
            MatrixDriver._displayGraph(_senseHAT, dataUseDict["TEMPERATURE"], dataUseDict["HUMIDITY"])
            if dataUseDict["WARN_ACCELERATION"]:
                MatrixDriver._displayAccelerationWarning(self, _senseHAT, dataUseDict["ACCELERATION"])
            if dataUseDict["WARN_HUMIDITY"]:
                MatrixDriver._displayRHWarning(self, _senseHAT, dataUseDict["HUMIDITY"])
            if dataUseDict["WARN_SPEED"]:
                MatrixDriver._displaySpeedWarning(self, _senseHAT, dataUseDict["SPEED"])
            if dataUseDriver["WARN_TEMPERATURE"]:
                MatrixDriver._displayTempWarning(self, _senseHAT, dataUseDict["TEMPERATURE"])

            # transfer data to DBAgent
            
        
    def terminate(self):
        self.isRunning = False
        
    def _flushQueue(self):
        pass
        
    
