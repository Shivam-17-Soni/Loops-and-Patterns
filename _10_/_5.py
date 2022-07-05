class Train:
    no_of_seat=100

    @staticmethod
    def status():
        print("")
        print("")
        print("")
        print("")
        print("")
        print("******************")
        print("******************")
        print("******************")
        print("******************")
        print("******************")
        print("Welcome to Railway Ticket Reservation Window.")

    def __init__(self,trainname,fare,seats):
        self.trainname=trainname
        self.fare=fare
        self.seats=seats
        print("")
        print("******************")
        print("Train's Information :")
        print(f"No. of seat available is : {self.no_of_seat} ")
        print(f"Name of Train is : {self.trainname} ")
        print(f"Price of one ticket is : Rs {self.fare} ")
        print(f"No. of seat You want is : {self.seats} ")

    def bookTicket(self):
        if (self.no_of_seat>0):
            print(f"Your tickets are booked.")
            self.no_of_seat=self.no_of_seat - 1
        else:
            print("Sorry this train is full. Kindly Go for tatkal ticket.")



class Passenger:
    def __init__(self,name,age,dob,from_place,to_place,when,which_class):
        self.name=name
        self.age=age
        self.dob=dob
        self.from_place=from_place
        self.to_place=to_place
        self.when=when
        self.which_class=which_class
        print("")
        print("******************")
        print("Passengers Information :")

    def passenger_info(self):
        print(f"Name of passenger is : {self.name}")
        print(f"Age of passenger is : {self.dob}")
        print(f"Date of Birth of  passenger is : {self.dob} ")
        print(f"Passenger is going to {self.to_place} from {self.from_place} .")
        print(f"Date of journey is : {self.when}")
        print(f"Travelling class in train of passenger is : {self.which_class}")


a=input("Enter Name of passenger : ")
b=int(input("Enter Age of passenger : "))
c=input("Enter Date of Birth of  passenger (in dd.mm.yyyy form) : ")
d=input("Enter from where you wnat to go : ")
e=input("Enter where you wnat to go : ")
f=input("Enter Date on which you want to go (in dd.mm.yyyy form) : ")
g=input("In which class you wnat to travel [Class are : 1st Ac, 2nd Ac, 3rd Ac, Slepper, General] : ")


ta=input("Enter Name of Train in which you want to travel : ")
tb=1
tar=Train(ta,350,tb)
tar.status()
tar.bookTicket()

pas=Passenger(a,b,c,d,e,f,g)
pas.passenger_info()