import time
import Adafruit_LSM303
import Adafruit_GPIO.SPI as SPI
import RPi.GPIO as GPIO
from gpiozero import Button

# Declaring the button pin on pin 17
button = Button(17)

# Suppress warnings
GPIO.setwarnings(False)

# Use "GPIO" pin numbering
#GPIO.setmode(GPIO.BCM)

# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
lsm303 = Adafruit_LSM303.LSM303()

# this is the code that will run once the button is pressed
def on_the_clock():
    
    # sleep for 15 seconds in order to allow time for the shell to be sealed, loaded into the cannon, and the potato cannon to be primed to fire
    time.sleep(15)
    
    # max_time is the number of seconds of duration for the timer on line 39
    max_time = 4
    
    # this line activates the timer by recording a start time
    start_time = time.time()
    
    # Organizes the X Y and Z readings into lists that go into a new .csv file, which is a dataset
    with open("accel_data.csv", "a") as log:
        
        # writes the titles to the columns
        log.write("{0},{1},{2}\n".format("accel_x", "accel_y", "accel_z"))
        
        # the code in this while loop will run until it reaches the number of seconds have gone by for the max_time variable
        while (time.time() - start_time) < max_time:
        
            # Read the X, Y, Z axis acceleration values.
            accel, mag = lsm303.read()
            
             # Grab the X, Y, Z components from the reading and input them into the .csv file
            accel_x, accel_y, accel_z = accel
            log.write("{0},{1},{2}\n".format(accel_x, accel_y, accel_z))
            
            # delay a quarter of a second before recording another reading
            time.sleep(.25)

 

# When the button is pressed it will activate the program
  if button.is_pressed:
    print("The button code works!")
    on_the_clock()
    
# as a github entry or reflection, I can review source #3 and explain how I created a timer using lines 30, 33, and 39

# as another github entry or reflection, I can review source #2 and explain how I created a table of values using lines 36 and 46 of my code

# sources:
#    1   https://projects.raspberrypi.org/en/projects/temperature-log/2
#    2   https://raspberrypi.stackexchange.com/questions/13720/best-way-to-store-temperature-data-offline
#    3   https://stackoverflow.com/questions/2831775/running-a-python-script-for-a-user-specified-amount-of-time
