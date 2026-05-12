from pysimverse import Drone
import time
drone=Drone()
drone.connect()
drone.take_off()

drone.move_down(20) #Moving 20 cm downward
time.sleep(2)
drone.move_up(30) # Moving 30 cm upward
time.sleep(2)


drone.land() #Drone land
time.sleep(1)
