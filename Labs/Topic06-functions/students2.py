# Olga Rozhdestvina
# Program that  that allows a user to
# create new students and to view students. 

students = []

def menue():
    print("What would you like to do?")
    print("\t(a) Add new students")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q): ").strip()
    return choice

def doAdd():
    currentStudent = {}
    currentStudent["name"] = input("enter name: ")
    currentStudent["modules"] = readModules()
    students.append(currentStudent)

def readModules():
    modules = []
    modulename = input("\tenter the first module name (blank to quit): ").strip()
    
    while modulename != "":
        module = {}
        module["name"] = modulename
        module["grade"] = int(input("\t\t enter grade: "))
        modules.append(module)
        modulename = input("\tenter next module name (blank to quit): ").strip()
    return modules
 
def viewModules(modules):
    print("\tName: \t\t Grade: ")
    for module in modules:
        print("\t {} \t\t {}". format(module["name"], module["grade"]))

def doView():
    for currentStudent in students:
        print(currentStudent["name"])
        viewModules(currentStudent["modules"])

choicemap = {
    'a': doAdd,
    'v': doView,
    'q': quit
}

choice = menue()
while choice != 'q':
    if choice in choicemap:
        choicemap[choice] ()
    else:
        print("\n\nplease select either a, v or q")
    choice = menue()
