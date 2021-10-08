'''
MatrixDriver
Matrix driver class contains the methods to display various data
on the LED Matrix on the senseHAT module as required
Kyle Mendonca 2021
'''
from sense_emu import SenseHat
import threading

# import Controller

class MatrixDriver(threading.Thread):
    def __init__(self, senseHAT):
        
        threading.Thread.__init__(self)
        
        self._senseHAT = SenseHat()
        self._currentData = None
        
        # define colour RGB values
        Red = (255,0,0)
        Green = (0,255,0)
        Blue = (0,0,255)
        Orange = (255,165,0)
        Black = (0,0,0)
        White = (255,255,255)
        
        self.isRunning = True
        
    def run(self):
        while self.isRunning:
            pass
        
    def terminate(self):
        self.isRunning = False
        
    def updateData(newData):
        pass
        
    def _displayGraph(self, _senseHAT, temp, relHumidity):
        temp_value = 24 * temp / 100
        RH_value = 24 * relHumidity / 100
        #pixels = [(Red if i > temp_value else Green for i in range(0,23)) + (Orange if i > RH_value for i in range(32,63))]
        pixels = [Red if i > temp_value else Green for i in range(64)]
        self._senseHAT.set_pixels(pixels)
        
    def _displayAccelerationWarning(self, _senseHAT, acceleration):
        self._senseHAT.show_message("Max Acceleration Exceeded!", scroll_speed = 0.25, text_colour = W, back_colour = R)      
        
    def _displayRHWarning(self, _senseHAT, relHumidity):
        self._senseHAT.show_message("Max Humidity Exceeded!", scroll_speed = 0.25, text_colour = W, back_colour = R)      
        
    def _displaySpeedWarning(self, _senseHAT, speed):
        self._senseHAT.show_message("Max Speed Exceeded!", scroll_speed = 0.25, text_colour = W, back_colour = R)
        
    def _displayTempWarning(self, _senseHAT, temp):
        self._senseHAT.show_message("Max Temperature Exceeded!", scroll_speed = 0.25, text_colour = W, back_colour = R)      
        