n=int(input("Enter a number : "))
#List Comprehension
l=[str(n*i) for i in range(1,11)]
print(l)
verticalTable="\n".join(l)
print(verticalTable)