#to know in which line python is written
mine = True
i=1
with open("D:\Python Programs\_9_\_6log.txt") as f:
    while mine:
        mine=f.readline()
        # to convert python in any case into lower case.
        mine.lower()
        if "python" in mine:
            print("Python is there in file on line number ",i)
            print(mine)
        i=i+1