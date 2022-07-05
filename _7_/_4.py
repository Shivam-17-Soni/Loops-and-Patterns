# Program to calculate sum of first n natural number.

n=int(input("Enter a number : "))
i=n
while i!=1:
    n=n+(i-1)
    i=i-1
print("Sum of first n natural number is",n)