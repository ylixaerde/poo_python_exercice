class Utilisateur:
	def __init__(self, nom, active):
		self.user_name = nom
		self.user_active = active
	
	def getNom(self):
		print(f"Nom d'utilisateur : {self.user_name}")
		
class Client(Utilisateur):
	is_client = True
	#attributs et méthodes propre à la classe client