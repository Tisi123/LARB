from gpiozero import Robot
from bluedot import BlueDot
from signal import pause

dot = BlueDot()
robby = Robot(left=(8,25), right=(7,1))


def stop():
    robby.stop()


def move(pos):
    if pos.top:
        robby.forward(pos.distance)
    elif pos.bottom:
        robby.backward(pos.distance)
    elif pos.right:
        robby.right(pos.distance)
    elif pos.left:
        robby.left(pos.distance)


dot.when_pressed = move
dot.when_moved = move
dot.when_released = stop
pause()