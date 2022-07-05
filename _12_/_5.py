n=int(input("Enter a number : "))
#List Comprehension
l=[n*i for i in range(1,11)]
print(l)

with open("table.txt","a") as f:
    f.write(f"Table of {n} is {str(l)}")
    f.write("\n")