from sense_emu import SenseHat
import threading

import Controller

class MatrixDriver(object):
    def __init__(self, senseHAT):
        
        threading.Thread.__init__(self)
        
        self._senseHAT = SenseHat()
        self._currentData = None
        
        Red = (255,0,0)
        Green = (0,255,0)
        Blue = (0,0,255)
        Orange = (255,165,0)
        Black = (0,0,0)
        White = (255,255,255)
        
        self.isRunning = True
        
    def run(self):
        while self.isRunning:
            updateData()
        
    def terminate(self):
        self.isRunning = False
        
    def updateData(newData):
        _displayGraph(?????????)
        # check flags and display relevant warnings if needed
        
    def _displayGraph(self, senseHAT, temp, relHumidity):
        pixels = [(Red if i > 6 else Green for i in range(8,24)) + (Orange if i > 28 for i in range(48,56))]
        self._senseHAT.set_pixels(pixels)
        
    def _displayAccelerationWarning(self, _senseHAT, acceleration):
        self._senseHAT.show_message("Max Acceleration Exceeded!", scroll_speed = 0.25, text_colour = W, back_colour = R)      
        
    def _displayRHWarning(self, _senseHAT, relHumidity):
        self._senseHAT.show_message("Max Humidity Exceeded!", scroll_speed = 0.25, text_colour = W, back_colour = R)      
        
    def _displaySpeedWarning(self, _senseHAT, speed):
        self._senseHAT.show_message("Max Speed Exceeded!", scroll_speed = 0.25, text_colour = W, back_colour = R)
        
    def _displayTempWarning(self, _senseHAT, temp):
        self._senseHAT.show_message("Max Temperature Exceeded!", scroll_speed = 0.25, text_colour = W, back_colour = R)      
        