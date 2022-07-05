# Program to set high score of a game in a seperate file.

def game():
    return 15555

score=game()
f=open("D:\Python Programs\_9_\_2game.txt")
d=f.read()
if f.read()=="" :
    f.close()
    with open("D:\Python Programs\_9_\_2game.txt","w") as d:
        d.write(str(score))
else:
    f.close()
    d=int(d)
    if d<score:
        with open("D:\Python Programs\_9_\_2game.txt","w") as d:
            d.write(str(score))
