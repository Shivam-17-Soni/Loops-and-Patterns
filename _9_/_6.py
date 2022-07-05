# Program to check wheather a word is there in a particular file or not.

with open("D:\Python Programs\_9_\_6log.txt") as f:
    mine=f.read()
# to convert python in any case into lower case.
mine.lower()
if "python" in mine:
    print("Python is there in file.")
else:
    print("Python is not there in file.")