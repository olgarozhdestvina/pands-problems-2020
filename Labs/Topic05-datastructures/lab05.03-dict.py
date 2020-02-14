# Program that stores a student name and a list of her courses
# and grades in a dict
# then prints out her data.

Student = {
    "Name": "Mary",
    "Subjects": [
        {
            "subjName": "Programming",
            "grade": 45 },
        {
             "subjName": "Hystory",
             "grade": 99 } 
    ]
}

print("Student: {}".format(Student["Name"]))
for Subjects in Student["Subjects"]:
    print("\t {} \t: {}". format(Subjects["subjName"], Subjects["grade"]))