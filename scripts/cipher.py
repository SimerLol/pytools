# Cipher || Simer@Codeable
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
yourpass = 'lolcat -a -d 25 -p 2 "./banners/yourpass.txt"'
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

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789[]{}()*;/._-! '

def encrypt(key, message):
  key,
  message,
  newmessage=""
  for d in message:
    pos = alphabet.find(d)
    newpos = (pos + key) % 76
    newchar = alphabet[newpos]
    newmessage+=newchar
  print("The encrypted message is:",newmessage)


def decrypt(key, message):
  key,
  message,
  newmessage=""
  for d in message:
    pos = alphabet.find(d)
    newpos = (pos - key) % 76
    newchar = alphabet[newpos]
    newmessage+=newchar
  print("The decrypted message is:",newmessage)


Decider = int(input("1) Would you like to [1]Encrypt or [2]Decrypt?\n"))
key = int(input("2) Enter in your secret pin:\n>>> "))
message = input("3) Enter in your secret message:\n>>> ")
if Decider == 1:
  encrypt(key,message)
elif Decider == 2:
  decrypt(key,message)
else:
  print("Invalid selection.")

# Cipher || Simer@Codeable