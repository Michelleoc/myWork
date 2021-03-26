# demonstrate reading from TSV and excel
# Author : Michelle O'Connor

import pandas as pd
import re
import numpy as np
import dataManipulation

filename = 'originalData.tsv'
# tsv tab separated
workbookFileName = 'timetableData.xlsx'
df = pd.read_table(filename)
# if want to read csv you say read_csv

df.to_excel(workbookFileName, sheet_name='activities', index=False)

ds_staff = dataManipulation.getSeriesOfUnique(df, 'Staff (delimited)')

#print (ds_staff) # debug I should use logging
# we have to use a different engin (openpyxl) to append to the book
with pd.ExcelWriter(workbookFileName, engine='openpyxl', mode='a') as writer:
    ds_staff.to_excel(writer, sheet_name="staff", index=False)


# openpyxl is good for formatting of excel sheets
# mode = a is to append
