class Employee:
    def __init__(self, nom, prenom, rue, numero, ville, code_postal, adresse_mail):
        self.nom = nom 
        self.prenom = prenom
        self.rue = rue
        self.numero = numero
        self.ville = ville
        self.code_postal = code_postal
        self.adresse_mail = adresse_mail

class Commercial(Employee):
    departement = "commercial"
    site = "Charleroi"

class Comptable(Employee):
    departement = "comptabilite"
    site = "Charleroi"

class Juriste(Employee):
    departement = "comptabilite"
    site = "Nivelles"

user01 = Commercial("Dupont", "Jean", "Rue des Lilas", "12", "Charleroi", "6000", "jean.dupont@example.com")
user02 = Comptable("Martin", "Claire", "Avenue des Fleurs", "25", "Charleroi", "6000", "claire.martin@example.com")
user03 = Juriste("Bernard", "Julien", "Boulevard des Champs", "78", "Nivelles", "1400", "julien.bernard@example.com")