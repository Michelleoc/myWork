# Basic analysis of the grades.csv file
# Author : Michelle O'Connor

import pandas as pd

# path = "../data/" if the file was in a different subfolder
path = ""
filenameForGrades = path + "grades.csv"

df = pd.read_csv(filenameForGrades, index_col=0)
df.dropna(inplace=True) # removes NaN
df.drop_duplicates(inplace=True) # removes duplicates
print (df)

meanValues = df.groupby('subject').mean()
print(meanValues)

sumValues = df.groupby('name').sum()
print(sumValues)

# could be mean, min, max, sum
# this will be useful for project

