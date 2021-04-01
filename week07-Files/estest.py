
filename = "moby-dick.txt"

l = "e"

# https://www.sanfoundry.com/python-program-read-file-counts-number/
# or alternatively we could have asked the user to input their desired letter

# l=input("Enter letter to be searched:")

k = 0 

with open(filename, "rt") as f:
    # A for loop is used to read through each line in the file
    for line in f:
        # I am working on the assumption that they want Upper and Lower case of the letter e
        # So this is to convert upper to lower case 
        # https://stackoverflow.com/questions/14067267/lower-case-from-a-text-file
        line = line.lower()
        # Each line is split into a list of words using split ()
        words = line.split()
        # A loop is used to work through the words and another loop to woek through the letters in the word
        for i in words:
            for letter in i:
                # If the letter equals our input "l" then the letter count is incremented 
                if(letter==l):
                    k=k+1
                    
print("Occurrences of the letter:")
print(k)

# https://www.sanfoundry.com/python-program-read-file-counts-number/