class Employee:
    def __init__(self,nom,prenom,rue,numero,ville,code_postal,adresse_mail):
        self.nom = nom
        self.prenom = prenom
        self.rue = rue
        self.numero = numero
        self.ville = ville
        self.code_postal = code_postal
        self.adresse_mail = adresse_mail

    def get_infos(self):
        return(
            f"Nom : {self.nom}\n"
            f"Prénom : {self.prenom}\n"
            f"Rue : {self.rue}\n"
            f"Numéro : {self.numero}\n"
            f"Ville : {self.ville}\n"
            f"Code Postal : {self.code_postal}\n"
            f"Adresse Mail : {self.adresse_mail}"
        )


class Commercial(Employee):
    def get_infos(self):
        base_info = super().get_infos()
        return(f"{self.departement.capitalize()} : \n"
            f"{base_info}\n"
            f"Département: {self.departement}\n"
            f"Site: {self.site}")
    
    departement = "commercial"
    site = "Charleroi"


class Comptable(Employee):
    def get_infos(self):
        base_info = super().get_infos()
        return(f"{self.departement.capitalize()} : \n"
            f"{base_info}\n"
            f"Département: {self.departement}\n"
            f"Site: {self.site}")
    
    departement = "comptabilite"
    site = "Charleroi"


class Juriste(Employee):
    def get_infos(self):
        base_info = super().get_infos()
        return(f"{self.departement.capitalize()} : \n"
            f"{base_info}\n"
            f"Département: {self.departement}\n"
            f"Site: {self.site}")
    
    departement = "juridique"
    site = "Nivelles"


commercial01 = Commercial("Leclerc","Charles","Rue du Casino","107","monaco","98000","charles@gmail.com")
comptable01 = Comptable("Verstappen","Max","Rue du Casino","108","monaco","98000","max@gmail.com")
juriste01 = Juriste("Hamilton","Lewis","Rue du Casino","109","monaco","98000","lewis@gmail.com")

print(commercial01.get_infos())
print()
print(comptable01.get_infos())
print()
print(juriste01.get_infos())