import json

#Getting the words and defs from a json file
#Make it into our own dictionary
data = json.load(open("data.json"))

#We have it in keys and values so let us make a function to help with that
def findDef(word):
    return data[word]

word = input("Enter word: ")


print(f"The definition is:  {findDef(word)}")
##print(translate(word))