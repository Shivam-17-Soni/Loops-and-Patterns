# Program to check wheather a number is a Armstrong number or not.

a=int(input("Enter a number : "))
b=a
sum=0
i=a%10                  # To get the last or unit digit number.
sum=sum+(i**3)
while (a//10)!=0:
    a=a//10             # To eliminate unit digit or last number every time and get the 1-digit less number.
    i=a%10              # To get the number after last or unit digit number.
    sum=sum+(i**3)
if sum==b:
    print("It is a Armstrong Number.")
else:
    print("It is not a Armstrong Number.")