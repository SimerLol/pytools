# Utility || Simer@Codeable
import os
import sys
import time
import random
import lolcat
from pyfiglet import Figlet

#defining colors for a user friendly environment
RED =   '\033[31;2m' # red color
BLUE =   '\033[34;2m' # blue color
GREEN =   '\033[32;1m' # green color
YELLOW =   '\033[93m' # yellow color
PINK =   '\033[95m' # ping color
PURPLE =   '\033[35m' # green color
GREY =   '\033[90;1m' # grey color
WHITE =   '\033[37;1m' # white color
END =   '\033[m' # reset to the default

#banners
header = 'lolcat -a -d 3 -p 2 "./banners/header.txt"'
utility = 'lolcat -a -d 2 -p 2 "./banners/utility.txt"'
footer = 'lolcat -a -d 3 -p 2 "./banners/footer.txt"'
os.system(header)
os.system(utility)
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

choice = input(YELLOW + ">>> " + END)

if choice == '1':
  clear()
  os.system("python ./scripts/cipher.py")
elif choice == "2":
  clear()
  os.system("python ./scripts/heterogramchecker.py")
elif choice == "3":
  clear()
  os.system("python ./scripts/invoice.py")
elif choice == "4":
  clear()
  os.system("python ./scripts/keylogger.py")
elif choice == "5":
  clear()
  os.system("python ./scripts/numbertracker.py")
elif choice == "6":
  clear()
  os.system("python ./scripts/passgen.py")
elif choice == "7":
  clear()
  os.system("python ./scripts/pseudocode.py")
elif choice == "8":
  clear()
  os.system("python ./scripts/text2ascii.py")
elif choice == "9":
  clear()
  os.system("python ./scripts/tts.py")
elif choice == "#":
  clear()
  os.system("python ./scripts/ytdownload.py")
else:
  typing("Invalid selection! Try again :)")
  time.sleep(2)
  clear()
  os.system("python main.py")

# Utility || Simer@Codeable