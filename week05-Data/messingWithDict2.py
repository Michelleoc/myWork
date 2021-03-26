# more messing with dictionaries
# Author : Michelle O'Connor

# Looking at for loops

car = {
    "make": "fiat", 
    "model": "punto", 
    "price" : 10000,
    "tags" : ["pre-owned", "Best Buy", "Dealer"]
}

# print (car)


'''
for key in car:
    print(key, "has a value", car [key])
'''

# another way to type this is 

print (car.items())
for key, value in car.items():
    print(key, "have a value", value)



#print (car.items())
#for pair in car.items():
    #print(pair)
    #print(type(pair))


# tags is a type of array 

# make, model, price and tags are "keys"