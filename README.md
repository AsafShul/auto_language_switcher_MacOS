# Auto language switcher for MacOS
no more need to manually change the language when switching between apps.

repo for automatically changing the keyboard input language based on the specific app preferences.
- ment to work if you have 2 languages set on your Mac (the swap is equivalent to '^ + space').

### Instructions:
1. change the absolute path for the config json file in the utils.py file.
2. change the absolute path for the language_switcher.py file in the run.command file
3. right-click the run.command file and click "Make Alias"
4. move the alias to the Desktop (or other wanted location)
5. right-click the alias and click "Get Info"
6. copy to clipboard the icon.png image
7. click the icon in the top left corner of the "Get Info" window and paste the icon.png image

congratulations! now, you can run the script by double-clicking the alias on the desktop, 
a terminal window will open and the script will run in the background. you can see when language
is changed by the prints in the terminal.
change the language preferences in the json file for each app to suit your needs.
