name=input("Enter Name : ")
marks=int(input("Enter marks : "))
phone=int(input("Enter your phone number : "))
if len(str(phone))>10 or len(str(phone))<10:
    print("Enter correct phone number with 10 digits.")
    phone=int(input("Enter your phone number : "))
print("The name of student is {}, his marks are {}, and phone number is {}.".format(name,marks,phone))