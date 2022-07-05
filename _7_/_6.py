# Program to print this pattern
#   *
#  ***
# *****

n=2
for i in range(1,6,2):
    print(" "*n,"*"*i," "*n)
    n=n-1



#Alternatively
# n=2
# for i in range(1,6,2):
#     print(" "*n,"*"*i)
#     n=n-1