# Program to check wheather a given student is pass or fail.
#  He will fail if his total percentage is less than 40 or if he gets less than 33 marks in any subject.

n1=int(input("Enter marks on subject 1 out of hundred :"))
n2=int(input("Enter marks on subject 2 out of hundred :"))
n3=int(input("Enter marks on subject 3 out of hundred :"))

s=(n1+n2+n3)/3
if (s>40) and (n1>33) and (n2>33) and (n3>33):
    print("Pass")
else:
    print("Fail")
