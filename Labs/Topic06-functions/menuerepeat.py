# Olga Rozhdestvina
# Function that keeps displaying the menu until the user picks q. 

def menue():
    print("What would you like to do?")
    print("\t(a) Add new students")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q): ").strip()
    return choice

def doAdd():
    print("in adding")

def doView():
    print("in viewing")

choice = menue()
while choice != 'q':
    if choice == 'a':
        doAdd()
    elif choice == 'v': 
        doView()
    else:
        print("\n\nplease select either a, v or q")
    choice = menue()
