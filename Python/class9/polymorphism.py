# Polymorphism:

class Grant_Parent:
    assets = ["Home", "Farm", "GuestHouse"]

    bank_balance = 1500  

    def hair_color(self):
        print("Hair color is White") 

class Parent(Grant_Parent):
    car = "Honda City"
    bank_balance = 2000000  

    def hair_color(self):
        print("Dad hair color is Brownie") 

class Child(Parent):
    bike = "Dio"
    degree = "Engineering"

    def hair_color(self):
        print("hair color black")

c1 = Child()

c1.hair_color()
print(c1.bank_balance)