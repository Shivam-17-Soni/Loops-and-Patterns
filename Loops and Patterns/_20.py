# Program to print below pattern:
# *
# **
# ***
# **
# *

n=5
b=1
for i in range(1,n+1):
    print("*"*b)
    if i<((n+1)//2):
        b+=1
    else:
        b-=1


# Program to print below pattern:
#   *
#  **
# ***
#  **
#   *

n=5
b=1
c=2
for i in range(1,n+1):
    print("  "*c,*"*"*b)
    if i<((n+1)//2):
        c-=1
        b+=1
    else:
        c+=1
        b-=1