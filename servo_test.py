import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

# these two lines set the servo pin as pin 22 
GPIO.setup(22, GPIO.OUT) 
pwm=GPIO.PWM(22, 50)

# this makes sure it doesn't set any angles on startup
pwm.start(0)

#SetAngle(90)
#SetAngle(0)

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(22, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(22, False)
	pwm.ChangeDutyCycle(0) # this changes the duty back
  # to 0 so that the pi isn't constantly sending signals to the servo.
SetAngle(90)
SetAngle(0)
