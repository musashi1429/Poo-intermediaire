class Product():
    prod = {"thé":1,"café":2,"bonbon":3,"pro" : 8}


    def __init__(self,produits,prix):
        self.produits = produits
        self.prix = prix


    @property
    def produit(self):
        return self.__produits

    @produit.setter
    def achat(self,produits):
        if produits in Product.prod.keys():
            self.__produits = produits
        else:
            ValueError
