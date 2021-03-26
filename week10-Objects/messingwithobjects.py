# messing with objects
# Author : Michelle O'Connor

class Nameofclass:
    name = "" # all will have a name attribute
    last = ""
    def getfullname(self): # can put in functions
        return self.name + " " + self.last  
    # pass

# good idea to define attributes
# pass to say there is nothing in the class


inst = Nameofclass()
inst2 = Nameofclass()

inst.name = 'Michelle'
inst2.last = 'OConnor'
person = inst 
# when you make one variables equal another variable, sometimes it is a reference another one and sometimes it is a new value of another

print(person.name)

inst.last = "bloks"
print (person.getfullname())

str1 = "blah de blah"
str2 = str1
str1 += " with bells on top"
print (str2)

# if str 2 was equal to blah de blah it is passed by value - this was the outcome
# if str 2 was equal to with bells on top so it passed by reference 