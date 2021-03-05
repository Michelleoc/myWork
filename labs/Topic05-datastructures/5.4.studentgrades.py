# A program that stores a student name and the list of courses and grade in a dict 
# The program will then print out her data
# The number of course she has could change
# Author: Michelle O'Connor

student = {
    "name": "Mary",

    "modules": [
        {
            "courseName": "Programming",
            "grade": 45
        },
        {
            "courseName": "History",
            "grade": 99
        }
    ]
}

print("Student: {}".format(student["name"]))

for module in student["modules"]:
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))
