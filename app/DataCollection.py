'''
DataCollection
Data collection class which collects information from the senseHAT,
processes it as appropriate and then enqueues the data as a
dictionary
Kyle Mendonca 2021
'''

from sense_emu import SenseHat
import threading
import time
import queue

#From Controller import Controller

class DataCollection(threading.Thread):
    
    def __init__(self, senseHAT, dataQueue):
        
        threading.Thread.__init__(self)

        self.__DCDataQueue = queue.Queue()
        self.__dataDict = {}
        
        self._senseHAT = SenseHat()
        self.__accelData = [0, 0, 0]
        self.__accel = 0
        self.__humidity = 0
        self.__speed = 0
        self.__temp = 0
        
        self.__accFlag = False
        self.__humFlag = False
        self.__spdFlag = False
        self.__tempFlag = False
        
        self.__currentSpeed = 0
        # change this depending on mounting position of the senseHAT
        self.__accelDirection = 'y'
        
        self.isRunning = True
        
        # define and set required value parameters
        self.__maxTemp = 6
        self.__minTemp = 2
        self.__maxRH = 85
        self.__minRH = 65
        self.__maxSpeed = 80
        self.__maxAccel = 1
        
    def run(self):
        while self.isRunning:
            # update current speed
            self.currentSpeed()
            
            # run loop adding data to lists
            # define temporary lists for storing temporary data
            accTempLst = []
            humTempLst = []
            spdTempLst = []
            tempTempLst = []
            
            # collect data for 1 second
            for i in range(9):
                self.__accelData = self._senseHAT.get_accelerometer_raw()
                self.__accel = self.__accelData[self.__accelDirection]
                accTempLst.append(self.__accel)
                humTempLst.append(self._senseHAT.humidity)
                spdTempLst.append(self.currentSpeed())
                tempTempLst.append(self._senseHAT.temp)
                
                time.sleep(0.1)
            
            self.__accel = self.__calculateAverage(accTempLst)
            self.__humidity = self.__calculateAverage(humTempLst)
            self.__speed = self.__calculateAverage(spdTempLst)
            self.__temp = self.__calculateAverage(tempTempLst)
            
            self.__generateFlags(self.__accel, self.__humidity, self.__speed, self.__temp)
            
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
            
            self.__DCDataQueue.put(self.__dataDict)
            
        
    def terminate(self):
        self.isRunning = False
        
    def currentSpeed(self):
        # update speed using the acceleration and sample rate
        self.__currentSpeed = self.__currentSpeed + (self.__accel * 0.1)
        return self.__currentSpeed
        
    def __generateFlags(self, acc, relH, spd, temp):  
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
        sums = sum(lst)
        length = len(lst)
        divs = sums / length
        return round(divs, 2)
