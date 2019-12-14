class Employee(Person):
    statuts = ("employé", "technicien", "manager","cadre")
    def__init__(self,nom,prenom,age,statuts):
        super().__init__(nom,prenom,age)
        self.statuts = {}
        
