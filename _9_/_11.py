# Program to rename any file.

import os

oldname="renamed_by_python.txt"
newname="renamed_by_python1.txt"
with open(oldname) as f:
    cont=f.read()

with open(newname,"w") as f:
    f.write(cont)

os.remove(oldname)