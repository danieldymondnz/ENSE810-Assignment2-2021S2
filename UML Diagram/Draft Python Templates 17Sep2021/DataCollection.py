
import Controller

class DataCollection(object):
    __maxTemp = None
    __minTemp = None
    __maxRH = None
    __minRH = None
    __maxSpeed = None
    def __init__(self, senseHAT, dataQueue):
        self._senseHAT = None
        self.__dataQueue = None
        self.__temps = ()
        self.__RHs = ()
        self.__speeds = ()
        self.__accels = ()
        self. = None
        pass
        
    def run(self):
        pass
        
    def terminate(self):
        pass
        
    @staticmethod
    def __generateFlags(temp, relHumidity, speed):
        pass
        
    @staticmethod
    def __calculateAverage(values):
        pass
        
    
