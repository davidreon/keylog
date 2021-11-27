import pynput.keyboard as Keyboard

def on_press(key):
    # Callback function whenever a key is pressed
    try:
        print(f'Key {key.char} pressed!')
    except AttributeError:
        print(f'Special Key {key} pressed!')
 
def on_release(key):
    print(f'Key {key} released')
    if key == Keyboard.Key.esc:
        # Stop the listener
        return False

with Keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

    