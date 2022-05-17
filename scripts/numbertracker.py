# NumberTracker || Simer@Codeable
import os
import time
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

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

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

#GeoTracker Active
print("Geo Tracker Active!")
print(END)
number = input(
    "Enter any number to check location... Example: +1234567890\n>>> ")
ch_number = phonenumbers.parse(number, 'CH')
time.sleep(0.5)
clear()
os.system(footer)
print(WHITE)
print(GREY + "Phone Number: ", END + number)
print(GREY + "Country: ",
      END + geocoder.description_for_number(ch_number, "en"))
s_num = phonenumbers.parse(number, 'RO')
print(GREY + "Carrier: ", END + carrier.name_for_number(s_num, "en"))
print(GREY + "Possible Number:", END, phonenumbers.is_possible_number(s_num))
print(GREY + "Valid Number:", END, phonenumbers.is_valid_number(s_num))
print(GREY + "Timezone: ", END, timezone.time_zones_for_number(s_num))
time.sleep(1.5)
print(END)
# NumberTracker || Simer@Codeable