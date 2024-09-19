class Utilisateur:
	def __init__(self, name, active):
		self.name = name
		self.active = active
	
	def getNom(self):
		print(f"Nom de l'utilisateur : {self.name}")

user01 = Utilisateur("John", True)
user02 = Utilisateur("Frank", True)

user01.getNom()