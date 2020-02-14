# This program puts 10 random numbers in to a queue,
# then outputs all the values in the queue,
# then takes the number from it one at a time,
# prints it and the current numbers still in the queue

import random

queue = []
rangefrom = 0
rangeto = 100
NofNumbers = 10

for number in range(0,NofNumbers):
    queue.append(random.randint(rangefrom,rangeto))
print("queue is {}".format(queue))

while len(queue) != 0:
    print("curent Number is {} and the queue is {}".format(queue.pop(0), queue))

print("the queue is now empty")