# Program to print below pattern:
#   *
#  * *
# *****
a=5
b=1
n=a-1
for i in range(1,a+1):
    print(" "*n,"*",end="")
    if i==a:
        print("*"*(2*i-1))
    elif i!=1:
        print(" "*b,"*",end="")
        b+=2
    n=n-1
    print(end="\n")