import json
from difflib import get_close_matches as match
import time,sys

#To use the dictionary, you need to download the json file I uploaded.

data = json.load(open("data.json")) 

def dictionary(word):
    word = word.lower()
    if(word in data):
        return data[word]
    elif(len(match(word, data.keys(), cutoff=0.8)) > 0):
        answer = input(f"Did you mean {match(word, data.keys())[0]} ? Y/N: ")
        if(answer=="Y" or answer=="y"):
            return data[match(word, data.keys())[0]]
        elif(answer=="N" or answer=="n"):
            return "The word does not exist!"
        else:
            return "Error!"

    else:
        return "The word does not exist!"

def exit():
    print("Exiting")
    time.sleep(.3)
    print(".")
    time.sleep(.3)
    print("..")
    time.sleep(.3)
    print("...")
    sys.exit()

word = input("Enter word: ")
output = dictionary(word)
print("*"*32)

if(type(output)==list):

    for i in output:
        print(i)
else:
    print(output)
    
    
while True:
    print("*"*32)
    continue_word=(input("Do You Want To Continue? Y/N: "))
    if continue_word=="Y" or continue_word=="y":
        word = input("Enter word: ")
        output = dictionary(word)
        print("*"*32)
        if(type(output)==list):

            for i in output:
                print(i)
        else:
            print(output)
    
    elif continue_word=="N" or continue_word=="n":
         exit()
         
    else:
        print("Please just write Y or N")     