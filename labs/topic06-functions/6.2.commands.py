# messing with commands
# Author : Michelle O'Connor

# \t indent or tabs a space

def displayMenu ():
    print ("What would you like to do?")
    print ("\t (a) Add new student")
    print ("\t (v) View students")
    print ("\t (q) Quit")
    choice = input ("Type one letter (a/v/q):").strip()

    return choice

choice = displayMenu ()
print ("you chose {}".format(choice))