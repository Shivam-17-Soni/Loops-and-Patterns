# Program to print below pattern:
#     1
#    212
#   32123
#  4321234
# 543212345

n=5
a=n-1
for i in range(1,n+1):
    print(" "*a,end="")
    b=i
    for j in range((2*i)//2):  # goes from i to 1.
        print(b,end="")
        b-=1
    b+=1
    for j in range(((2*i)//2)-1): # goes from 1 to i.
        b+=1
        print(b,end="")
    print(end="\n")
    a-=1


# Program to print below pattern:
#         1
#       2 1 2
#     3 2 1 2 3
#   4 3 2 1 2 3 4
# 5 4 3 2 1 2 3 4 5

n=5
a=(n-1)
for i in range(1,n+1):
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
    a-=1