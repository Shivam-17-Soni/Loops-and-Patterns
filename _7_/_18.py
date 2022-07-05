# Program to print below pattern:
#     0
#    12
#   345
#  6789

n=4
a=n-1
b=0
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

n=6
a=n-1
b=1
for i in range(1,n+1):
    for j in range(i):
        if j==(i-1):
            print(b," ",end="\n")
        else:
            print(b," ",end="")
        b+=1
    a-=1


# Program to print below pattern:
#     0
#    01
#   012
#  0123

n=4
a=n-1
for i in range(1,n+1):
    b=0
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
# 12
# 123
# 1234

n=6
a=n-1
for i in range(1,n+1):
    b=1
    for j in range(i):
        if j==(i-1):
            print(b,end="\n")
        else:
            print(b,end="")
        b+=1
    a-=1


# Program to print below pattern:
#     0
#    01
#   012
#  0123

n=4
a=n-1
for i in range(1,n+1):
    b=n
    print(" "*a,end="")
    for j in range(i):
        if j==(i-1):
            print(b,end="\n")
        else:
            print(b,end="")
        b-=1
    a-=1

# Program to print below pattern:
# 1234
# 123
# 12
# 1

n=6
a=n-1
for i in range(1,n+1):
    b=n
    for j in range(i):
        if j==(i-1):
            print(b,end="\n")
        else:
            print(b,end="")
        b-=1
    a-=1