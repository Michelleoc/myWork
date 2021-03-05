# quiz on types
# Author : Michelle O'Connor

numberOfQuestions = 5
averageAge = 23.4
debugMode = True
name = "joe"
ages = []
months = ('Jan', 'Feb', 'Mar')
book = {}
stuff = [12, 'Fred', False, {}]
someone = dict(firstname="joe")
me = {
    "firstName": "Andrew",
    "teaching": [{
        "courseName": "programming",
        "semester": 1
    }, {
        "courseName": "Data Representation",
        "semester": 2
    }
    ]
}

print ("numberOfQuestions is " + str(type(numberOfQuestions)))
print ("averageAge is " + str(type(averageAge)))
print ("debugMode is " + str(type(debugMode)))
print ("name is "+ str (type(name)))
print ("ages is "+ str (type(ages)))
print ("months is "+ str (type(months)))
print ("months [1] "+ str (type(months [1])))
print ("book is "+ str (type(book)))
print ("stuff is "+ str (type(stuff)))
print ("stuff [2] "+ str (type(stuff [2])))
print ("someone is "+ str (type(someone)))
# print ("someone ["firstname"] is "+ str (type(someone ["firstname"])))
print ("me is "+ str (type(me)))
# print ("me ["teaching"] is "+ str (type(me ["teaching"])))
# print ("me ["teaching"] [0] ["semester"] is" "+ str (type(me ["teaching"] [0] ["semester"])))