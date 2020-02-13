# This program reads in students until 
# until the user enters blank in the students first name
# and prints out all the students entered

students = []

firstname = input("enter firstname (blank to quit): ").strip()

while firstname != "":
    name = {}
    name["firstname"] = firstname
    lastname = input("enter lastname: ").strip()
    name["lastname"] = lastname
    students.append(name)

    firstname = input("enter firstname of next (blank to quit): ").strip()

print("here are the students you entered:")
for enteredstudents in students:
    print ("{} {}".format(enteredstudents["firstname"],enteredstudents["lastname"]))