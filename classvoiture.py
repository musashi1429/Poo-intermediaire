from classclio import Clio

class Voiture(Clio):

    def __init__(self,number_doors, colors, color_number,immatriculation):
        super().__init__(number_doors, colors, color_number)
        self.immatriculation = immatriculation


    @property
    def immatriculation(self):
        return self.__immatriculation

    @immatriculation.setter
    def immatriculation(self,immatriculation):
        self.__immatriculation = immatriculation




voiture_de_fally = Voiture(5,"blue",14255,"BG67590")
print(voiture_de_fally.immatriculation)
print(voiture_de_fally.number_doors)
