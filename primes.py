# Olga Rozhdestvina
# Computing the primes

# My list of primes - TBD
P = []
#Loop through all of the numbers we#re checking for primality 

for i in range(2, 3000):
    # Assume that i is a prime
    isprime= True
    # Loop through all values j from 2 up to but not incl i
    for j in range(2, i):
        # See if j divides i
        if i % j == 0:
            # If it does, i isn't a prime so exit the loop
            isprime = False
            break
    # if it is prime, then append to P.
    if isprime:
        P.append(i)
# Print out our list.
print(P)