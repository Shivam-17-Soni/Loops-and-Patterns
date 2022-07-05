# Program to check wheather a number is a prime number or not.

n = int(input('Enter the number:'))
a=True
for i in range(2,(n//2)+1):
    if n%i==0 and n!=2 :
        print("It is not a prime number.")
        a=False
        break

if a:
    print("It is a prime number.")
