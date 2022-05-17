# HeterogramChecker || Simer@Codeable
import os
import sys
import time
import random
import lolcat

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

# Function to Check whether a given string is Heterogram or not   
def heterogram(input):
  
     # separate out list of alphabets using list comprehension
     # ord function returns ascii value of character
     alphabets = [ ch for ch in input if ( ord(ch) >= ord('a') and ord(ch) <= ord('z') )]
  
     # convert list of alphabets into set and 
     # compare lengths
     if len(set(alphabets))==len(alphabets):
         print ("\nYes, it's a heterogram!")
     else:
         print ("\nNo, it's not a heterogram!")
  
input = input("Type something to check if it's a heterogram or not\n>>> ")
heterogram(input)
time.sleep(3)
clear()
os.system(footer)
# HeterogramChecker || Simer@Codeable