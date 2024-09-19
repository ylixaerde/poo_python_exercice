class Utilisateur:
	def __init__(self, nom, active):
		self.user_name = nom
		self.user_active = active
	
	def getNom(self):
		print(f"Nom d'utilisateur : {self.user_name}")

	id = 1
	grp_db = ["admin", "invité"]

user01 = Utilisateur("John", True)
user02 = Utilisateur("Frank", True)

user02.id = 2

print(f"ID de user01 : {user01.id}")
print(f"ID de user02 : {user02.id}")

user01.grp_db[0] = "root"

print(f"grp_db de user02 : {user02.grp_db}")