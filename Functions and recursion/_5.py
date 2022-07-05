# Function to print below pattern.

# ****
# ***
# **
# *

def pat(n):
   while n!=0:
        print("*"*n)
        n=n-1

n=int(input("Enter a number : "))
print(pat(n))