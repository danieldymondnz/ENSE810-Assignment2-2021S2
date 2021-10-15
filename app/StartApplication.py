from Controller import Controller
import time

# Starts Application, Runs for 10 Secs in Offline Mode, 
# then 20s in Online Mode. Created to demonstrate functionality.

# Create controller and start processing data
controller = Controller()
controller.start()

# Wait 10s, then switch DBAgent to Online Mode
time.sleep(10)
controller.dbAgent.setRemoteOnline()

# Wait 20s, then terminate Controller and children threads
time.sleep(20)
controller.terminate()