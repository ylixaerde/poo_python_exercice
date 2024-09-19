class Vehicule:
    def __init__(self,marque,modele,type_vehicule,couleur,plaque_immatriculation):
        self.marque = marque
        self.modele = modele
        self.type_vehicule = type_vehicule
        self.couleur = couleur
        self.plaque_immatriculation = plaque_immatriculation
    
    def get_infos(self):
        return(f"Marque : {self.marque}\n"
               f"Modele : {self.modele}\n"
               f"Type de véhicule  : {self.type_vehicule}\n"
               f"couleur : {self.marque}\n"
               f"Marque : {self.marque}\n")

class Voiture(Vehicule):
    couleur_jante = "noir"
    type_moteur = "V12"
    type_chassis = "Carbone"

    def get_infos(self):
        base_info = super().get_infos()
        return(f"{base_info}\n"
               f"Couleur des jantes : {self.couleur_jante}\n"
               f"Type de moteur: {self.type_moteur}"
               f"Type de chassis: {self.type_chassis}")
    
class Moto(Vehicule):
    couleur_jante = "noir"
    type_moteur = "V12"
    type_chassis = "Carbone"

    def get_infos(self):
        base_info = super().get_infos()
        return(f"{base_info}\n"
               f"Couleur des jantes : {self.couleur_jante}\n"
               f"Type de moteur: {self.type_moteur}\n"
               f"Type de chassis: {self.type_chassis}\n")
    
class Velo(Vehicule):

    def get_infos(self):
        base_info = super().get_infos()
        return(f"{base_info}\n")
    
voiture01 = Voiture("Ferrari", "812 Competizione", "SuperSportive", "Rouge", "IT - 131023")
moto01 = Moto("Yamaha", "YZF-R1" , "Sportive", "Violet", "IT - 131023")
velo01 = Velo("Pinarello", "Dogma F12", "Course", "Gris", "IT - 131023")

print(voiture01.get_infos())
print()
print(moto01.get_infos())
print()
print(velo01.get_infos())
print()