# Program to print below pattern:
# ABC
# AB
# A

n=4
for i in range(n,0,-1):
    for j in range(i):
        print(chr(65+j),end="")
    print(end="\n")


print(end="\n\n\n")


# Program to print below pattern:

# ABC
# AB
# A
# A
# AB
# ABC

n=4
for i in range(n,0,-1):
    for j in range(i):
        print(chr(65+j),end="")
    print(end="\n")

for i in range(1,n+1):
    for j in range(i):
        print(chr(65+j),end="")
    print(end="\n")


print(end="\n\n\n")


# Program to print below pattern:

# ABC
# AB
# A
# AB
# ABC

n=4
for i in range(n,0,-1):
    for j in range(i):
        print(chr(65+j),end="")
    print(end="\n")

for i in range(2,n+1):
    for j in range(i):
        print(chr(65+j),end="")
    print(end="\n")