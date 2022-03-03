from gpiozero import Button

# Declaring the button pin on pin 17
button = Button(11)

while True:
  
  if button.is_pressed:
    print("The button code works!")
