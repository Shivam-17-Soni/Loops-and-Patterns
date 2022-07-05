#  Program to print table from 2 to 20 in a seprate file.
for i in range(2,21):
    with open(f"D:\Python Programs\_9_\_tables_Of_{i}.txt","w") as f:
        for j in range(1,11):
            f.write(f"{i}x{j}={i*j}")
            if j!=10:
                f.write("\n")