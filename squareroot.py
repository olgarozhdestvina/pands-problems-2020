# Olga Rozhdestvina
# Program that takes a positive floating-point number as input
# annd outputs an approximation of its square root.

def sqrt(x):
    if x < 0:
        print("Please restart the program and enter a POSITIVE NUMBER!")
    else: # the next two lines taken from https://stackoverflow.com/questions/32291218/use-newtons-method-to-find-square-root-of-a-number
        y = 1.0
        while abs(x - y * y) > 10 **(-10):  
            y = y - (y * y - x) / (2 * y)
        print("The square root of {} is approx. {:.1f}".format(x, y))
sqrt(x = float(input("Please enter a positive number: ")))