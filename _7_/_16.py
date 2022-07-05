# Program to print below pattern:
#   *
#  * *
# * * *
#  * *
#   *

a=5
b=1
c=n=(a+1)//2
for i in range(1,a+1):
    print(" "*n,"*",end="")
    if i!=1 and i!=a:
        if i!=c:
            print(" "*b,"*",end="")
        if i==c:
            for j in range(1,i):
                print(" ","*",end='')
        if i<=(a/2):
            b+=2
        else:
            b-=2
            n=n+1
    if i<=(a/2):
        n=n-1
    print(end="\n")