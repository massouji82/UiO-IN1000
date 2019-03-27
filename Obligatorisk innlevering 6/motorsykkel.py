# Du skal skrive en klasse ​Motorsykkel​ som skal modellere 
# kjøringen av biler. En motorsykkel har et merke, et 
# registreringsnummer og en kilometerstand som viser hvor 
# langt den har kjørt.

# 1.Skriv klassen ​Motorsykkel​ med en konstruktør (init-metode) 
# som initierer de instansvariablene klassen trenger.

class Motorsykkel():

	def __init__(self, merke, regnummer, kmstand):
		self.merke = merke
		self.regnummer = regnummer
		self.kmstand = kmstand

# 2.Skriv en metode ​kjor(self, km)​ som øker kilometerstanden.
	def kjor(self, km):
		self.kmstand += km   

# 3.Skriv en metode ​hentKilometerstand(self)​ som returnerer 
# motorsykkelens totale kilometerstand.

	def hentKilometerstand(self):
		return self.kmstand

# 4.Skriv en metode ​skrivUt(self)​ som skriver ut merke, 
# registreringsnummer og kilometerstand.

	def skrivUt(self):
		print(f'Merke: {self.merke}\nRegistreringsnummer: {self.regnummer}\nKilometerstand: {self.kmstand}')
