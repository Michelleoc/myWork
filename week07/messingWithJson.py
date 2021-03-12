# messing with json (jave script object notation)
# Author : Michelle O'Connor

#json is just for storing data
# python has pickle, not going to use this for now

import json

electricBill = {
    "name" : "Andrew", 
    "amount" : "999"
}

with open ("storeData.json", "wt") as f:
    json.dump(electricBill, f)

# can set the identation json.dumps(x, indent=4)

with open ("storeData.json", "rt") as f:
    readDict = json.load(f)
    print (readDict ["name"])


