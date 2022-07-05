i=True 
sum=0
while(True):
    a=input("Enter prices or q to quit : \n")
    if a!="q":
        a=int(a)
        sum=sum+a
    else:
        print("Thanks for shopping with us.")
        break
print(f"Total bill price is : {sum}.")