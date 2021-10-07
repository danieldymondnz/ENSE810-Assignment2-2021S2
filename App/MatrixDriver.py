from sense_emu import SenseHat

import Controller

class MatrixDriver(object):
    def __init__(self, senseHAT):
        self._senseHAT = SenseHat()
        self._currentData = None
        
        R = (255,0,0)
        G = (0,255,0)
        B = (0,0,0)
        W = (255,255,255)
        pass
        
    def run(self):
        pass
        
    def terminate(self):
        pass
        
    def updateData(newData):
        pass
        
    def _displayGraph(self, senseHAT, temp, relHumidity):
        pixels = [R if i > 6 else G for i in range(64)]
        self._senseHAT.set_pixels(pixels)
        pass
        
    def _displayTempWarning(self, senseHAT, temp):
        self._senseHAT.show_message("Max Temperature Exceeded!", scroll_speed = 0.25, text_colour = W, back_colour = R)
        pass
        
    def _displayRHWarning(self, senseHAT, relHumidity):
        self._senseHAT.show_message("Max Humidity Exceeded!", scroll_speed = 0.25, text_colour = W, back_colour = R)
        pass
        
    def _displaySpeedWarning(self, senseHAT, speed):
        self._senseHAT.show_message("Max Speed Exceeded!", scroll_speed = 0.25, text_colour = W, back_colour = R)
        pass
        
    def _displayAccelerationWarning(self, senseHAT, acceleration):
        self._senseHAT.show_message("Max Acceleration Exceeded!", scroll_speed = 0.25, text_colour = W, back_colour = R)
        pass
        
    
