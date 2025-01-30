from gpiozero import Servo
import time

servo = Servo(12)


servo.max()
time.sleep(1)
servo.min()