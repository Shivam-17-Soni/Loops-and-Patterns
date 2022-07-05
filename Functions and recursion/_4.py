# Function for sum of all n natural numbersusing recursion.

def sum(n):
    if (n-1)==0:
        return n
    else:
        n=sum(n-1)+n
        return n

n=int(input("Enter a number : "))
print(sum(n))

#Function for factorial using recursion.

n=int(input("Enter a number : "))
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

print("Factorial of number is : ",fact(n))
