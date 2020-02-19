# Olga Rozhdestvina
# A function to power numbers

def power(x, y):
    ans = x
    y = y - 1
    while y > 0:
        ans = ans * x
        y = y - 1
    return ans

print(power(3, 6))


import math

def isprime(i):
    # Loop through all values j from 2 up to but not incl i
    for j in range(2, math.floor(math.sqrt(i))):
        # See if j divides i
        if i % j == 0:
            # If it does, i isn't a prime so exit the loop
            return False
    return True