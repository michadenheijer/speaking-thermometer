from speaking import say_temp, say_shutdown
import os
import keyboard
import time

def key_press(key):
    if "a down" in str(key):
        say_shutdown()
        #os.system("sudo shutdown now")
    else:
        say_temp(24)

keyboard.on_press(key_press)

while True:
    time.sleep (1)


