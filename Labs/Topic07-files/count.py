# Olga Rozhdestvina
#  a program that, uses these two functions, to count how many times
# the program has been run. 

filename = "count.txt"

def openTxt():
    with open(filename) as c:
        number = int(c.read())
        return number


def overWrite(number):
    with open(filename, 'wt') as c:
        c.write(str(number))


num = openTxt()
num += 1
if num == 1:
    print("we run this program once")
elif num == 2:
    print("we run this program twice")
else:
    print("we have run this program {} times".format(num))
overWrite(num)
