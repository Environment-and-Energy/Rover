from gpiozero import Robot, LineSensor
from time import sleep

glug = Robot(left=(19,26), right=(15,18)) # Initialise motors
left_Sensor = LineSensor(21) # Initialise left line sensor / Orange out cable
right_Sensor = LineSensor(20) # Initialise right line sensor / Yellow out cable

speed = 0.65

# Code to run Rover with line sensors
def motor_speed():
    while True:
        left_detect = int(left_Sensor.value)
        right_detect = int(right_Sensor.value)
        # Stage 1
        if left_detect == 0 and right_detect == 0:
            left_mot = 1
            right_mot = 1
        # Stage 2
        if left_detect == 0 and right_detect == 1:
            left_mot = -1
        if left_detect == 1 and right_detect == 0:
            right_mot = -1
        yield (right_mot * speed, left_mot * speed)

glug.source = motor_speed()

sleep(60)
glug.stop()
glug.source = None
glug.close()
left_Sensor.close()
right_Sensor.close()

# Test code to test the Rover with line sensors
#left_Sensor.when_line = glug.left()
#right_Sensor.when_line = glug.right()
#left_Sensor.when_no_line = glug.forward()
#right_Sensor.when_no_line = glug.forward()

# Code to run the Rover with motor controller
#while True:
    #glug.forward(0.4)
    #sleep(10)
    #glug.stop()
    #glug.right(0.4)
    #sleep(1)
    #glug.stop()
    #break
