with open("E:\Shivam\Python Programs\Projects\currency_data.txt") as f:
    lines=f.readlines()

my_dict={}
for line in lines:
    p=line.split("\t")
    my_dict[p[0]]=p[1]

amount=int(input("Enter the amount you want to convert : \n"))
#[print(item) for item in my_dict.keys()]
i=0
for item in my_dict.keys():
    i=i+1
    print(f"{i}.{item}")

convert=input("Enter the name of the currency you want to convert this amount to? Available Options :\n")
print(f"{amount} INR is equal to {amount *float(my_dict[convert])} {convert}.")