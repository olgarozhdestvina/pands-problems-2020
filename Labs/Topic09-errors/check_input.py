# Olga Rozhdestvina
# a program	that takes in a number as an input and subtracts 10%	
# prints the result,
# the program should throw a value error of the input is less than 0

# input number
num = int(input("Please enter a number: "))
# calculate 90% 
percent = 0.90 # (1- 0.10) 
ans = num * percent
if num < 0:
    raise ValueError("input should be greater than 0: {}".format(num))
print("{} minus 10% is {}".format(num, ans))