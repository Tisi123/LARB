from gpiozero import AngularServo
from bluedot import BlueDot
from signal import pause

dot = BlueDot()
servo = AngularServo(12)

def turn(pos):
    if pos.right:
        servo.angle = 90
    elif pos.left:
        servo.angle = -90

#dot.when_pressed = turn
dot.when_moved = turn
dot.when_released = servo.angle = 0
pause()