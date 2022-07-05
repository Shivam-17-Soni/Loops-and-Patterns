# Program to replace list of words with different string in another file.

words=["donkey","kaddu","mota","putku"]
with open("D:\Python Programs\_9_\_5.txt") as f:
    content=f.read()

for word in words:
    content=content.replace(word,"######$@!^&")

with open("D:\Python Programs\_9_\_5.txt","w") as f:
    f.write(content)