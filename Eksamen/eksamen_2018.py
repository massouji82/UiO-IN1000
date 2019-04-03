# #1a)
# 3

# #1b)
# ad

# #1c)
# 17

# #1d)
# 9

# #1e)
# 16

# #1f)
# 32

# #2a)
# 49

# #2b)
# 60

# #2c)
# 49

# #2d)
# 49

# 3a)
# def vinnerlag(hjemmelag, bortelag, hjemmemaal, bortemaal):
# 	if hjemmemaal > bortemaal:
# 		return hjemmelag
# 	elif hjemmemaal < bortemaal:
# 		return bortelag
# 	else:
# 		return 'Uavgjort'

# # print(vinnerlag('Brasil', 'Norge', 5, 1))

# #3b)
# def forkort_lagliste(lagliste):
# 	lagnavn = []
# 	for n in lagliste:
# 		if n not in lagnavn:
# 			lagnavn.append(n)
# 	return lagnavn

# # print(forkort_lagliste(['Brasil', 'Norge', 'Brasil', 'Iran']))

# #3c)
# def legg_inn_null_maal(lagliste):
# 	scoring = {}
# 	for n in lagliste:
# 		scoring[n] = 0
# 	return scoring

# # print(legg_inn_null_maal(['Brasil', 'Norge', 'Iran']))

# # 3d)
# fn = open('resultat.txt','r')

# def ekstraher_lagliste(fn):
# 	ny_liste = []
# 	for line in fn:
# 		lag = line.split()
# 		hjemmelag = lag[0]
# 		bortelag = lag[1]
# 		ny_liste.append(hjemmelag)
# 		ny_liste.append(bortelag)
		
# 	return ny_liste

# # print(ekstraher_lagliste(fn))

# fn.close()

# #3e)
# fn = open('resultat.txt','r')

# def regn_poengsum(fn):
# 	lag = forkort_lagliste(ekstraher_lagliste(fn))
# 	oversikt = legg_inn_null_maal(lag)
	
# 	for line in fn:
# 		biter = line.split()
# 		hjemmelag = biter[0]
# 		bortelag = biter[1]
# 		hjemmemaal = int(biter[2])
# 		bortemaal = int(biter[3])
# 		vinner = vinnerlag(hjemmelag, bortelag, hjemmemaal, bortemaal)
# 		if vinner == hjemmelag:
# 			oversikt[hjemmelag] = 3
# 		elif vinner == bortelag:
# 			oversikt[bortelag] = 3
# 		else:
# 			oversikt[hjemmelag] = 1
# 			oversikt[bortelag] = 1
# 	return oversikt

# print(regn_poengsum(fn))

#3f)

#3g)

#4a)

class Rett():
	def __init__(self, navn, pris, innhold):
		self._navn = navn
		self._pris = pris
		self._innhold = innhold

	def sjekkInnholdOK(self, unngaa):
		for n in self._innhold:
			if n in unngaa:
				return False
			return True

	def __str__(self):
		m = 'Rett: {}, Pris: {}, Ingredienser: '.format(self._navn, self._pris,)
		for i in self._innhold:
			m += ', ' +i
		return m

# b)

class Kategori():
	def __init__(self, katNavn, retter):
		self._katNnavn = katNavn
		self._retter = retter

	def hentOKRetter(self, unngaa):
		kurant = []
		for n in self._retter:
			if n.sjekkInnholdOK(unngaa):
				kurant.append(n)
		return kurant

	def skrivKat(self):
		print(f'Kategori: {katNavn}')
		for r in self._retter:
			print(r)

#c)

class Meny():
	def __init__(self, katNavnListe):
		self._meny = {}
		for n in katNavnListe:
			self._meny[knavn] = self._lesKategoriFil(knavn + '.txt')

	def hentRedusertMeny(self, unngaa):
		for n in self._meny:
			retter = self._meny[n].hentOKRetter(unngaa) 
			if retter:
				redusert = Kategori(katNavn, retter)
				okKategorier[katNavn] = redusert
		return okKategorier

#d)

class Kunde():
	def __init__(self, nrKunde, unngaa):
		self._nrKunde = nrKunde
		self._unngaa = unngaa

	def velgRetter(self, meny):
		kategorier = meny.hentRedusertMeny(self._unngaa)
		liste = []
		for n in kategorier.values():
			n.skrivKat()
			valg = input('Velg en rett fra kategorien eller trykk Enter for å velge blant neste kategori: ')
				if valg != '':
				liste.append(valg)
		return valg 

# e)

class TakeAway():
	def __init__(self, kategorier, kundefil):
		self._meny = Meny(kategorier)
		self._kundekatalog = self._lesKundefil(kundefil)

	def betjentKunde(self, tlfKontakt):
		kunde = self._kundekatalog[tlfKontakt]
		bestilling = kunde.velgRetter(self._meny)
		self._lagOgLeverMat(bestilling)

	def _lagOgLeverMat(self, bestilling):
		print('Din bestilling: ')
		for b in bestilling:
			print(b)

#f)

def hovedprogram():
	mineKategorier = ['Forretter', 'Hovedretter', 'Desserter']
	minTakeAway = TakeAway(mineKategorier, 'Kunder.txt')

	bestill = input('Tast inn ditt telefonnummer: ')
	while bestill != '':
		minTakeAway.betjentKunde(bestill)
		bestill = input('Tast inn ditt telefonnummer: ')

hovedprogram()

































