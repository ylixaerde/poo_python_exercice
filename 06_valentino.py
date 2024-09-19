class Employee:
    def __init__(self,nom,prenom,rue,numero,ville,code_postal,adresse_mail):
        self.nom = nom
        self.prenom = prenom
        self.rue = rue
        self.numero = numero
        self.ville = ville
        self.code_postal = code_postal
        self.adresse_mail = adresse_mail

    def getNom(self):
        print(f"Nom d'utilisateur : {self.name}")

class Commercial(Employee):
    departement = "commercial"
    site = "Charleroi" 

class Comptable(Commercial):
    departement = "comptabilite"
    site = "Charleroi"

class Juriste(Comptable):
    departement = "juridique"
    site = "Nivelles"

commercial01 = Commercial("Leclerc","Charles","Rue du Casino","107","monaco","98000","Charles@gmail.com",True)
comptable01 = Comptable("Verstappen","Max","Rue du Casino","108","monaco","98000","Max@gmail.com",True)
juriste01 = Juriste("Hamilton","Lewis","Rue du Casino","109","monaco","98000","Lewis@gmail.com",True)
