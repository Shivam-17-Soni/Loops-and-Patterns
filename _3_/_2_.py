# Program to print letter in given format.

Letter = '''Dear <|NAME|>,
\tYOu are selected!

\tDate : <|DATE|>
'''
a=input("Enter Your Name : ")
b=input("Enter Date : ")
Letter = Letter.replace("<|NAME|>",a)
Letter = Letter.replace("<|DATE|>",b)
print(Letter)