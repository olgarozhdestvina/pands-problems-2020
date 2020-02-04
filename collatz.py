# Olga Rozhdestvina
# Program that asks a user to input any positive integer
# and outputs the successive values of the following calculations:

x = int(input("Please enter a positive integer: "))
  
while True:
    if x < 0:
        print("Please start the program again and enter POSITIVE integer!")
        break
    elif x == 1:
        break
    elif x % 2 == 0:
        x = int(x / 2)
        print (x, end=" ")
    else:
        x = int (x * 3 + 1)
        print (x, end=" ")