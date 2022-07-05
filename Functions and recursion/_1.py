# Function to find max of three numbers.

def  maximum(num1,num2,num3):
    if (num1>num2):
        if (num1>num3):
            return num1
        else:
            return num3
    else:
        if (num3>num2):
            return num3
        else:
            return num2
num1=int(input("Enter number 1 : "))
num2=int(input("Enter number 2: "))
num3=int(input("Enter number 3 : "))
m=maximum(num1,num2,num3)
print("The value of the maximum is ",m)