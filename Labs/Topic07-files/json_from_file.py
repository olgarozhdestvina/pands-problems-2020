# Olga Rozhdestvina
#  function that will read in a dict object from file. 

import json

filename = "testdict.json"

def readDict():
    with open (filename) as f:
        return json.load(f)

print(readDict())