# Program to print this pattern
# *
# **
# ***
for i in range(1,4):
    print("*"*i)


print(end="\n\n\n")

# Program to print this pattern
#    *
#   **
#  ***

n=3
for i in range(1,n+1):
    print(" "*(n-i),"*"*i)


print(end="\n\n\n")

# Program to print this pattern
#  ***
#   **
#    *

n=3
for i in range(n,0,-1):
    print(" "*(n-i),"*"*i)


print(end="\n\n\n")

# Program to print this pattern
#  ***
#  **
#  *

n=3
for i in range(n,0,-1):
    print("*"*i)