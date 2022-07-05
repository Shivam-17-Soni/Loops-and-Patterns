# Program to print this print:
# ####
# #  #
# #  #
# ####

n=int(input("Enter a number : "))
j=n-2
for i in range(1,n+1):
    if i==1 or i==n:
        print("#"*n )
    else:
        print("#"*1," "*j,"#"*1)