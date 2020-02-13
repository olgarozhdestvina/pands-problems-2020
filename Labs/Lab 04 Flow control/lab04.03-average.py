# This program keeps reading numbers until the user enters 0
# and prints out each of the numbers entered and the average of them



Ns = []

N = int (input("enter number(0 to quit): "))

while N != 0:
    Ns.append(N)
    N = int (input("enter number(0 to quit): "))

for value in Ns:
    print(value) 

avg = float(sum(Ns)) / len(Ns)
print("The average os {}".format(avg))