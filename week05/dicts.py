# messing with dictionaries
# Author : Michelle O'Connor

car = {
    "make": "ford", 
    "price": 123}

print (type(car))
print (car)

car ["model"]= "focus"
print(car)


make = car ["make"]
notMake = car.get("sasjsjjs")
print (notMake)
print (make)