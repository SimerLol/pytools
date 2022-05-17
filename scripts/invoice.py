# Invoice || Simer@Codeable
import os
import sys
import time
import random
import lolcat
from reportlab.pdfgen import canvas

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

company = input("Please enter in your full company name\n>>> ")
logo = input("\nPlease enter in your company logo ending with some of these extensions:\n.png .jpg .jpeg etc.\n>>> ")
abn = input("\nPlease enter in company's abn\n>>> ")
suburb = input("\nPlease enter your suburb and country\nExample - Melbourne, Australia\n>>> ")
street = input("\nPlease enter your street and building number\nExample - 101 Example Street\n>>> ")
employee = input("\nPlease enter in the name of the serving employee\n>>> ")

# Creating Canvas
c = canvas.Canvas("invoice.pdf",pagesize=(210,297),bottomup=0)

# Logo Section
# Setting th origin to (10,40)
c.translate(10,40)
# Inverting the scale for getting mirror Image of logo
c.scale(1,-1)
# Inserting Logo into the Canvas at required position
c.drawImage(logo,0,0,width=50,height=50)

# Title Section
# Again Inverting Scale For strings insertion
c.scale(1,-1)
# Again Setting the origin back to (0,0) of top-left
c.translate(-10,-40)
# Setting the font for Name title of company
c.setFont("Helvetica-Bold",10)
# Inserting the name of the company
c.drawCentredString(125,20,company)
# For under lining the title
c.line(70,22,180,22)
# Changing the font size for Specifying Address
c.setFont("Helvetica-Bold",5)
c.drawCentredString(125,30,street)
c.drawCentredString(125,35,suburb)
# Changing the font size for Specifying GST Number of firm
c.setFont("Helvetica-Bold",6)
c.drawCentredString(125,42,"ABN: " + abn)

# Line Seprating the page header from the body
c.line(5,45,195,45)

# Document Information
# Changing the font for Document title
c.setFont("Courier-Bold",8)
c.drawCentredString(100,55,"TAX-INVOICE")

# This Block Consist of Costumer Details
c.roundRect(15,63,170,40,10,stroke=1,fill=0)
c.setFont("Times-Bold",5)
c.drawRightString(70,70,"INVOICE No. :")
c.drawRightString(70,80,"DATE :")
c.drawRightString(70,90,"CUSTOMER NAME :")
c.drawRightString(70,100,"PHONE No. :")

# This Block Consist of Item Description
c.roundRect(15,108,170,130,10,stroke=1,fill=0)
c.line(15,120,185,120)
c.drawCentredString(25,118,"SR No.")
c.drawCentredString(75,118,"GOODS DESCRIPTION")
c.drawCentredString(125,118,"RATE")
c.drawCentredString(148,118,"QTY")
c.drawCentredString(173,118,"TOTAL")
# Drawing table for Item Description
c.line(15,210,185,210)
c.line(35,108,35,220)
c.line(115,108,115,220)
c.line(135,108,135,220)
c.line(160,108,160,220)

# Declaration and Signature
c.line(15,220,185,220)
c.line(100,220,100,238)
c.drawString(20,225,"We declare that above mentioned")
c.drawString(20,230,"information is true.")
c.drawString(20,235,"(This is system generated invoive)")
c.drawRightString(180,235,employee)

# End the Page and Start with new
c.showPage()
# Saving the PDF
c.save()
typing("Finished making the template! Find it in the root folder :)")
time.sleep(3)
clear()
os.system(footer)
# Invoice || Simer@Codeable