class Calculator:
    def __init__(self,num):
        self.number=num
    def sqr(self):
        print(f"The square of entered number is {self.number**2}.")
    def cube(self):
        print(f"The cube of entered number is {self.number**3}.")
    def sqr_root(self):
        print(f"The square root of entered number is {self.number**(1/2)}.")

n=int(input("Enter a number : "))
s=Calculator(n)
s.sqr()
s.cube()
s.sqr_root()