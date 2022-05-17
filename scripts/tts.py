# TTS || Simer@Codeable
import os
import sys
import time
import random
import lolcat
from gtts import gTTS
from pyfiglet import Figlet

#defining colors for a user friendly environment
RED = '\033[31;2m'  # red color
BLUE = '\033[34;2m'  # blue color
GREEN = '\033[32;1m'  # green color
YELLOW = '\033[93m'  # yellow color
PINK = '\033[95m'  # ping color
PURPLE = '\033[35m'  # green color
GREY = '\033[90;1m'  # grey color
WHITE = '\033[37;1m'  # white color
END = '\033[m'  # reset to the default

#banners
header = 'lolcat -a -d 3 -p 2 "./banners/header.txt"'
footer = 'lolcat -a -d 3 -p 2 "./banners/footer.txt"'
os.system(header)
print()

#Generating Script
animation = "|/-\\"
for i in range(25):
    time.sleep(0.1)
    sys.stdout.write(WHITE + "\rLoading" + animation[i % len(animation)])
    sys.stdout.flush()
sys.stdout.write(GREEN + "\rLoaded!\n")
time.sleep(0.5)

#clear command
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')


#automated typing thing
def typing(words):
    words
    for char in words:
        time.sleep(random.choice([0.04, 0.04, 0.05, 0.05, 0.04, 0.038, 0.05]))
        sys.stdout.write(char)
        sys.stdout.flush()


#Setting up TTS
audio = 'speech.mp3'
language = 'en'

#TTS Active
print("TTS Active!")
print(YELLOW)
typing("Enter Text to Convert to Speech...")
print(END)
text = input(">>> ")
sp = gTTS(text=text, lang=language, slow=False)
time.sleep(0.5)
sp.save(audio)
print(GREEN)
typing(
    "Please find your TTS in the code section- 'speech.mp3'\n       Make sure to follow me on my socials!")
time.sleep(5)
clear()
os.system(footer)

# TTS || Simer@Codeable