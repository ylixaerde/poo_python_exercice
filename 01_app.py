class Utilisateur:
	active = False
	
	def setNom(self, n):
		self.nom = n

user01 = Utilisateur()
user02 = Utilisateur()

user01.active = True
print(f'user01.active : {user01.active}')
print(f'user02.active : {user02.active}')

user01.setNom("John")
user02.setNom("Frank")
print(f'user01.nom : {user01.nom}')
print(f'user02.nom : {user02.nom}')
