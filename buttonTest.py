import Adafruit_GPIO.SPI as SPI
import RPi.GPIO as GPIO

# Declaring the button pin on pin 17
button_pin = 17

# Suppress warnings
GPIO.setwarnings(False)

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)

if GPIO.input(button_pin)== True:
  print("The button code works!")
