a=int(input("Enter First Number : "))
b=int(input("Enter Second Number : "))
if a==0 and b==0:
    print("No Answer. Please enter number other than zero at both numerator or denominator.")
try:
    print(a/b)
except ZeroDivisionError:
    print("Infinte")
