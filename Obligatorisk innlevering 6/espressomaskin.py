# I denne oppgaven skal vi modellere en kapselmaskin for espresso. 
# Maskinen har to innstillinger, espresso (liten kopp) og lungo (større kopp). 
# Maskinen kan ikke startes uten nok vann. En espresso krever 40ml, og en 
# lungo krever 110ml. Maskinens vanntank er på 1000ml -- én liter.

# Gitt "skjelettet" under, fyll ut metodene. Du kommer til å måtte definere 
# dine egne instansvariabler når du skal løse denne oppgaven, og du står også 
# fritt til å definere egne metoder i klassen.

class EspressoMaskin:
    #Konstruktør
    def __init__(self, makskapasitet):
    	self._MAKS = makskapasitet
    	self._vannmengde = 1000
    # Lag espresso dersom det er nok vann
    def lagEspresso(self):
    	if self._vannmengde >= 40: 
    		self._vannmengde -= 40
    		print('Din espresso er servert!:)')
    	else:
    		print('Det er ikke nok vann til en espresso:(')
    # Lag lungo dersom det er nok vann
    def lagLungo(self):
    	if self._vannmengde >= 110:
    		self._vannmengde -= 110
    		print('Din lungo er servert!:)')
    	else:
    		print('Det er ikke nok vann til en lungo:(')
    # Fyll paa et gitt antall milliliter vann, dersom det er plass
    def fyllVann(self, ml):
    	if ml <= self._MAKS - self._vannmengde:
    		self._vannmengde += ml
    		print(f'Fylte på med {ml}ml vann.')
    	else:	
    		print('Det er ikke plass til så mye vann!')
    # Les av maalestrekene på vanntanken og tilgjengelig vann i ml
    def hentVannmengde(self):
    	return self._vannmengde

kaffe = EspressoMaskin(1000)

kaffe.lagLungo()
print(kaffe.hentVannmengde())
kaffe.lagEspresso()
kaffe.lagEspresso()
kaffe.lagEspresso()
print(kaffe.hentVannmengde())
kaffe.fyllVann(50)
print(kaffe.hentVannmengde())
kaffe.fyllVann(500)
print(kaffe.hentVannmengde())


