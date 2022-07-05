# Function to remove any word from the string

def reas(string,word):
    newstr=string.replace(word,"")
    return newstr.strip()

n="   Good Morning Dear   "
a=reas(n,"Dear")
print(a)

#print(n)
#print(n.strip())