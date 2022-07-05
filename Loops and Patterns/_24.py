# Program to print below pattern:

# *****
#  ***
#   *
#   *
#  ***
# *****

n=4
a=0
for i in range(n,0,-1):
    print(" "*a,"*"*((2*i)-1))
    a+=1
a-=1
for i in range(1,n+1):
    print(" "*a,"*"*((2*i)-1))
    a-=1


print(end="\n\n\n")


# Program to print below pattern:

# *****
#  ***
#   *
#  ***
# *****

n=4
a=0
for i in range(n,0,-1):
    print(" "*a,"*"*((2*i)-1))
    a+=1
a-=2
for i in range(2,n+1):
    print(" "*a,"*"*((2*i)-1))
    a-=1