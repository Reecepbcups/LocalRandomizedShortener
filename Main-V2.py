import string

from random import choice
from os import path

# Reece W (v2 - 5/26/2020)
# Basic local URL Condenser.
# Future additions could include:
# - Setting your own variable for the link
# - Removing variables for the link
# - Adding file explorer to a link (ex. root='C:\') to open
# | - maybe add the ability to open multiple files from 1

FILENAME = 'shortener.txt'
ALPHABET = string.ascii_letters + string.digits

def FileLines(FileName=FILENAME):
    if not path.isfile(FileName):
       open(FileName, 'a') 
    return open(FileName, 'r')

def getRandomKey(length=6):
    key = ''.join([choice(ALPHABET) for i in range(length)])

    with open(FILENAME) as f:
        if key not in f.read():
            return key
    # If key was already in use -> get a new key       
    getRandomKey(length)

def main(inputedValue):
    foundLink = False
    
    for line in FileLines():
        value = line.replace('\n','').split('=')
        shortened, link = value[0], value[1]

        if link == inputedValue:
            print(f"Encoded String: {shortened}") 
            foundLink = True

        if shortened == inputedValue:
            print(f"Decoded URL: {link}")
            foundLink = True

    # If link is not found in text file
    if foundLink == False:
                
        ShortenedKey = getRandomKey(6)
        
        f = open(FILENAME, 'a')
        f.write(ShortenedKey+'='+inputedValue+'\n')
        f.close()
        print(f'Your shortened link: {ShortenedKey}')

while True: 
    link = input('New Link or Encoded URL > ')
    main(link)
