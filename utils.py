# imports:
import json
import subprocess

# constants:
JSON_PATH = 'language_config.json'

CHANGE_LANGUAGE_SCRIPT = "osascript -e 'tell application \"System Events\" to tell process \"SystemUIServer\" to " \
                         "keystroke space using {control down}' "

GET_CURRENT_LAYOUT_SCRIPT = "defaults read ~/Library/Preferences/com.apple.HIToolbox.plist AppleSelectedInputSources"

GET_ACTIVE_WINDOW_SCRIPT = "osascript -e 'tell app \"System Events\" to get name of first process whose frontmost is " \
                           "true' "


# functions:
def run_script(script):
    """
    Run a script and return the output.
    :param script: applescript string to run.
    :return: the output from the activation.
    """
    return subprocess.check_output(script, shell=True).decode('utf-8').strip()


def load_json(path=JSON_PATH):
    """
    Load a json file.
    :param path: the path to the json file.
    :return: the json file as a dict.
    """
    with open(path) as f:
        return json.load(f)
