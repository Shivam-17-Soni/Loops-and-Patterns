# Program to print pascal's triangle :

#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

n=5
for i in range (n):
    print("  "*(n-i),end="")
    a=1
    for j in range(i):
        print(a," ",end="")
        a=a*(i-j)//(j+1)
    print("1",end="\n")