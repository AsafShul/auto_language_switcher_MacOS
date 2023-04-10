# Auto language switcher for MacOS
no more need to manually change the language when switching between apps.

repo for automatically changing the keyboard input language based on the specific app preferences.
- ment to work if you have 2 languages set on your Mac (the swap is equivalent to '^ + space').

### Instructions:
  1. change the absolute path for the 'config json' file in the 'utils.py' file.
  2. change the absolute path for the 'language_switcher.py' file in the 'run.command' file
  3. Change the language preferences in the json file for each app to suit your needs.
  4. open terminal in progect dir and run the command:

```chmod +x run.command```

  5. Right-click the run.command file and click "Make Alias".

<img width="368" alt="image" src="https://user-images.githubusercontent.com/44872433/230908034-a556f0cb-9ebb-48d6-9a3d-1a9612d5fe75.png">

To make an "app-like" desktop executable (optional):

  6. Move the alias to the Desktop (or other wanted location).
  7. Copy to clipboard the icon.png image.
  8. Right-click the alias and click "Get Info".
  9. Click the icon in the top left corner of the "Get Info" window and paste the icon.png image.

<img width="274" alt="image" src="https://user-images.githubusercontent.com/44872433/230908698-18733391-6513-4433-963c-b9ef2403d235.png">

Congratulations! now, you can run the script by double-clicking the alias on the desktop.

<img width="161" alt="image" src="https://user-images.githubusercontent.com/44872433/230907710-36a86b38-aaac-460a-a884-953d30f84d7b.png">

On running, a terminal window will open and the script will run in the background. you can see when language
is changed by the prints in the terminal.

<img width="582" alt="Screen Shot 2023-04-10 at 16 28 47" src="https://user-images.githubusercontent.com/44872433/230910368-ba000749-84b0-4b83-9f9d-69ae8a55fb3f.png">

to kill the sctipt simply terminate the terminal window.


