# Program that prints out random fruit through tuple

import random
fruits = tuple("Banana", "Apple", "Kiwi", "Orange")
random.choice(fruits)

print("A Random fruit: {}".format(fruits))