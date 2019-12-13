from classclio import Clio

from classclio import Clio

class Bus(Clio):

    def __init__(self,number_doors, colors, color_number,immatriculation,floor):
        Clio.__init__(self,number_doors, colors, color_number)
        self.immatriculation = immatriculation
        self.floor = floor

    @property
    def floor(self):
        return self.__floor

    @floor.setter
    def floor(self,floor):
        self.__floor = floor


    @property
    def immatriculation(self):
        return self.__immatriculation

    @immatriculation.setter
    def immatriculation(self,immatriculation):
        self.__immatriculation = immatriculation



bus_de_fally = Bus(3,"black",14255,"TY97590",2)
print(bus_de_fally.immatriculation)
print(bus_de_fally.number_doors)
print(bus_de_fally.colors)
print(bus_de_fally.color_number)
print(bus_de_fally.floor)
