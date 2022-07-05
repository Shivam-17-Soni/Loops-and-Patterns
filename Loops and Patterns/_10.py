# Program to print below pattern:
#     *****
#    *****
#   *****
#  *****
# *****

n=5
a=n-1
for i in range(n):
    print(" "*a,"*"*5)
    a-=1