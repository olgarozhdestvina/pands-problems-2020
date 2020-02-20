# Olga Rozhdestvina
# Function that reads the students name, 
# the module names and grades


students = []



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

doAdd()
doAdd()
print(students)