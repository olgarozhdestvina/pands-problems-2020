# Olga Rozhdestvina

import sys

try:
    with open(sys.argv[1]) as f:
        print(f.read())
    a = 1 / 0
except FileNotFoundError:
    print("File " + sys.argv[1] + " doesn't exist.")
except ZeroDivisionError:
    print("This is the zero division error handler.")