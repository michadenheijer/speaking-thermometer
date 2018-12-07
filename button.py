from speaking import say_temp, say_shutdown
from temperature import get_temp
import os
import keyboard
import time

def key_press(key):
    if "a down" in str(key):
        say_shutdown()
        time.sleep(5)
        os.system("sudo shutdown now")
    else:
        say_temp(get_temp())

keyboard.on_press(key_press)

while True:
    time.sleep (1)


