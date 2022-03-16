from gpiozero import Servo
from time import sleep

servo = Servo(22)

while True:
    servo.min()
    sleep(3)
    servo.mid()
    sleep(3)
    servo.max()
    sleep(3)
