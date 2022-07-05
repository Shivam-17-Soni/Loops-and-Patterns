# Program to print below pattern:

#  **************
#  **************
#  **************
#  **************
#  **************

n=5
for i in range(n):
    print("*"*(n+7))


# Program to print below pattern:
#    *
#   * *
#  * * *
# *     *

a=2
b=1
n=a-1
for i in range(1,a+1):
    print(" "*n,"*",end="")
    if i==(a//2)+1:
        print(" *"*(i-1),end="")
        b+=2
    elif i!=1:
        print(" "*b,"*",end="")
        b+=2
    n=n-1
    print(end="\n")