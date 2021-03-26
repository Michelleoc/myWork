# testing reading a CSV
# Author : Michelle O'Connor

import csv

filename = "test.csv"

with open (filename, "rt") as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ",")
    firstLine = True
    for line in csvReader:
        if firstLine:
            firstLine = False
            continue 
        print (line[2]) # this will print out the 3rd element

# each line is an array
