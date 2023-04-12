# Auto language switcher for MacOS

no more need to manually change the language when switching between apps, or re-write mistyped text!

this repo will automatically change the keyboard input language based on the specific app preferences, and fix mistypes.



<img width="625" alt="image" src="https://user-images.githubusercontent.com/44872433/231365942-d7fdc5f6-2eaf-44bd-9924-e417b8e8bb4a.png">
<img width="627" alt="image" src="https://user-images.githubusercontent.com/44872433/231366013-d33cb7eb-954a-4bc9-803d-4f4ab82ac91b.png">

- ment to work if you have 2 languages set on your Mac (the swap is equivalent to '^ + space').

### Instructions:
  1. in the 'run.command' change the folliwing:
    
   * change the absolute path for the 'language_switcher.py'.
    
   * optional: the fix activation sequance (default '000').
    
  2. Change the language preferences in the 'language_config.json' file for each app to suit your needs.
  3. create an 'conversion_chart_<MAIN_LAYOUT>_<SECONDARY_LAYOUT>.json' in the same format for your language (its a somewhat manual process, you can use chatGPT to speef it up). in this repo, MAIN_LAYOUT='ABC' (thats the layout name for English) and SECONDARY_LAYOUT='Hebrew', these names need to match the names for your 'language_config.json'
  4. open terminal in project dir and run the command:

    chmod +x run.command

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


