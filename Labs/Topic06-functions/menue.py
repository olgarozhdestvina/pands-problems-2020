# Olga Rozhdestvina
# Function that prints out a menu of commands we can perform
# and returns what the user chose

def menue():
    print("What would you like to do?")
    print("\t(a) Add new students")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q): ").strip()
    return choice

choice = menue()
print("you chose {}".format(choice))