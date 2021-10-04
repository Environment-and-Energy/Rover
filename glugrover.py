from gpiozero import Robot, LineSensor
from time import sleep
from signal import pause

glug = Robot(left=(26,19), right=(15,18)) # Initialise motors
left_Sensor = LineSensor(21) # Initialise left line sensor / Orange out cable
right_Sensor = LineSensor(20) # Initialise right line sensor / Yellow out cable

# Code to run the Rover with line sensors
left_Sensor.when_line = glug.left
right_Sensor.when_line = glug.right
left_Sensor.when_no_line = glug.forward(0.4)
right_Sensor.when_no_line = glug.forward(0.4)

pause()

# Code to run the Rover with motor controller
#while True:
    #glug.forward(0.4)
    #sleep(3)
    #glug.stop()
    #glug.right(0.4)
    #sleep(1)
    #glug.stop()
    #break
