#This program prints out random number from 1 to 10

import random
x = int(input("Please enter number from: "))
y = int(input("Please enter number to: "))

number = random.randint(x,y)

print("Here is a random number {}".format(number))