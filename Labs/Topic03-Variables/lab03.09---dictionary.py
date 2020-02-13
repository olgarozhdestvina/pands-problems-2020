student = {
    "firstname": "joe", 
    "lastname": "bloggs"
}
print (student)
print("The student's full name is:")
for value in student.values():
    print("  => {}".format(value))