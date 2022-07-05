# Program to make a dictionary containing english names of hindi items and give print of the entered hindi item.

mydict={"Pankha":"fan" ,
    "dabba":"box" ,
    "kutta":"dog" ,
    "billi":"cat" ,
    "tel":"oil"
}
print("Options are : ",mydict.keys())
a=input("Enter the Hindi words to know their English Meaning. Options are above:\n")
# print("The engish name of word you searched is",mydict[a])
# Below line will not throw an error if key is not present but above line will throw error.
print("The engish name of word you searched is",mydict.get(a))