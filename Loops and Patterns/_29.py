# Program to print below pattern:
#         1
#       2 1 2
#     3 2 1 2 3
#   4 3 2 1 2 3 4
#     3 2 1 2 3 
#       2 1 2
#         1

n=4
a=(n//2)
for i in range(1,(n//2)+1):
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
a=0
for i in range((n//2+1),0,-1):
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