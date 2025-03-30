from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
import os
import time

factory = PiGPIOFactory(host=os.environ["PIGPIO_ADDR"])
servo = AngularServo(12)


servo.max_angle = 90
time.sleep(3)
servo.min_angle = -90