# Olga Rozhdestvina
# Adding into last week program a new menue item Save.
#  When the user selects the doSave() function should be called 

# Olga Rozhdestvina
# Program that  that allows a user to
# create new students and to view students. 

students = []
import json
filename = "studentData.json"

def writeDict(obj):
    with open (filename, "wt") as f:
        json.dump(obj,f)

def readDict():
    with open (filename) as f:
        return json.load(f)

def menue():
    print("What would you like to do?")
    print("\t(a) Add new students")
    print("\t(v) View students")
    print("\t(s) Save students")
    print("\t(l) Load students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/s/l/q): ").strip()
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
    print("\tName: \t\t\t Grade: ")
    for module in modules:
        print("\t {} \t\t {}". format(module["name"], module["grade"]))

def doView():
    for currentStudent in students:
        print(currentStudent["name"])
        viewModules(currentStudent["modules"])


def doSave():
    writeDict(students)
    print("students saved")

def doLoad():
    global students
    students = readDict()
    print("students loaded")



choicemap = {
    'a': doAdd,
    'v': doView,
    's': doSave,
    'l': doLoad,
    'q': quit
}

choice = menue()
while choice != 'q':
    if choice in choicemap:
        choicemap[choice] ()
    else:
        print("\n\nplease select either a, v, s, l or q")
    choice = menue()
