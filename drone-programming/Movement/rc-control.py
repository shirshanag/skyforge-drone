from  pysimverse import Drone
drone=Drone()
left_right=10
forward_backward=0
up_down=20
yaw=0
drone.connect()
while True:
    drone.send_rc_control(left_right, forward_backward, up_down, yaw)
