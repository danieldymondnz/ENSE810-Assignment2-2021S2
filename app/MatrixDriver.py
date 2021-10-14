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
        self.Red = (255,0,0)
        self.Green = (0,255,0)
        self.Blue = (0,0,255)
        self.Orange = (255,165,0)
        self.Black = (0,0,0)
        self.White = (255,255,255)

        # define Display setups
        self.noWarning = [self.Green, self.Green, self.Green, self.Green, self.Green, self.Green, self.Green, self.Green,
                    self.Blue, self.Blue, self.Green, self.Green, self.Green, self.Red, self.Red, self.Red,
                    self.Blue, self.Blue, self.Green, self.Green, self.Green, self.Red, self.Red, self.Red,
                    self.Blue, self.Blue, self.Green, self.Green, self.Green, self.Red, self.Red, self.Red,
                    self.Green, self.Green, self.Green, self.Green, self.Green, self.Green, self.Green, self.Green,
                    self.Blue, self.Blue, self.Green, self.Green, self.Green, self.Green, self.Orange, self.Orange,
                    self.Blue, self.Blue, self.Green, self.Green, self.Green, self.Green, self.Orange, self.Orange,
                    self.Blue, self.Blue, self.Green, self.Green, self.Green, self.Green, self.Orange, self.Orange]

        self.temWarning = [self.Red, self.Red, self.Red, self.Red, self.Red, self.Red, self.Red, self.Red,
                    self.Blue, self.Blue, self.Green, self.Red, self.Green, self.Red, self.Red, self.Red,
                    self.Blue, self.Blue, self.Green, self.Red, self.Green, self.Red, self.Red, self.Red,
                    self.Blue, self.Blue, self.Green, self.Red, self.Green, self.Red, self.Red, self.Red,
                    self.Green, self.Green, self.Green, self.Green, self.Green, self.Green, self.Green, self.Green,
                    self.Blue, self.Blue, self.Green, self.Green, self.Green, self.Green, self.Orange, self.Orange,
                    self.Blue, self.Blue, self.Green, self.Green, self.Green, self.Green, self.Orange, self.Orange,
                    self.Blue, self.Blue, self.Green, self.Green, self.Green, self.Green, self.Orange, self.Orange]

        self.humWarning = [self.Green, self.Green, self.Green, self.Green, self.Green, self.Green, self.Green, self.Green,
                    self.Blue, self.Blue, self.Green, self.Green, self.Green, self.Red, self.Red, self.Red,
                    self.Blue, self.Blue, self.Green, self.Green, self.Green, self.Red, self.Red, self.Red,
                    self.Blue, self.Blue, self.Green, self.Green, self.Green, self.Red, self.Red, self.Red,
                    self.Red, self.Red, self.Red, self.Red, self.Red, self.Red, self.Red, self.Red,
                    self.Blue, self.Blue, self.Green, self.Red, self.Red, self.Green, self.Orange, self.Orange,
                    self.Blue, self.Blue, self.Green, self.Red, self.Red, self.Green, self.Orange, self.Orange,
                    self.Blue, self.Blue, self.Green, self.Red, self.Red, self.Green, self.Orange, self.Orange]

        self.bothWarning = [self.Red, self.Red, self.Red, self.Red, self.Red, self.Red, self.Red, self.Red,
                    self.Blue, self.Blue, self.Green, self.Red, self.Green, self.Red, self.Red, self.Red,
                    self.Blue, self.Blue, self.Green, self.Red, self.Green, self.Red, self.Red, self.Red,
                    self.Blue, self.Blue, self.Green, self.Green, self.Green, self.Red, self.Red, self.Red,
                    self.Red, self.Red, self.Red, self.Red, self.Red, self.Red, self.Red, self.Red,
                    self.Blue, self.Blue, self.Green, self.Red, self.Red, self.Green, self.Orange, self.Orange,
                    self.Blue, self.Blue, self.Green, self.Red, self.Red, self.Green, self.Orange, self.Orange,
                    self.Blue, self.Blue, self.Green, self.Red, self.Red, self.Green, self.Orange, self.Orange]
        
        self.isRunning = True
        
    def run(self):
        while self.isRunning:
            pass
        
    def terminate(self):
        self.isRunning = False
        
    def _displayGraph(self, _senseHAT, temp, relHumidity):

        self._senseHAT.set_pixels(self.noWarning)

        if temp < 2 or temp > 6:
            self._senseHAT.set_pixels(self.temWarning)
        elif relHumidity < 65 or relHumidity > 85:
            self._senseHAT.set_pixels(self.humWarning)
        elif (temp < 2 or temp > 6) and (relHumidity < 65 or relHumidity > 85):
            self._senseHAT.set_pixels(self.bothWarning)
        else:
            self._senseHAT.set_pixels(self.noWarning)
        
    def _displayAccelerationWarning(self, _senseHAT, acceleration):
        self._senseHAT.show_message("Max Acceleration Exceeded!", scroll_speed = 0.25, text_colour = self.White, back_colour = self.Red)      
        
    def _displayRHWarning(self, _senseHAT, relHumidity):
        self._senseHAT.show_message("Max Humidity Exceeded!", scroll_speed = 0.25, text_colour = self.White, back_colour = self.Red)      
        
    def _displaySpeedWarning(self, _senseHAT, speed):
        self._senseHAT.show_message("Max Speed Exceeded!", scroll_speed = 0.25, text_colour = self.White, back_colour = self.Red)
        
    def _displayTempWarning(self, _senseHAT, temp):
        self._senseHAT.show_message("Max Temperature Exceeded!", scroll_speed = 0.25, text_colour = self.White, back_colour = self.Red)      
        