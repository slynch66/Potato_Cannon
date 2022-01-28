import time
import Adafruit_LSM303
import Adafruit_GPIO.SPI as SPI
import RPi.GPIO as GPIO

# Declaring the button pin
button_pin = 17

# Suppress warnings
GPIO.setwarnings(False)

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)

# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
lsm303 = Adafruit_LSM303.LSM303()

# Need code for a button to start this program
def launch_sequence():
    time.sleep(15) # sleep for 15 seconds in order to allow time for the shell to be sealed, and the potato cannon to be primed to fire
    
    # Read the X, Y, Z axis acceleration values.
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    
    # Organize the X Y and Z readings into lists that go into a dataset, which is a .csv file
 

if GPIO.input(button_pin)== True:
    
    
