from pysimverse import Drone
import time
drone=Drone()
drone.connect()
drone.take_off() #Taking off the drone
time.sleep(2) #Waiting for 2 seconds
drone.set_speed(50) #Setting the speed to 50 cm/s
drone.rotate(60) #Rotating the drone by 60 degrees

time.sleep(2)

drone.land()
time.sleep(1)
