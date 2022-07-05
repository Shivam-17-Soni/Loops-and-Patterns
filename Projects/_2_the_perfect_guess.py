import random
randNum=random.randint(1,101)
#print(randNum)
n=0
userGuess = None
while userGuess!=randNum:
    userGuess = int(input("Guess a Number and Enter it : "))
    if (userGuess==randNum):
        print("You guessed it right!")
    else:
        print("You guessed it wrong!")
        if userGuess<randNum:
            print("You guessed too less! Enter a larger number.")
        else:
            print("You guessed too more! Enter a lesser number.")
    n+=1
print(f"YOu guessed the number {n} times to guess it right.")

with open("E:\Shivam\Python Programs\Projects\hiscore.txt","r") as f:
    hiscore=int(f.read())

if n<hiscore:
    print("You have broken the High Score.")
    with open("E:\Shivam\Python Programs\Projects\hiscore.txt","w") as f:
        f.write(str(n))
