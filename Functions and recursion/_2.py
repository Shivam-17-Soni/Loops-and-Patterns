# Function to convert celcieus to fahrenheit.

def converter(num1):
    a=(num1*(9/5)) + 32
    return a

num1=int(input("Enter the value to convert into fahrenheit : "))
print(converter(num1))
