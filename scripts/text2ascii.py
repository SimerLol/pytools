# Pseudocode || Simer@Codeable
import os
import sys
import time
import random
import lolcat
from art import tprint

#defining colors for a user friendly environment
RED =   '\033[31;2m' # red color
BLUE =   '\033[34;2m' # blue color
GREEN =   '\033[32;1m' # green color
YELLOW =   '\033[93m' # yellow color
PINK =   '\033[95m' # ping color
PURPLE =   '\033[35m' # green color
ORANGE = '\033[33m' # orange color
CYAN = '\033[94m' # cyan color
GREY =   '\033[90;1m' # grey color
WHITE =   '\033[37;1m' # white color
END =   '\033[m' # reset to the default

#banners
header = 'lolcat -a -d 3 -p 2 "./banners/header.txt"'
footer = 'lolcat -a -d 3 -p 2 "./banners/footer.txt"'
os.system(header)
print()

#clear command
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

# automated typing thing 
def typing(words):
  words
  for char in words:
    time.sleep(random.choice([0.04, 0.04,0.05, 0.05, 0.04, 0.038, 0.05]))
    sys.stdout.write(char)
    sys.stdout.flush()

def color_choice():

    print(YELLOW + "Pick a color (for color):\n")
    print(RED + "(1) Red")
    print(GREEN + "(2) Green")
    print(YELLOW + "(3) Yellow")
    print(ORANGE + "(4) Orange")
    print(BLUE + "(5) Blue")
    print(CYAN + "(6) Cyan")

def load():
    print(RED + "Loading...")
    time.sleep(1.5)
    os.system("clear")

text = input(YELLOW + "Enter your text to convert to ASCII: ")
font_y_n = input(CYAN + "\nAny fonts (y/n)? ")
colors = input(ORANGE + "\nAny colors (y/n)? ")
print(YELLOW + "\nAnimations are on")
input(BLUE + "\nPress enter to continue ")
os.system("clear")

if font_y_n == "n":
    load()
    if colors == "n":
        for i in range(1):
            colours = random.choice(
                [RED, GREEN, ORANGE, BLUE, CYAN, YELLOW, WHITE])
            tprint(text)
            time.sleep(0.5)
            os.system("clear")
            print(colours, end="")
        print(WHITE, end="")
        tprint(text)
    else:
        color_choice()
        color = input(ORANGE + "\nYour choice: ")
        print("")
        load()
        time.sleep(0.1)
        os.system("clear")
        for i in range(1):
            colours = random.choice(
                [RED, GREEN, ORANGE, BLUE, CYAN, YELLOW, WHITE])
            tprint(text)
            time.sleep(0.5)
            os.system("clear")
            print(colours, end="")
        if color == "1":
            print(RED, end="")
            tprint(text)
        elif color == "2":
            print(GREEN, end="")
            tprint(text)
        elif color == "3":
            print(YELLOW, end="")
            tprint(text)
        elif color == "4":
            print(ORANGE, end="")
            tprint(text)
        elif color == "5":
            print(BLUE, end="")
            tprint(text)
        else:
            print(CYAN, end="")
            tprint(text)
else:
    load()
    print(YELLOW + "Any text can be turned to a font\n")
    print(ORANGE +
        '''Recommended fonts: lol, wdym, afk, noice, china, binary, idk, ethiopia, unicode, and supercalifragilisticexpialidocious(italic)\n'''
    )
    fonta = input(CYAN + "Your font: ")
    os.system("clear")
    load()
    if colors == "n":
        print(WHITE, end="")
        tprint(text, font=fonta)
    else:
        color_choice()
        color = input(ORANGE + "\nYour choice for color: ")
        print("")
        os.system('clear')
        load()
        time.sleep(0.1)
        os.system("clear")
        for i in range(1):
            colours = random.choice(
                [RED, GREEN, ORANGE, BLUE, CYAN, YELLOW, WHITE])
            tprint(text, font=fonta)
            time.sleep(0.5)
            os.system("clear")
            print(colours, end="")
        if color == "1":
            print(RED, end="")
            tprint(text, font=fonta)
        elif color == "2":
            print(GREEN, end="")
            tprint(text, font=fonta)
        elif color == "3":
            print(YELLOW, end="")
            tprint(text, font=fonta)
        elif color == "4":
            print(ORANGE, end="")
            tprint(text, font=fonta)
        elif color == "5":
            print(BLUE, end="")
            tprint(text, font=fonta)
        else:
            print(CYAN, end="")
            tprint(text, font=fonta)
time.sleep(3)
clear()
os.system(footer)