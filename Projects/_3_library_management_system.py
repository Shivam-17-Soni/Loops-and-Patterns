class Library:
    def __init__(self,book_list):
        self.books=book_list

    def displayAvailableBooks(self):
        print(f"The Books Available in this library are : ")
        n=1
        for book in self.books:
            print(n,". ",book)
            n+=1
        print("\n")
    def borrowBook(self,bookName):
        #
        if bookName in self.books:
            print(f"You have been issued  {bookName}. Please keep it safe and Return it within 30 Days. Otherwise you have to pay fine according to 10/- per day.")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is not available or someone may have already issued it. Please wait till it is available or Please, Take another Book if you want.")
            return False
    
    def return_book(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning the book. Hope You enjoyed reading it.")


class Student:
    def requestBook(self):
        self.Book=input("Enter the name of Book you want to borrow : ")
        return self.Book
    
    def returnBook(self):
        self.Book = input("Enter the name of book you want to return.")
        return self.Book


if __name__ == "__main__":
    central_Library=Library(["Python","More in SQL","Algorithms","Django","Ethical Hacking for Begineers To Adavance","The Power Of Your Subconsious Mind"])
    student=Student()
    #central_Library.displayAvailableBooks()
    while(True):
        welMsg='''          *****Welcome to Central Library*****          
        
        Pleae choose an option from below :
        1. Listing all the Books
        2. Request a book
        3. Add/Return a book
        4.Exit the library
        '''
        print(welMsg)

        a=int(input("Enter your choice : "))
        try:
            if a==1:
                central_Library.displayAvailableBooks()
            elif a==2:
                central_Library.borrowBook(student.requestBook())
            elif a==3:
                central_Library.return_book(student.returnBook())
            elif a==4:
                print("Thanks! For Coming to Central Library. Have a great day ahead.")
                exit()
            elif a>4 or a==0:
                print("Invalid Choice!")
        except ValueError:
            print("Please enter a number of choice.")
    