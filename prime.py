# Olga Rozhdestvina
# Check if a number is prime
# The primes are 2, 3, 5, 7, 11, 13, ...

p = 347
isprime = True

for m in range(2,p-1):
    if  p % m == 0:
        # print(m, "divides", p, "and therefore", p, "is not prime.")
        isprime = False
        break

if isprime:
    print(p, "is a prime number.")
else:
    print(p, "is not prime")