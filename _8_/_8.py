# Function to print table of a number.

def mtply(number):
    for i in range(1,11):
        print(f"{number}x{i} = {number*i}")

n=int(input("Enter a number : "))
a=mtply(n)