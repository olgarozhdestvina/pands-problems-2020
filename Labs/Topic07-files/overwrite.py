# Olga Rozhdestvina
# a function that takes in a number and overwrites a file with that number

filename = "count.txt"
number = int(input("enter a number: "))
def overWrite(number):
    with open(filename, 'wt') as c:
        c.write(str(number))

overWrite(number)