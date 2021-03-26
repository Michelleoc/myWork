# messing with functions
# Anonymous functions
# Author : Michelle O'Connor

def doubler (num):
    return num *2

def triple (num):
    return num * 3

isMax = True
# is Max = False then it will return the tripler value
if isMax: 
    fun = doubler 
else:
    fun = tripler

var = fun(10)

print (var)