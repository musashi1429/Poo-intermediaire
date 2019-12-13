class Clio():
    price_range = [8000, 30000]
    price = 20000
    doors = (3, 5)
    colors = {
        "black" : 1234258,
        "blue" : 14255,
        "green" : 143582,
        "red" : 134625852,
        "white" : 125452
        }
    def __init__(self, number_doors, colors, color_number):

        self.number_doors = number_doors
        self.colors = colors
        self.color_number = color_number

    @property

    def number_doors(self):
        return self.__number_doors

    @number_doors.setter

    def number_doors(self, number_doors) :
        if number_doors in Clio.doors :
            self.__number_doors = number_doors
        else :
            raise ValueError

    @property

    def color_number(self):
        return self.__color_number

    @color_number.setter

    def color_number(self, color_number) :
        if color_number in Clio.colors.values() :
            self.__color_number = color_number
        else :
            raise ValueError

    @property
    def color(self):
        return self.__colors

    @color.setter

    def color(self, color) :
        if color in Clio.colors.key() :
            self.__colors = colors
        else :
            raise ValueError

    @classmethod

    def checkprice(cls):
        if cls.price in range(8000,30000):
            return cls.price
        else :
            raise ValueError
