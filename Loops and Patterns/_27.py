# Program to print below pattern:
#   A
#  B B
# C   C
#  D D
#   E


a=5
b=1
n=(a+1)//2
print(n)
for i in range(1,a+1):
    print(" "*n,chr(64+i),end="")
    if i!=1 and i!=a:
        print(" "*b,chr(64+i),end="")
        if i<=(a/2):
            b+=2
        else:
            b-=2
            n=n+1
    if i<=(a/2):
        n=n-1
    print(end="\n")