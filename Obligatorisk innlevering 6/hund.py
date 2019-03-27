# 1.Skriv en klasse ​Hund​ med en konstruktør som tar imot verdier, 
# og setter instansvariabler for ​alder​ og ​vekt​. ​Hund​ skal i tillegg 
# ha en instansvariabel ​metthet som får verdien 10.

class Hund():
	def __init__(self, alder, vekt, metthet=10):
		self._alder = alder
		self._vekt = vekt
		self._metthet = metthet

# 2.Skriv metoder som lar brukere hente ut ​alder​ og ​vekt​.

	def alder(self):
		print(f'Alder: {self._alder}')

	def vekt(self):
		print(f'Vekt: {self._vekt}')

# 3.Skriv en metode ​spring​. Den tar ingen argumenter. Metoden skal 
# minske ​metthet med 1. Utvid metoden med en sjekk som minsker ​vekt​ 
# med 1 dersom ​metthet ​er mindre enn 5.

	def spring(self):
		self._metthet -= 1
		if self._metthet < 5:
			self._vekt -= 1

# 4.Skriv en metode ​spis​. Den tar et heltall og legger det til ​metthet​. 
# Skriv deretter en sjekk som setter opp ​vekt​ med 1 dersom metthet er 
# større enn 7.

	def spis(self, tall):
		self._metthet += tall
		if self._metthet > 7:
			self._vekt += 1