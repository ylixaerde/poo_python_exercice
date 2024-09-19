class Utilisateur:
	def __init__(self, nom, active):
		self.user_name = nom
		self.user_active = active
	
	def getInfo(self):
		print(f"Nom d'utilisateur : {self.user_name}")

class Client(Utilisateur):
	def __init__(self, nom, active, mail):
		self.user_name = nom
		self.user_active = active
		self.user_mail = mail

	def getInfo(self):
		print(f"Client {self.user_name}, adresse mail {self.user_mail}")
		
user01 = Utilisateur("John", True)
user02 = Client("Frank", True, "frank@gmail.com")

user01.getInfo()
user02.getInfo()
