# Classe mère Vehicule
class Vehicule:
    def __init__(self, modele, couleur, vitesse, nb_place, prix):
        self.modele = modele
        self.couleur = couleur
        self.vitesse = vitesse
        self.nb_place = nb_place
        self.prix = prix
        
    def afficher_info(self):
        return f"{self.modele} {self.couleur}, {self.vitesse} km/h, {self.nb_place} places, {self.prix} €"

# Classe Voiture
class Voiture(Vehicule):
    def __init__(self, modele, couleur, vitesse, nb_place, prix, type_voiture):
        super().__init__(modele, couleur, vitesse, nb_place, prix)
        self.type_voiture = type_voiture

    def afficher_info(self):
        base_info = super().afficher_info()
        return f"{base_info}, Type: {self.type_voiture}"

# Classe Velo
class Velo(Vehicule):
    def __init__(self, modele, couleur, vitesse, nb_place, prix, type_velo):
        super().__init__(modele, couleur, vitesse, nb_place, prix)
        self.type_velo = type_velo

    def afficher_info(self):
        base_info = super().afficher_info()
        return f"{base_info}, Type: {self.type_velo}"

# Classe Moto
class Moto(Vehicule):
    def __init__(self, modele, couleur, vitesse, nb_place, prix, type_moto):
        super().__init__(modele, couleur, vitesse, nb_place, prix)
        self.type_moto = type_moto

    def afficher_info(self):
        base_info = super().afficher_info()
        return f"{base_info}, Type: {self.type_moto}"

# Création d'objets
voiture1 = Voiture("Tesla Model 3", "Noir", 250, 5, 50000, "Sportif")
velo1 = Velo("VTT Rockrider", "Rouge", 30, 1, 500, "Tout-terrain")
moto1 = Moto("Yamaha YZF-R1", "Bleu", 300, 2, 15000, "Sportive")

# Affichage des informations des véhicules
print(voiture1.afficher_info())
print(velo1.afficher_info())
print(moto1.afficher_info())
