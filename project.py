from pynput.mouse import Listener as ms
from pynput.keyboard import Listener as kb
from pynput.keyboard import Key, Controller
import os
import sys
import subprocess

keyboard = Controller()

def on_press(key):
    print('{0} pressed'.format(
        key))

def on_release(key):
    print('{0} release'.format(
        key))
    if key.char == 'q':
        keyboard.press(Key.f5)
        keyboard.release(Key.f5)
    if key == "a":
        subprocess.call("C:/Users/", shell=True)
    if key == 'z':
        subprocess.call("C:/Users/lkl/Desktop/autofill.vbs", shell=True)
    if key == Key.esc:
        return False

def on_click(x, y, button, pressed):
    if pressed:
        pass
    else:
        #subprocess.call("C:/Users - Copy.vbs", shell=True)
        print('Released')

def on_scroll(x, y, dx, dy):
    print('Scrolled {0}'.format(
        (x, y)))

# Collect events until released
with ms(
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    with kb(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join() 