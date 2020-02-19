# Olga Rozhdestvina
# Program that takes a positive floating-point number as input
# annd outputs an approximation of its square root.

def sqrt(x):
    if x < 0:
        print("Please restart the program and enter a POSITIVE NUMBER!")
    else:
        print("The square root of {} is approx. {:.1f}".format(x, x ** 0.5))
print(sqrt(x = float(input("Please enter a positive number: "))))

# I coudn't manage to make Newton's method for square roots work