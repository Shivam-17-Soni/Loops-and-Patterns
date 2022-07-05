# Program to print below pattern:
#     1
#    2 2
#   3 3 3
#  4 4 4 4
# 5 5 5 5 5

n=5
a=n-1
for i in range(1,n+1):
    print(" "*a,end="")
    for j in range(i):
        if j==(i-1):
            print(i,end="\n")
        else:
            print(i,end="")
            print(" ",end="")
    a-=1


# Program to print below pattern:
#     1
#    22
#   333
#  4444
# 55555
n=6
a=n-1
for i in range(1,n+1):
    print(" "*a,end="")
    for j in range(i):
        if j==(i-1):
            print(i,end="\n")
        else:
            print(i,end="")
    a-=1


# Program to print below pattern:
# 1
# 22
# 333
# 4444
# 55555
n=6
a=n-1
for i in range(1,n+1):
    for j in range(i):
        if j==(i-1):
            print(i,end="\n")
        else:
            print(i,end="")
    a-=1


# Program to print below pattern:
#     1
#    23
#   456
#  78910

n=4
a=n-1
b=1
for i in range(1,n+1):
    print(" "*a,end="")
    for j in range(i):
        if j==(i-1):
            print(b,end="\n")
        else:
            print(b,end="")
        b+=1
    a-=1

# Program to print below pattern:
# 1
# 23
# 456
# 78910

n=4
a=n-1
b=1
for i in range(1,n+1):
    for j in range(i):
        if j==(i-1):
            print(b,end="\n")
        else:
            print(b,end="")
        b+=1
    a-=1