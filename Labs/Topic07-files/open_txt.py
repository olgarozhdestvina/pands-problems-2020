# Olga Rozhdestvina
# Write a function that reads in a number from a file that already exists

filename = "count.txt"
def openTxt():
    with open(filename) as c:
        number = int(c.read())
        return number

num = openTxt()
print(num)