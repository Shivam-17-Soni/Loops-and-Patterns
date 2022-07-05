# Snake,Water,Gun Game Or Rock,Paper,Scissors Game.
import random

def gamewin(computer,you):
    # If two values are same then tie.
    if computer==you:
        return None
    # If different then won or lose. Won=True and Lose=False
    elif computer=="s":
        if you=="w":
            return False
        elif you=="g":
            return True
    elif computer=="w":
        if you=="g":
            return False
        elif you=="s":
            return True
    elif computer=="g":
        if you=="s":
            return False
        elif you=="w":
            return True

print(f"Computer's turn : Snake(s),Water(w) or Gun(g) ?")

#Computer randomly choose snake water gun.

randNo=random.randint(1,3)
if randNo==1:
    computer="s"
elif randNo==2:
    computer="w"
else:
    computer="g"

you=input(f"Your turn : Snake(s),Water(w) or Gun(g) ?")
a=gamewin(computer,you)

print("Computer Choose ",computer)
print("You Choose ",you)

if a==None:
    print("The game is tie")
elif a:
    print("You won the the game.")
else:
    print("You lose the the game.")

print("Thank you for playing the game.")
