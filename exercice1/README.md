Dans cet exercice vous aller créer une classe chargée de représenter un objet que vous connaissez
tous : les Renault Clio.
Vous allez donc déclarer une classe clio dans laquelle nous allons intégrer quelques caractéristiques
d’une vraie clio à savoir : le nombre de portes, la couleur de la carrosserie, et le prix neuf de la
voiture.
L’objectif de cet exercice est de vous faire concevoir des objets plus complexes dont le
comportement est plus proche de ceux observés dans le monde réel. Il n’y aura donc pas que de
simples attributs et méthodes dans votre classe. Vous allez devoir déclarer des attributs de classe
quand cela est nécessaire mais aussi peut-être des méthodes de classes ou encore encapsuler des
attributs.
Ne vous inquiétez pas nous allons y aller étape par étape.
Pour vous aider, voici déjà quelques petites informations que vous devriez savoir :
- Une clio n’a que deux nombres de portes possibles : 3 et 5, c’est une spécificité du modèle, vous
ne verrez jamais de clio avec 7 portes. Cela est donc propre au modèle Clio à quoi correspond la
notion de modèle en POO ?
- Une clio n’a que 5 couleurs de carrosserie possibles (à vous de choisir), une couleur est définie par
un nom « bleu_nuit » par exemple et une référence couleur telle que 213800058. Vous ne pouvez
construire que des Clios avec les couleurs autorisées, là encore cet ensemble clés/valeurs appartient
au modèle. Quand on détermine la couleur de la clio on doit également déterminer un autre attribut :
le numéro de la couleur.
- Le prix neuf de la voiture est commun à toute les clios créées, si le prix neuf d’une voiture change
alors celui de toutes les voitures change aussi.
Votre classe aura à minima les attributs suivants :
• number_doors : le nombre de porte de la voiture, s’assurer que ce soit 3 ou 5
• color_number : le numéro de couleur de la voiture (je vous laisse choisir les chiffres
associés), ce numéro est assigné en même temps que la couleur
• color : le nom de la couleur de la voiture, s’assurer que ce soit une couleur autorisée
Concrètement vous allez stocker les valeurs autorisées dans des attributs de classe, créer des
attributs d’objet mais assigner et récupérer leurs valeurs à l’aide de setters et de getters qui eux
s’occuperont d’effectuer le travail de vérification nécessaire sur la base des attributs de classe.
Le prix neuf des voitures est quand à lui modifiable mais vous devez vous assurer qu’il soit compris
entre 8000 et 30000 euros.

In this exercise you will create a class responsible for representing an object that you know
all: the Renault Clio.
You will therefore declare a clio class in which we will integrate some characteristics
of a real clio to know: the number of doors, the color of the bodywork, and the new price of the
car.
The objective of this exercise is to make you design more complex objects whose
behavior is closer to those seen in the real world. So there will not be only
simple attributes and methods in your class. You will have to declare class attributes
when necessary but also perhaps class methods or even encapsulate
attributes.
Don't worry we will go step by step.
To help you, here is already some small information that you should know:
- A clio has only two possible numbers of doors: 3 and 5, this is a specificity of the model, you
will never see a clio with 7 doors. So this is specific to the Clio model what is the
concept of a model in OOP?
- A clio only has 5 possible body colors (the choice is yours), one color is defined by
a name “bleu_nuit” for example and a color reference such as 213800058. You cannot
build that Clios with the colors allowed, again this set key / values ​​belongs
to the model. When determining the color of the clio, another attribute must also be determined:
the number of the color.
- The new price of the car is common to all the clios created, if the new price of a car changes
so that of all cars changes too.
Your class will have at least the following attributes:
• number_doors: the number of doors in the car, make sure it's 3 or 5
• color_number: the color number of the car (I let you choose the numbers
associated), this number is assigned at the same time as the color
• color: the name of the color of the car, make sure that it is an authorized color
In concrete terms, you will store the allowed values ​​in class attributes, create
object attributes but assign and retrieve their values ​​using setters and getters which
will perform the necessary verification work based on the class attributes.
The new price of cars can be changed, but you must make sure it is understood
between 8,000 and 30,000 euros.
Envoyer des commentaires
