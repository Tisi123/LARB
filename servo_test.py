from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
import time

factory = PiGPIOFactory(host='192.168.178.74')
servo = Servo(12)


servo.max()
time.sleep(1)
servo.min()