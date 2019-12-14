
from product import Product
from person import Person

class Client(Person):
    montant_total = 0
    panier = {}
    def __init__(self,nom,prenom,age,produits):
        super().__init__(nom,prenom,age)
        self.produits = produits


    @classmethod

    def ajout(cls):
        if produits in Product.prod.keys():
            produits.append(panier)



acheteur = Client("fally","kassama",29,"café")

acheteur = Client("fally","kassama",29,"thé")
print(acheteur.age,acheteur.montant_total,acheteur.produits)
acheteur = Client("fally","kassama",29,"café")
print(acheteur.age,acheteur.montant_total,acheteur.produits)
acheteur = Client("fally","kassama",29,"bonbon")
print(acheteur.age,acheteur.montant_total,acheteur.produits)
print(Client.panier)
