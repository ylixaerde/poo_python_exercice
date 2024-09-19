class Véhicule:
    def __init__(self, marque, modele, couleur, poids, type, prix, annee_de_fabrication):
        self.marque = marque 
        self.modele = modele
        self.couleur = couleur
        self.poids = poids
        self.type = type
        self.prix = prix
        self.annee_de_fabrication = annee_de_fabrication
        
    def get_info(self):
        return(
            f"Marque : {self.marque}\n"
            f"Modele : {self.modele}\n"
            f"Couleur : {self.couleur}\n"
            f"Poids : {self.poids} kg\n"
            f"Type : {self.type}\n"
            f"Prix : {self.prix} EUR\n"
            f"Année de fabrication : {self.annee_de_fabrication}\n"
        )
    

class Voiture(Véhicule):
    def __init__(self, motorisation, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.motorisation = motorisation

    def get_info(self):
        base_info = super().get_info()
        return(f"Voiture\n"
            f"{base_info}"
            f"Motorisation : {self.motorisation}\n"
            f"Conduite : {self.conduite}\n"
            f"État : {self.etat}\n"
            f"Kilometrage : {self.kilometrage} km\n"
        )

    conduite = "Gauche"
    etat = "Nouvelle"
    kilometrage = "0"


class Moto(Véhicule):
    def __init__(self, motorisation, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.motorisation = motorisation

    def get_info(self):
        base_info = super().get_info()
        return(f"Moto\n"
            f"{base_info}"
            f"Motorisation : {self.motorisation}\n"      
            f"État : {self.etat}\n"
            f"Kilometrage : {self.kilometrage} km\n"

        )

    etat = "Nouvelle"
    kilometrage = "0"


class Vélo(Véhicule):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_info(self):
        base_info = super().get_info()
        return(f"Vélo\n"
            f"{base_info}"
            f"Etat : {self.etat}\n"
            f"Kilométrage : {self.kilometrage} km\n"
        )

    etat = "Nouveau"
    kilometrage = "0"

# motorisation, marque, modele, couleur, poids, type, prix, annee_de_fabrication, 
voiture01 = Voiture("Hybride essence", "Toyota", "Corolla", "Bleu", 1684, "compact", 21000, "2024")
# motorisation, marque, modele, couleur, poids, type, prix, annee_de_fabrication, 
moto02 = Moto("Essence", "Yamaha", "MT-07", "Noir", 98, "Roadster", 12000, "2024")
# marque, modele, couleur, poids, type, prix, annee_de_fabrication
velo03 = Vélo("Giant", "Escape 3", "Rouge", 9, "MTB", 900, "2024")

print(voiture01.get_info())
print()
print(moto02.get_info())
print()
print(velo03.get_info())
