#Program that prints out random fruit

import random

fruits = ("Banana", "Apple", "Orange", "Kiwi", "Pineapple")

index = random.randint(0,len(fruits)-1)
fruit = fruits[index]

print("A Random Fruit: {}". format(fruit))