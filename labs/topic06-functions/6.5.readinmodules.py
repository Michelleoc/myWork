# Read in the modules and keep reading moduules until the user enters a module name of blank
# Author : Michelle O'Connor

students= []

def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit) :").strip()
    
    while moduleName != "":
        module = {}
        module["name"]= moduleName
        module["grade"]=int(input("\t\tEnter grade: "))
        modules.append(module)
        # now read the next module name
        moduleName = input("\tEnter next module name (blank to quit) :").strip()

    return modules


def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("Enter name: ")
    currentStudent["modules"]= readModules()

    students.append(currentStudent)


doAdd(students)
doAdd(students)
print (students)
