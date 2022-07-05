# Program to print below pattern:
#     0
#    10
#   210
#  3210

n=4
a=n-1
for i in range(1,n+1):
    print(" "*a,end="")
    b=i-1
    for j in range(i):
        if j==(i-1):
            print(b,end="\n")
        else:
            print(b,end="")
        b-=1
    a-=1


# Program to print below pattern:
# 0
# 10
# 210
# 3210

n=4
a=n-1
for i in range(1,n+1):
    b=i-1
    for j in range(i):
        if j==(i-1):
            print(b,end="\n")
        else:
            print(b,end="")
        b-=1
    a-=1


# Program to print below pattern:
# 0
# 10
# 101
# 0101

n=4
a=n-1
b=2
for i in range(1,n+1):
    for j in range(i):
        if j==(i-1):
            print(b%2,end="\n")
        else:
            print(b%2,end="")
        b+=1
    a-=1


# Program to print below pattern:
# 0
# 01
# 101
# 0101

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        if ((i+j)%2)==0:
            print("1",end="")
        else:
            print("0",end="")
    print(end="\n")