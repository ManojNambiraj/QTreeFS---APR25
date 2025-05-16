    # class Car:
    #     def __init__(self, title, wheels, color):
    #         print("I'm constructor")

    #         self.title = title
    #         self.no_of_wheels = wheels
    #         self.color = color

    #     def __str__(self):
    #         return self.color

    #     def __del__(self):
    #         print("This is Destructor")    

    # i10 = Car("i10", 4, "White")
    # i20 = Car("i10", 4, "red")

    # # print(i10.no_of_wheels)
    # # print(i10.color)

    # print(i10)
    # print(i20)

# Inheritance
    # 1. Single Inheritance

        # class Parent:
        #     car = "Honda City"
        #     bank_balance = 2000000  

        #     def hair_color(self):
        #         print("Dad hair color isLight Brownie") 

        # class Child(Parent):
        #     bike = "Dio"
        #     degree = "Engineering"

        # c1 = Child()

        # print(c1.car)
        # c1.hair_color()

    # 2. Multi_level inheritance

        # class Grant_Parent:
        #     assets = ["Home", "Farm", "GuestHouse"]

        # class Parent(Grant_Parent):
        #     car = "Honda City"
        #     bank_balance = 2000000  

        #     def hair_color(self):
        #         print("Dad hair color isLight Brownie") 

        # class Child(Parent):
        #     bike = "Dio"
        #     degree = "Engineering"

        # c1 = Child()

        # print(c1.assets)
        # c1.hair_color()

# Multiple inheritance

    # class Mother:
    #     assets = ["Home", "Farm", "GuestHouse"]

    # class Father:
    #     car = "Honda City"
    #     bank_balance = 2000000  

    #     def hair_color(self):
    #         print("Dad hair color isLight Brownie") 

    # class Child(Father, Mother):
    #     bike = "Dio"
    #     degree = "Engineering"

    # c1 = Child()

    # print(c1.assets)
    # c1.hair_color()