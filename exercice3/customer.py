
from product import Product
from person import Person

class Client(Person):
    nbr_achat = 0
    def __init__(self,nom,prenom,age,produits):
        super().__init__(nom,prenom,age)
        self.produits = produits
        self.montant_total = 0
        self.panier = {}
        Client.nbr_achat += 1


    def ajout(self,produits):
        for produits in Product.prod.keys():
            return produits
            panier += produits
            print(produits)

    def panier(self,panier):
        self.panier = panier
        panier += produits


acheteur = Client("fally","kassama",29,"café")
acheteur.ajout("café")
print(acheteur.produits)
print(acheteur.panier   )
acheteur = Client("fally","kassama",29,"thé")
print(acheteur.age,acheteur.montant_total,acheteur.produits)
print(acheteur.panier)
acheteur = Client("fally","kassama",29,"café")
print(acheteur.age,acheteur.montant_total,acheteur.produits)
print(acheteur.panier)
acheteur = Client("fally","kassama",29,"bonbon")
print(acheteur.age,acheteur.montant_total,acheteur.produits)
print(Client.nbr_achat)
