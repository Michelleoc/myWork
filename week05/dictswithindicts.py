# messing with dictionaries
# Author : Michelle O'Connor

car = {
    "make": "ford", 
    "price": 123, 
    "owner" : {
        "firstName" : "Fred", 
        "age" : 12
    }
    }

print (type(car))
print (car)

car ["model"]= "focus"
print(car)

print (car["owner"]["age"])