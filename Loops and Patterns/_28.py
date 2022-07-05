# Program to print below pattern:

#   4 3 2 1 2 3 4
#     3 2 1 2 3 
#       2 1 2
#         1

n=4
a=0
for i in range(n,0,-1):
    print("   "*a,end="")
    b=i
    for j in range((2*i)//2):  # goes from i to 1.
        print(b," ",end="")
        b-=1
    b+=1
    for j in range(((2*i)//2)-1): # goes from 1 to i.
        b+=1
        print(b," ",end="")
    print(end="\n")
    a+=1


# Program to print below pattern:

# *   *
#   *
# *   *

n=3
for i in range(n):
    for j in range(n):
        if (i+j)%2==0:
            print("* ",end="")
        else:
            print("  ",end="")
    print(end="\n")


# Program to print below pattern:

#     *
#   *
# *   *

n=3
a=n-1
for i in range(n):
    print("  "*a,"* ",end="")
    if i==n-1:
        print(" "*i,"*")
    a-=1
    print(end="\n")