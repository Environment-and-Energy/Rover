from gpiozero import Robot
from time import sleep

glug = Robot(left=(9,10), right=(8,7))

#while True:
#    glug.forward()
#    sleep(3)
#    glug.stop()
#    glug.right()
#    sleep(1)
#    glug.stop()
#    break