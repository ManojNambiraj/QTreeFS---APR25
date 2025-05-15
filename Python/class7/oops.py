# OOPs --> Object Oriented Programmings

"""
    1. Class
    2. Objects
    3. Inheritance
    4. Encapsulation
    5. Polymorphism
    6. Abstraction
"""

# Class Example 1:

    # class Car:
    #     no_of_wheels = 4
    #     color = "white"
    #     no_of_sheets = 7
    #     fuel_type = "petrol"

    # elevate = Car()

    # print(elevate.no_of_wheels)
    # print(elevate.color)

    # print("----------------------")

    # verna = Car()

    # print(verna.no_of_sheets)

# Class Example 2:

# class Car:
#     no_of_wheels = 0
#     color = ""
#     no_of_sheets = 0
#     fuel_type = ""

#     def demo(self):
#         print(self.color)

# i10 = Car()

# i10.no_of_wheels = 4
# i10.color = "red"

# # print(i10.no_of_wheels)
# # print(i10.color)

# i10.demo()

# print("----------------------")

# inova = Car()

# inova.no_of_wheels = 5
# inova.color = "white"

# # print(inova.no_of_wheels, inova.color)

# # inova.demo()

# Example 3:

class Car:
    def __init__(self, name, wheels, color, sheets, fuel):
        print("I'm Constructor")

        self.title = name
        self.no_of_wheels = wheels
        self.color = color
        self.no_of_sheets = sheets
        self.fuel_type = fuel

    def demo(self):
        print(self.title)

i10 = Car("i10", 4, "red", 5, "diesel")

inova = Car("inova", 5, "white", 7, "petrol")

xoo = Car("xoo", 6, "Crimson", 9, "Gas")

i10.demo()
print(i10.no_of_wheels)
print(i10.no_of_sheets)
print(i10.color)
print(i10.fuel_type)


print("-------------------")



inova.demo()
print(inova.no_of_wheels)
print(inova.no_of_sheets)
print(inova.color)
print(inova.fuel_type)