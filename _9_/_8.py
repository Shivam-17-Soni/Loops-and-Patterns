# to make a copy of file this.txt

with open("D:\\Python Programs\\_9_\\this.txt") as f:
    copy=f.read()

with open("D:\Python Programs\_9_\copy.txt","w") as f:
    f.write(copy)