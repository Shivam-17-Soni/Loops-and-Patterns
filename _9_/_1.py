# Program to open a file and check wheather "twinkle" word is present in it or not.

f=open('_9_\_1poem.txt','r')
t=f.read()
if "twinkle" in t:
    print("Twinkle is present")
else:
    print("Twinkle is absent")
f.close()