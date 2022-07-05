# Program to print below pattern:
# A
# AB
# ABC

n=4
for i in range(1,n+1):
    for j in range(i):
        print(chr(65+j),end="")
    print(end="\n")


# Program to print below pattern:
# A
# BB
# CCC

n=4
for i in range(n):
    print(chr(65+i)*(i+1))


# Program to print below pattern:
#   A
#  A B
# A B C

n=4
a=n-1
for i in range(1,n+1):
    print(" "*a,end="")
    for j in range(i):
        print(chr(65+j)," ",end="")
    print(end="\n")
    a-=1