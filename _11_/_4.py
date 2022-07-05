class Complex:
    def __init__(self,num,i):
        self.real=num
        self.imaginary=i
    def __add__(self,c):
        return Complex(self.real + c.real, self.imaginary + c.imaginary)
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

    def __mul__(self,c):
        mreal=(self.real*c.real - self.imaginary*c.imaginary) # (a+bi)(c+di) = (ac-bd)+ (ad+bc)i
        mimag=(self.real*c.imaginary + self.imaginary*c.real)
        return Complex(mreal , mimag)
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

c1=Complex(3,2)
c2=Complex(1,7)
print(c1+c2)
print(c1*c2)
