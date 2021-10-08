'''
DataCollection
Data collection class which collects information from the senseHAT
and processes it as needed.
'''

from sense_emu import SenseHat
import threading
import time

import Controller

class DataCollection(object):
    
    def __init__(self, senseHAT, dataQueue):
        
        threading.Thread.__init__(self)

        self.__dataQueue = dataQueue[]
        self.__dataDict = {}
        
        self._senseHAT = SenseHat()
        self.__accelData = 0
        self.__accel = 0
        self.__humidity = 0
        self.__speed = 0
        self.__temp = 0
        
        self.__accFlag = False
        self.__humFlag = False
        self.__spdFlag = False
        self.__tempFlag = False
        
        self.__currentSpeed = 0
        self.__accelDirection = 'y'
        
        self.isRunning = True
        
        # define and set required value parameters
        __maxTemp = 6
        __minTemp = 2
        __maxRH = 85
        __minRH = 65
        __maxSpeed = 80
        __maxAccel = 1
        
    def run(self):
        while self.isRunning:
            # update current speed
            currentSpeed()
            
            # run loop adding data to lists
            accTempLst = []
            humTempLst []
            spdTempLst = []
            tempTempLst = []
            
            # collect data for 1 second
            for i in range(9):
                accTempLst.append(_senseHAT.get_accelerometer_raw())
                humTempLst.append(_senseHAT.humidity)
                spdTempLst.append(currentSpeed())
                tempTempLst.append(_senseHAT.temp)
                
                time.sleep(0.1)
            
            self.__accel = __calculateAverage(accTempLst)
            self.__humidity = __calculateAverage(humTempLst)
            self.__speed = __calculateAverage(spdTempLst)
            self.__temp = __calculateAverage(tempTempLst)
            
            __generateFlags(self.__accel, self.__humidity, self.__speed, self.__temp)
            
            self.__dataDict = {
                "ACCELERATION": self.__accel,
                "HUMIDITY": self.__humidity,
                "SPEED": self.__speed,
                "TEMPERATURE": self.__temp,
                "WARN_ACCELERATION": self.__accFlag,
                "WARN_HUMIDITY": self.__humFlag,
                "WARN_SPEED": self.__spdFlag,
                "WARN_TEMPERATURE": self.__tempFlag
                }
            
            self.__dataQueue.append(self.__dataDict)
            
        
    def terminate(self):
        self.isRunning = False
        
    def currentSpeed(self)
        # update speed using the acceleration and update interval
        self.__currentSpeed = self.__currentSpeed + (self.__accX * 0.1)
        
    @staticmethod
    def __generateFlags(acc, relH, spd, temp):  
        if acc > self.__maxAccel:
            self.__accFlag = True
        else:
            self.__accFlag = False
        if relH < self.__minRH or relH > self.__maxRH:
            self.__humFlag = True
        else:
            self.__humFlag = False
        if spd > self.__maxSpeed:
            self.__spdFlag = True
        else:
            self.__spdFlag = False
        if temp < self.__minTemp or temp > self.__maxTemp:
            self.__tempFlag = True
        else:
            self.__tempFlag = False
        
    @staticmethod
    def __calculateAverage(lst):
        return sum(lst) / len(lst)
    
    pass

#        self.__accX = accelData['x']
#        self.__accY = accelData['y']
#       self.__accZ = accelData['z']
        
#        self.__accX = abs(self.__accX)
#        self.__accY = abs(self.__accY)
#        self.__accZ = abs(self.__accZ)
        
        
    
