# Program to check wheather two files are identical or not.

with open('D:\\Python Programs\\_9_\\this.txt') as f:
    c=f.read()

with open("D:\Python Programs\_9_\copy.txt",) as f:
    d=f.read()
if c==d:
    print("It is identical.")
else:
    print("It is not identical.")
