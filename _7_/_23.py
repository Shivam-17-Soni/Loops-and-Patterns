# Program to print below pattern:

# *    *
# **  **
# ******
# **  **
# *    *

n=5
b=1
c=2
for i in range(1,n+1):
    #print("*"*b,end="")
    print("* "*b,"  "*(2*c),*"*"*b)
    if i<((n+1)//2):
        c-=1
        b+=1
    else:
        c+=1
        b-=1