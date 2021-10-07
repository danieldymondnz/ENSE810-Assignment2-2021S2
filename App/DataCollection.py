from sense_emu import SenseHat

import Controller

class DataCollection(object):
    __maxTemp = 6
    __minTemp = 2
    __maxRH = 85
    __minRH = 65
    __maxSpeed = 80
    __maxAccel = 1.5
    
    def __init__(self, senseHAT, dataQueue):
        self._senseHAT = SenseHat()

        self.__dataQueue = None
        self.__temps = ()
        self.__RHs = ()
        self.__speeds = ()
        self.__accels = ()
        pass
        
    def run(self):
        pass
        
    def terminate(self):
        pass
        
    @staticmethod
    def __generateFlags(temp, relHumidity, speed):
        tempFlag = false
        RHFlag = false
        speedFlag = false
        accelFlag = false
        pass
        
    @staticmethod
    def __calculateAverage(values):
        pass
        
    
