# Program to check whether text is talking about harry or not.

a=input("Enter the text :\n")
if ("harry" in a) or ("Harry" in a) or ("hARRY" in a) or ("harry" in a):
    print("Talking about Harry.")
else:
    print("Not talking about Harry.")