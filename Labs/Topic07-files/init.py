# Olga Rozhdestvina
# A program that checks if the file exist and if it doesn't
# creates it and inputs "0" in it

import os.path

filename = "count.txt"

def openTxt():
    try:
        with open(filename) as c:
            number = int(c.read())
            return number
    except IOError:
        return(0)


def overWrite(number):
    with open(filename, 'wt') as c:
        c.write(str(number))

if not os.path.isfile(filename):
    print("File doesn't exist")
    overWrite(0)