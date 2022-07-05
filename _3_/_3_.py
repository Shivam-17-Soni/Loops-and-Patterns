# Program to find number of whitespaces and double whitespaces in the strings.

a=input("Enter Your a string : ")
b=a.count(" ")
c=a.find(" ")
print("Number of white space is ",b)
print("First white space is at ",b)

b=a.count("  ")
c=a.find("  ")
print("Number of double white space is ",b)
print("First double white space is at ",b)