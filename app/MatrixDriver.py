'''
MatrixDriver
Matrix driver class contains the methods to display various data
on the LED Matrix on the senseHAT module as required
Kyle Mendonca 2021
'''
import threading

class MatrixDriver(threading.Thread):
    
    def __init__(self, senseHAT, matrixQueue):
        
        threading.Thread.__init__(self)
        
        self._senseHAT = senseHAT
        self._currentData = None
        self._matrixQueue = matrixQueue

        # clear display
        self._senseHAT.clear()
        
        # define colour RGB values
        self.Red = (255,0,0)
        self.Green = (0,255,0)
        self.Blue = (0,0,255)
        self.Orange = (255,165,0)
        self.Black = (0,0,0)
        self.White = (255,255,255)
        
        self.isRunning = True
        
    def run(self):

        while self.isRunning:

            self.__dataUseDict = self._flushQueue()
            if self.__dataUseDict == None:
                continue

             # display data
            self._senseHAT.clear()
            self._displayGraph(self.__dataUseDict["TEMPERATURE"], self.__dataUseDict["HUMIDITY"])
            
            if self.__dataUseDict["WARN_ACCELERATION"]:
                self._displayAccelerationWarning(self.__dataUseDict["ACCELERATION"])
            if self.__dataUseDict["WARN_HUMIDITY"]:
                self._displayRHWarning(self.__dataUseDict["HUMIDITY"])
            if self.__dataUseDict["WARN_SPEED"]:
                self._displaySpeedWarning(self.__dataUseDict["SPEED"])
            if self.__dataUseDict["WARN_TEMPERATURE"]:
                self._displayTempWarning(self.__dataUseDict["TEMPERATURE"])

        # Clear Screen on Terminate
        self._senseHAT.clear()
        
    def terminate(self):
        self.isRunning = False
        
    def _displayGraph(self, temp, relHumidity):

        if temp < 2:
            for i in range (0,8):
                self._senseHAT.set_pixel(1,i, self.Blue)
                self._senseHAT.set_pixel(2,i, self.Blue)

        elif temp >= 2 and temp <= 6:
            h = int(1.5 * temp - 2)
            for i in range (0,h):
                 self._senseHAT.set_pixel(1,7-i,self.Green)
                 self._senseHAT.set_pixel(2,7-i,self.Green)

        else:
            for i in range (0,8):
                self._senseHAT.set_pixel(1,i, self.Red)
                self._senseHAT.set_pixel(2,i, self.Red)

        if relHumidity < 65:
            for i in range (0, 8):
                self._senseHAT.set_pixel(5,7-i,self.Blue)
                self._senseHAT.set_pixel(6,7-i,self.Blue) 

        elif relHumidity >= 65 and relHumidity <= 85:
            y = int(0.3 * relHumidity - 18.5)
            for i in range (0, y):
                self._senseHAT.set_pixel(5,7-i,self.Orange)
                self._senseHAT.set_pixel(6,7-i,self.Orange) 

        else:
            for i in range (0, 8):
                self._senseHAT.set_pixel(5,7-i,self.Orange)
                self._senseHAT.set_pixel(6,7-i,self.Orange)
        
    def _displayAccelerationWarning(self, acceleration):
        self._senseHAT.show_message("Max Acceleration Exceeded!", scroll_speed = 0.01, text_colour = self.White, back_colour = self.Red)      
        
    def _displayRHWarning(self, relHumidity):
        self._senseHAT.show_message("Max Humidity Exceeded!", scroll_speed = 0.01, text_colour = self.White, back_colour = self.Red)      
        
    def _displaySpeedWarning(self, speed):
        self._senseHAT.show_message("Max Speed Exceeded!", scroll_speed = 0.01, text_colour = self.White, back_colour = self.Red)
        
    def _displayTempWarning(self, temp):
        self._senseHAT.show_message("Max Temperature Exceeded!", scroll_speed = 0.01, text_colour = self.White, back_colour = self.Red)      
        
    def _flushQueue(self):
        # Review the current number of items in the queue
        queueSize = self._matrixQueue.qsize()

        # If no items exist, reuturn null
        if (queueSize == 0):
            return None

        elif (queueSize == 1):
            return self._matrixQueue.get_nowait()
            
        else:
            while(self._matrixQueue.qsize() > 1):
                self._matrixQueue.get_nowait()
            return self._matrixQueue.get_nowait()
