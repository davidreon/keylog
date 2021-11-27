import pynput
from pynput.keyboard import Key, Listener

def on_press(key):
    print("{0} pressed".format(key))
    except AttributeError:
        print(f'Special Key {key} pressed!')
def on_release(key):
    if key == key.esc:
        print(f'Key {key} released')
        return False


with Listener(on_press=on_press, on_release=on_release) as Listener:
    Listener.join() 