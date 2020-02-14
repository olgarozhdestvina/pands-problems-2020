# Program that generates 10 random numbers (0 - 100)
# and prints them out 
# then prints out the top three

import random

howMany = 10
topHowMany = 3
rangeFrom = 0
rangeTo = 100

numbers = []

for i in range(0,10):
    numbers.append(random.randint(rangeFrom,rangeTo))
print ("{} random numbers {}".format(howMany,numbers))

topOnes = numbers.copy()
topOnes.sort(reverse = True)
print ("The top {} are {}".format(topHowMany,topOnes[0:topHowMany]))