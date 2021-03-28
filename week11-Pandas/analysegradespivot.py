# Using pivots in analysis of the grades.csv file 
# Author : Michelle O'Connor

import pandas as pd
import matplotlib.pyplot as plt

path = ""
filenameForGrades = path + "grades.csv"

df = pd.read_csv(filenameForGrades, index_col=0)
df.dropna(inplace=True) # removes NaN
df.drop_duplicates(inplace=True) # removes duplicates

df = df.pivot_table(values="grade", index=["name", "subject"], aggfunc="max").reset_index()
# reset_index - removes the 2nd row that appears for John Programmming

print (df)

meanValues = df.groupby('name').mean()

print(meanValues)

df = df.pivot(index="name", columns="subject", values="grade")
print (df.corr()) # to correlate. SIEM is not correlated as there is only occurance of SIEM
df.plot.bar()
plt.show()

# can also have "hist" for histogram
# can also have "scatter" for scatter plot