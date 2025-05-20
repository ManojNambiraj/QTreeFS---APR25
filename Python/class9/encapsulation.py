# Access specifier
    # 1. Public
    # 2. Private

# Encapsulation  ---> (Getter & Setter)

class Car:
    def __init__(self, wheels, color, sheets):
        self.__no_of_wheels = wheels
        self.car_color = color
        self.no_of_sheets = sheets

    def setNo_of_wheels(self, values):
        self.__no_of_wheels = values

    def getNo_of_wheels(self):
        return self.__no_of_wheels

c1 = Car(0, "white", 7)

c1.setNo_of_wheels(6)

print(c1.getNo_of_wheels())