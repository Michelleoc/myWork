# Demonstart reading from TSV and excel
# Author : Michelle O'Connor

import pandas as pd
import re
import numpy as np
import dataManipulation

filename = "originalData.tsv"

df = pd.read_table(filename)
listofCols = ["Module ID", "Duration"] 
print (df[listofCols].head(2))

# print (df[["Module ID", "Duration"]].head(2))

# head(2) - gives the first two rows
# [Module ID] = gives you just the column calld Module ID
# if adding more than one column, need to pass in as list ["Module ID", "Duration"] within the [] brackets


# make a new column
df["New"] = df["Duration"] * df["Number of Weeks"]

listofCols = ["Number of Weeks", "Duration", "New"] 
print (df[listofCols].head(10))

# sets don't allow for duplicates, can only have unique values

'''
def getSeriesOfUnique(dataFrame, nameOfCol, delim = '/'):

    # drop na gets rid of the values in the series that have no value
    # this actually returns a numpy.ndarray
    valuesWithDelims = dataFrame[nameOfCol].dropna().unique()

    # iterate through it and break up the delimited values
    # I am using a set becaue this will remove duplicates as I add them
    # yes I am sure there is a more efficient way of doing this
    uniqueValues = set([])  # empty set
    for valueInCol in valuesWithDelims:
        #print (staff, ":", type(staff)) # for debugging
        valueAsList = re.split('/', valueInCol)
        uniqueValues.update(valueAsList)
    ds = pd.Series(list(uniqueValues))
    # I take the liberty of sorting this series
    ds.sort_values()
    return ds
'''