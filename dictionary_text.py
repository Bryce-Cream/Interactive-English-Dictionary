import json
from difflib import get_close_matches

#Getting the words and defs from a json file
#Make it into our own dictionary
data = json.load(open("data.json"))

#We have it in keys and values so let us make a function to help with that
def findDef(w):
    w = w.lower() #Case sensitivity
    #Valid word we have
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        return "Did you mean %s instead?" % get_close_matches(w, data.keys())[0]
        ##return "Did you mean {get_close_matches(w, data.keys())[0]} instead?"
    else:
        return "The world doesn't exist. Please double check it."

word = input("Enter word: ")

print(f"The definition is:  {findDef(word)}")