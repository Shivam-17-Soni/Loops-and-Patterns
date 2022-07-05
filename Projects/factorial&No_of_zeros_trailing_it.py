a=int(input("Enter the number to get its factorial : "))
fact=1
if a==0:
    fact=1
else:
    for i in range(1,(a+1)):
        fact=fact*i
print("Factorial of the given number is ",fact)

fact=str(fact)
zeroes=0
for i in range(1,len(fact)):
    a=fact[-i]
    if a=="0":
        zeroes+=1
    else:
        break
print("No. of trailing zeroes are ",zeroes)

# another approach

def factorial(number):
    if number==0 or number==1:
        return 1
    else:
        return number*factorial(number-1)

def factoralTrailingZeros(number):
    #fac=factorial(number)
    count=0
    i=5
    while(number//i !=0):
        count+=int(number/i)  # No. of zeroes is equal to number of pairs of 2 and 5. Here we count no. of 5 as 2 is present in every 2nd no. in form of even no.
        i=i*5
    #while(fac%10 ==0):
    #   count=count+1
    #    number=number/10
    return count

if __name__=='__main__':
    number = int(input("Enter a number :\n"))
    fac=factorial(number)
    print("Factorial of the given number is ",fac)
    fac_zeroes=factoralTrailingZeros(number)
    print("No. of trailing zeroes are ",fac_zeroes)
