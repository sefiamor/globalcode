from gpiozero import LED, Button,Buzzer
from time import sleep
import os

button = Button(2)
led= LED(17)

def restart():
   led.on()
   sleep(2)
   print('Rebooting...')
   os.system('sudo shutdown -r now')

button.when_pressed=restart
