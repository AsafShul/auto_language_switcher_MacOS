# imports:
import time
from threading import Lock

from pynput import keyboard, mouse
from utils import *

# threading globals:
keys_pressed = []
listen = True
listen_lock = Lock()
keys_pressed_lock = Lock()
keyboard_controller = keyboard.Controller()


# functions:
def re_write_stack() -> None:
    """
    Re-write the keys_pressed stack with the correct typing.
    :return: None
    """
    print('Re-write activated: fixing typing in wrong language...')
    global keys_pressed, keys_pressed_lock, listen_lock, listen

    # Get the fixed keys:
    fixed_keys_pressed = convert_typing(get_current_layout(), keys_pressed[:-ACTIVATION_SIZE])
    run_fixed_keys = ([keyboard.Key.backspace] * len(keys_pressed)) + fixed_keys_pressed

    # Reset the keys_pressed list and change the keyboard layout:
    with keys_pressed_lock:
        keys_pressed = []

    subprocess.call(CHANGE_LANGUAGE_SCRIPT, shell=True)

    # Re-write the keys:
    for key in run_fixed_keys:
        keyboard_controller.press(key)
        keyboard_controller.release(key)
        time.sleep(TYPING_DILAY)

    with listen_lock:
        listen = True


def register_key(key: keyboard.Key) -> None:
    """
    Register the pressed key to the stack.
    :param key: pynput.keyboard.Key
    :return: None
    """
    global keys_pressed, listen_lock, listen
    if not listen:
        return

    # Add the key to the keys_pressed list and handle special keys:
    with keys_pressed_lock:
        try:
            char = key.char
            if char:
                keys_pressed.append(key.char)

        except AttributeError:
            # special keys like shift or enter don't have a char attribute
            if key == keyboard.Key.space:
                keys_pressed.append(keyboard.Key.space)
            elif key == keyboard.Key.backspace and keys_pressed:
                keys_pressed.pop()
            else:
                keys_pressed = []

    # Check if the activation keys were pressed, if so, re-write the stack:
    if keys_pressed and (len(keys_pressed) > ACTIVATION_SIZE):
        if (keys_pressed[-ACTIVATION_SIZE:] == PRIME_TYPING_CHANGE_ACTIVATION) or \
                (keys_pressed[-ACTIVATION_SIZE:] == SECONDARY_TYPING_CHANGE_ACTIVATION):
            with listen_lock:
                listen = False

            re_write_stack()


def reset_keys(x, y, button, pressed) -> None:
    global keys_pressed, keys_pressed_lock
    """
    Empties the keys stack.
    """
    with keys_pressed_lock:
        keys_pressed = []


# main:
if __name__ == '__main__':
    # create threads for the keyboard and mouse listeners
    with keyboard.Listener(on_press=register_key) as k_listener:
        with mouse.Listener(on_click=reset_keys) as m_listener:
            k_listener.join()
            m_listener.join()
