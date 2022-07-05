with open("E:\Shivam\Python Programs\Projects\currency_data.txt") as f:
    lines=f.readlines()

my_dict={}
my_dict1={}
for line in lines:
    p=line.split("\t")
    my_dict[p[0]]=p[1]
    my_dict1[p[0]]=p[2]

i=0
for item in my_dict1.keys():
    i=i+1
    print(f"{i}.{item}")

convert=input("Enter the name of the currency you use : \n")

amount=int(input("Enter the amount you want to convert : \n"))
b=amount *float(my_dict1[convert])
#[print(item) for item in my_dict.keys()]
i=0
for item in my_dict.keys():
    i=i+1
    print(f"{i}.{item}")

convert1=input("Enter the name of the currency you want to convert this amount to? Available Options :\n")
print(f"{amount} {convert} is equal to {b *float(my_dict[convert1])} {convert1}.")