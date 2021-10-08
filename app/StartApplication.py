from Controller import Controller
import time

controller = Controller()
controller.start()

time.sleep(5)
controller.dbAgent.setRemoteOnline()
time.sleep(20)
controller.terminate()