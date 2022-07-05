# Program to print below pattern:
# *****
#  ***
#   *
n=3
a=0
for i in range(n,0,-1):
    print(" "*a,"*"*((2*i)-1))
    a+=1


print(end="\n\n\n")

# Program to print below pattern:
# * * *
#  * *
#   *
n=3
a=0
for i in range(n,0,-1):
    print(" "*a,end="")
    for j in range(i):
        print("*"," ",end="")
    print(end="\n")
    a+=1