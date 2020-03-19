import sys
import myfunctions

# get n from the command line
n = int(sys.argv[1])
# calculate the factorial of n
ans = myfunctions.factorial(n)
# print the answer
print("The factorial of", n, "is:", ans)