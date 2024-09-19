# Classe mère Employee
class Employee:
    def __init__(self, nom, prenom, rue, numero, ville, code_postal, email):
        self.nom = nom
        self.prenom = prenom
        self.rue = rue
        self.numero = numero
        self.ville = ville
        self.code_postal = code_postal
        self.email = email

    def afficher_info(self):
        return f"{self.prenom} {self.nom}, {self.rue} {self.numero}, {self.ville}, {self.code_postal}, {self.email}"

# Sous-classe Commercial
class Commercial(Employee):
    departement = "commercial"
    site = "Charleroi"

    def afficher_info(self):
        base_info = super().afficher_info()
        return f"{base_info}, Département: {self.departement}, Site: {self.site}"

# Sous-classe Comptable
class Comptable(Employee):
    departement = "comptabilite"
    site = "Charleroi"

# Sous-classe Juriste
class Juriste(Employee):
    departement = "juridique"
    site = "Nivelles"

# Instanciation des sous-classes
commercial = Commercial("Dupont", "Jean", "Rue de la Loi", 123, "Charleroi", "6000", "jean.dupont@exemple.com")
comptable = Comptable("Martin", "Sophie", "Avenue des Nations", 45, "Charleroi", "6000", "sophie.martin@exemple.com")
juriste = Juriste("Durand", "Marie", "Boulevard de l'Europe", 78, "Nivelles", "1400", "marie.durand@exemple.com")

# Afficher les informations des employés
print(commercial.afficher_info())
print(comptable.afficher_info())
print(juriste.afficher_info())
