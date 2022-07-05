import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation
    #while True:
    #    try:
    #        plen = int(input("Enter the password length \n"))
    #        break
    #    except ValueError :
    #        print("Oops! That's not the valid number. Please try again...")

    plen = int(input("Enter password length : \n")) # Todo1: Handle Gibbersish
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    #print(s)
    random.shuffle(s)
    #print(s)
    print("Your password is : ")
    print("".join(s[0:plen]))

    # Alternatively we can use "sample" instead of "shuffle". Below is its code.
    #print("".join(random.sample(s,plen)))