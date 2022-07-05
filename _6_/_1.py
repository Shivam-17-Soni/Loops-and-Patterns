# Program to get greater number among given four numbers.

a1=int(input("Enter number 1:"))
a2=int(input("Enter number 2:"))
a3=int(input("Enter number 3:"))
a4=int(input("Enter number 4:"))

if (a1>a4):
    f1 = a1
else:
    f1=a4

if (a2>a3):
    f2=a2
else:
    f2=a3

if (f1>f2):
    print("Gretest number among entered 4 numbers is :",f1)
else:
    print("Gretest number among entered 4 numbers is :",f2)
