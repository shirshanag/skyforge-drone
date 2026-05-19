from pysimverse import Drone
import time
drone=Drone()
drone.connect()
drone.take_off()
drone.set_speed(720)
drone.move_forward(250)
drone.move_right(220)
drone.move_backward(2)

drone.land()
