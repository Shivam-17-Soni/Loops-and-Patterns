def readFile(filename):
    try:
        with open(filename,"r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} is not found")
        print("Do you wnat to create a file with the following name?")
        a=input("Enter Yes or No : ")
        if a=="Yes":
            with open(filename,"w") as f:
                f.write("")
                print(f"File {filename} is created.")
        print("Thanks for running the program.")

readFile("1.txt")
readFile("2.txt")
readFile("3.txt")
