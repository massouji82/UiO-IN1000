# a) Skriv en klasse med navn 'Bil':

# b) Bilen skal ha to variabler, en for eier og en for merke:	

# c) Sett verdiene i en konstruktør (init-metode).

# d) Skriv en metode for å skrive ut verdien til eieren og merket.

# e) Test klassen din ved å opprette to Bil-objekter med forskjellige eiere.

class Bil:
	def __init__(self, eier, merke):
		self.eier = eier
		self.merke = merke

	def skriv(self):
		print(f'Eier: {self.eier}, Merke: {self.merke}')

bil1 = Bil('Fritjof', 'Skoda')
bil2 = Bil('Randi', 'Ford')

bil1.skriv()	
bil2.skriv()	