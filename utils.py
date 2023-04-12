# imports:
import os
import sys
import copy
import json
import subprocess

# constants:
BUFFER_SIZE = 32
TYPING_DILAY = 0.05

file_path = sys.argv[0]
WORK_DIR = file_path[:len(file_path) - file_path[::-1].find('/')]

with open(os.path.join(WORK_DIR, 'run.command')) as f:
    lines = f.readlines()

PRIME_TYPING_CHANGE_ACTIVATION = [c for c in \
                                  lines[0][lines[0].find("'") + 1: len(lines[0]) - lines[0][::-1].find("'") - 1]]

ACTIVATION_SIZE = len(PRIME_TYPING_CHANGE_ACTIVATION)


CONFIG_JSON_PATH = os.path.join(WORK_DIR, 'language_config.json')
CONVERSION_JSON_PATH = os.path.join(WORK_DIR, 'conversion_chart_ABC_Hebrew.json')

LAYOUT_RETURN_PREFIX = '"KeyboardLayout Name" = '
LAYOUT_RETURN_POSTFIX = ';\n    }\n)'

# apple scripts:
CHANGE_LANGUAGE_SCRIPT = "osascript -e 'tell application \"System Events\" to tell process \"SystemUIServer\" to " \
                         "keystroke space using {control down}' "

GET_CURRENT_LAYOUT_SCRIPT = "defaults read ~/Library/Preferences/com.apple.HIToolbox.plist AppleSelectedInputSources"

GET_ACTIVE_WINDOW_SCRIPT = "osascript -e 'tell app \"System Events\" to get name of first process whose frontmost is " \
                           "true' "


# functions:
def load_json(path):
    """
    Load a json file.
    :param path: the path to the json file.
    :return: the json file as a dict.
    """
    with open(path) as f:
        return json.load(f)


MAIN_LAYOUT, SECONDARY_LAYOUT = list(load_json(CONVERSION_JSON_PATH).keys())
CONVERSION_PAIRS = load_json(CONVERSION_JSON_PATH)


def run_script(script):
    """
    Run a script and return the output.
    :param script: applescript string to run.
    :return: the output from the activation.
    """
    return subprocess.check_output(script, shell=True).decode('utf-8').strip()


def get_current_layout():
    """
    Get the current keyboard layout.
    :return: the current keyboard layout.
    """

    current_layout = run_script(GET_CURRENT_LAYOUT_SCRIPT)
    return current_layout[current_layout.find(LAYOUT_RETURN_PREFIX) + len(LAYOUT_RETURN_PREFIX):
                          current_layout.find(LAYOUT_RETURN_POSTFIX)]


def convert_typing(layout, stack):
    """
    Convert the typing from one language to another.
    :param stack: text to convert as a list.
    :param layout: current keyboard language.
    :return: the converted text.
    """
    print(layout, get_current_layout())
    if layout != MAIN_LAYOUT and layout != SECONDARY_LAYOUT:
        return copy.deepcopy(stack)
    else:
        return [CONVERSION_PAIRS[layout][key] if key in CONVERSION_PAIRS[layout] else key
                for key in stack]


SECONDARY_TYPING_CHANGE_ACTIVATION = convert_typing(MAIN_LAYOUT, PRIME_TYPING_CHANGE_ACTIVATION)
