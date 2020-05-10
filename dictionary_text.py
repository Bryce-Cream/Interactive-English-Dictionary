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
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        #Change this later to maybe have if the word entered starts with y or n
        response = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0]).upper()
        
        if response == "Y":
            return data[get_close_matches(w, data.keys())[0]] #User agrees this was the best match
        elif response == "N":
            return "The word doesn't exist. Please double check your spelling"
        else:
            return "We didn't understand your response"
    else:
        return "The world doesn't exist. Please double check it."

word = input("Enter word: ")

output = findDef(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)