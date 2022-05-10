# This will set the double-sided servo horn to perpendicular with the main servo body.

import RPi.GPIO as GPIO
import time

servoPIN = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

try:
    p.ChangeDutyCycle(5)
    time.sleep(0.5)

except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
