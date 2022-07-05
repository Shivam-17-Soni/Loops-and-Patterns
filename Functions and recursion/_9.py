# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
# Print the decimal value of each fraction on a new line with  places after the decimal.


def plusMinus(arr):
    # Write your code here
    p,ng,z=0,0,0
    for i in range(n):
        if arr[i]>0:
            p+=1
        elif arr[i]<0:
            ng+=1
        else:
            z+=1
    p,ng,z=(p/n),(ng/n),(z/n)
    ar=[p,ng,z]
    for i in range(3):
        print(f"{ar[i]:.6f}")
        #print(round(ar[i],6))

if __name__ == '__main__':
    n = int(input("Enter no of elements in list : \n"))

    arr = eval(input("Enter the list : \n"))

    plusMinus(arr)