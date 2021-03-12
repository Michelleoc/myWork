# write json that will store a simple Dict to a file as JSON 
# Author : Michelle O'Connor

import json

filename="testdict.json"

sample= dict(name='michelle', age=25, grades=[1,74,65])

def writeDict(obj):
    with open(filename, 'wt') as f:
        json.dump(obj,f)


writeDict(sample)