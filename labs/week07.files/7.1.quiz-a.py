# the with statement will automatically close the file when it is finished with it

with open("test-a.txt",'wr') as f:
    data = f.read()
    print (data)


# nothing will happen as it is asking to read a file that does not exist

# this is the same as
# f = open ("test1.txt")
# data = f.read()
# print(data)
# f.close()