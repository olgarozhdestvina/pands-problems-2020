# This program reads in a students percentage mark
# and prints out the corresponding grade
#Modified to deal with rounding

x = float (input ("Enter the percentage: "))


if x < 40:
    print("Fail")
elif x <= 49.5:
    print("Pass")
elif x <= 59.5:
    print("Merit 2")
elif x <= 69.5:
    print("Merit 1")
else:
    print("Distinction")


# or 

x = float (input ("Enter the percentage: "))

if x < 40:
    print("Fail")
elif x < 49.6:
    print("Pass")
elif x < 59.6:
    print("Merit 2")
elif x < 69.6:
    print("Merit 1")
else:
    print("Distinction")