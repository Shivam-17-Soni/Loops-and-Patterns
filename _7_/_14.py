# Program to print below pattern:
#   *
#  ***
# *****
#  ***
#   *

a=5
b=1
n=(a+1)//2
for i in range(1,a+1):
    print(" "*n,"*",end="")
    if i!=1 and i!=a:
        print("*"*(2*b-2),end="")
    if i<=(a/2):
        n=n-1
        b+=1
    else:
        n=n+1
        b-=1
    print(end="\n")