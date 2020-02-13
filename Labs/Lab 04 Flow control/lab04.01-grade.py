# This program reads in a students percentage mark
# and prints out the corresponding grade

x = float (input("Enter the percentage: "))

if x < 40:
    print("Fail")
elif x in range(40, 49):
    print("Pass")
elif x in range(50, 59):
    print("Merit 2")
elif x in range(60, 69):
    print("Merit 1")
else:
    print("Distinction")