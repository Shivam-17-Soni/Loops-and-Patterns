class Programmer:
    Company="Microsoft"
    def __init__(self,name,product):
        self.name=name
        self.product=product
    def getInfo(self):
        print(f"The name of programmer is {self.name} and the product is {self.product}.")

shivam=Programmer("Shivam","Excel")
harry=Programmer("Harry","Skype")
shivam.getInfo()
harry.getInfo()
