# Papago Kor => Eng Subtitle Translations

## Requirements
1. `python3` is installed
2. Install `selenium` using `pip`
3. `chrome web driver` is installed and is in `PATH`
## Installation
1. Follow instructions on installing Selenium and installing Chrome webdriver [from official Selenium Docs](https://www.selenium.dev/documentation/en/getting_started_with_webdriver/)
   2. Make sure to add chromedriver `PATH` correctly
 
## Running Script

1. Download project from github repo
2. Place the subtitle file into `/subs` folder (ex. `Night_Talk.srt`)
3. Cd into the folder of the project and type `python translate.py` or `python3 translate.py` if your have both python versions.
4. Type in the name of your subtitle file inside the `/subs` folder (ex. `Knock_Knock_2_KOR.srt`)
   1. Remember to include the file type `.srt` at the end
5. Type in the name of the target file. If it doesn't exist it will be made.
   1. ex. `Knock_Knock_2_ENG.srt` file doesn't exist, it will be made.
6. Wait for the `chrome` web driver to run.
7. Wait until the `script` finishes. Usually takes around ~20mins

## Bugs
1. Some of the last few lines weren't saved into the target file. Need to investigate.