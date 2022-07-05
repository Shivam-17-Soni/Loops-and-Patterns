# Program to replace a word with different string in another file.

with open("D:\Python Programs\_9_\_4.txt") as f:
    content=f.read()

content=content.replace("donkey","######$@!^&")

with open("D:\Python Programs\_9_\_4.txt","w") as f:
    f.write(content)
