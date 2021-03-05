# Create a program that puts 10 random numbers into a queue(list) 
# the program should then output all the values in the queue 
# then take the numbers from the queue one at a time
# print it and the current numbers still in the queue 
# the command pop(0) takes the first element out of a list
# Author: Michelle O'Connor


import random
# Returns a random float number between 0 and 1

queue = []
# [] list
numberOfNumbers = 10
rangeTo = 100

for n in range(0, numberOfNumbers):
    queue.append(random.randint(0, rangeTo))

print("queue is {}".format(queue))

while len(queue) != 0:

    currentNumber = queue.pop(0)
    print("current Number is {} and the queue is {} ".format(currentNumber, queue))

print("the queue is now empty")