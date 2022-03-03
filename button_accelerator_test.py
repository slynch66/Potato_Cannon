import time
import Adafruit_LSM303
import Adafruit_GPIO.SPI as SPI
#import RPi.GPIO as GPIO
from gpiozero import Button
from signal import pause

# Declaring the button pin on pin 17
button = Button(17)

# Suppress warnings
#GPIO.setwarnings(False)

# Use "GPIO" pin numbering
#GPIO.setmode(GPIO.BCM)

# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
lsm303 = Adafruit_LSM303.LSM303()

counter = 0

while True:
  
  if button.is_pressed:
    
    while counter < 20:
      
      # Read the X, Y, Z axis acceleration values.
      accel, mag = lsm303.read()
            
      # Grab the X, Y, Z components from the reading and input them into the .csv file
      accel_x, accel_y, accel_z = accel

      print("accelx = " + accel_x + ";  accely = " + accel_y + "; accelz = " + accel_z)
      
      counter = counter + 1
pause()
