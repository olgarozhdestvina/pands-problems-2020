def viewModules(modules):
    print("\tName: \t Grade: ")
    for module in modules:
        print("\t {} \t {}". format(module["name"], module["grade"]))

def doView(currentStudent):
    for currentStudent in students:
        print(currentStudent["name"])
        viewModules(currentStudent["modules"])
