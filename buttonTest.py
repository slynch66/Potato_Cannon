from gpiozero import Button
from signal import pause

# Declaring the button pin on pin 17
button = Button(17)


#def does_it_work():
#	print("It works!")

#button.when_pressed = does_it_work()

while True:
  
  if button.is_pressed:
    print("The button code works!")
pause()
