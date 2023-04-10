# imports:
import time
from utils import *

# constants:
LOOP_ITER_DELAY = 0.5  # (seconds) change as you see fit:


# functions:
def change_keyboard_language(language_config: dict, active_window_title: str):
    """
    Change the keyboard layout to the wanted layout.
    :param language_config: The language config dict.
    :param active_window_title: string of the active window title.
    :return: None
    """
    # Get the wanted layout:
    wanted_layout = language_config.get(active_window_title)

    # Check the current keyboard layout:
    current_layout = run_script(GET_CURRENT_LAYOUT_SCRIPT)

    # If the wanted layout is not the current layout, change it:
    if wanted_layout and (wanted_layout not in current_layout):
        print(f'active_window changed to: {active_window_title} -> Changing keyboard layout to: "{wanted_layout}"...')
        # Change the keyboard layout to English
        subprocess.call(CHANGE_LANGUAGE_SCRIPT, shell=True)
    else:
        print(f'active_window changed to: {active_window_title} -> Keyboard layout is already correct.')


def runner() -> None:
    """
    The main loop of the program.
    :return: None
    """
    # Load the language config:
    config = load_json()

    # Run the main loop:
    prev_active_window = None
    while True:
        # check if the active window changed:
        active_window = run_script(GET_ACTIVE_WINDOW_SCRIPT)
        if (not prev_active_window) or (active_window != prev_active_window):
            change_keyboard_language(config, active_window)
            prev_active_window = active_window
        time.sleep(LOOP_ITER_DELAY)


# main:
if __name__ == '__main__':
    runner()
