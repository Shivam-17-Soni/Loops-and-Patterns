#Program to print multiplication table of a given number.
#  By for loop

a = int(input("Enter the number : "))
for i in range(1,11):
    print(a,"multiply by",i,"is equal to",a*i)


# By while loop

a = int(input("Enter the number : "))
i=1
while i<11:
    print(f"{a}x{i}={a*i}")
    i=i+1