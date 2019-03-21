# 1.Skriv en funksjon ​addisjon​ som har to parametre. 
# Funksjonen skal returnere summen av disse. Skriv en 
# kodelinje som kaller på ​addisjon​ med heltallsargumenter 
# du velger selv, og skriv ut resultatet.

def addisjon(num1, num2):
	return num1 + num2

def test_addisjon():
	assert addisjon(5, -5) == 0
	assert addisjon(5, 5) == 10
	assert addisjon(-5, -5) == -10

test_addisjon()

# 2.Skriv tilsvarende funksjoner for ​subtraksjon​, der du 
# trekker det andre parameteret fra det første, og ​divisjon​, 
# der du deler det første parameteret på det andre. Du skal 
# teste disse funksjonene også, men denne gangen ved hjelp 
# av ​assert​. Skriv minst 3 assert​-uttrykk for hver funksjon, 
# der du sjekker at kall på funksjonen med forskjellige heltall 
# du velger selv får verdien du forventer (minst ett kall med 
# to positive tall, ett med to negative tall og ett kall med 
# ett positivt og ett negativt tall).

def subtraksjon(num1, num2):
	return num1 - num2

def test_subtraksjon():
	assert subtraksjon(5, -5) == 10
	assert subtraksjon(5, 5) == 0
	assert subtraksjon(-5, -5) == 0

test_subtraksjon()

def divisjon(num1, num2):
	return num1 / num2

def test_divisjon():
	assert divisjon(5, -5) == -1
	assert divisjon(5, 5) == 1
	assert divisjon(-5, -5) == 1

test_divisjon()

# 3.Lag en funksjon ​tommerTilCm​ med ett parameter ​antallTommer​. 
# Øverst i denne funksjonen skal du bruke ​assert​ for å sjekke at ​
# antallTommer​ er større enn 0. Deretter skal funksjonen returnere 
# hvor mange centimeter ​antallTommer​ tilsvarer. For å regne om 
# fra tommer til centimeter kan du gange ​antallTtommer ​med 2.54.
# Test funksjonen din.

def tommerTilCm(antallTommer):
	assert antallTommer > 0, 'Antall tommer må være større enn 0!'
	return antallTommer * 2.54

# print(tommerTilCm(10))

# 4.Lag en prosedyre ​skrivBeregninger​. Den skal ikke ta imot noen 
# argumenter, men istedet bruke ​input​ for å hente inn verdier fra 
# bruker til kall på funksjonene du skrev over. Ta høyde for at 
# brukeren kan skrive inn flyttall.

# a.Først skal prosedyren hente inn to tall fra bruker. Disse 
# tallene skal brukes som argumenter i kall på ​addisjon​, ​subtraksjon​ 
# og ​divisjon​. Hver av disse funksjonene skal kalles og resultatet 
# skrives ut til terminal.

# def skrivBeregninger():
# 	print('Utregninger:')
# 	tall1 = float(input('Tast inn første tall: '))
# 	tall2 = float(input('Tast inn andre tall: '))
	
# 	add = addisjon(tall1, tall2)
# 	sub = subtraksjon(tall1, tall2)
# 	div = divisjon(tall1, tall2)

# 	print(f'\nResultat av summering: {add}')
# 	print(f'Resultat av subtraksjon: {sub}')
# 	print(f'Resultat av divisjon: {div}')

# skrivBeregninger()

# b.Deretter skal prosedyren hente inn et nytt tall som skal konverteres 
# fra tommer til centimeter. Også dette resultatet skal skrives ut.

def skrivBeregninger():
	print('Utregninger:')
	tall1 = float(input('Tast inn første tall: '))
	tall2 = float(input('Tast inn andre tall: '))
	
	add = addisjon(tall1, tall2)
	sub = subtraksjon(tall1, tall2)
	div = divisjon(tall1, tall2)

	print(f'\nResultat av summering: {add}')
	print(f'Resultat av subtraksjon: {sub}')
	print(f'Resultat av divisjon: {div}')

	print('\nKonvertering fra tommer til cm:')
	tall3 = float(input('Tast inn et nytt tall: '))

	cm = tommerTilCm(tall3)

	print(f'\nResultat: {cm}')

if __name__ == '__main__':	
	print(addisjon(5,5))
	print(subtraksjon(5, 5))
	print(divisjon(5,5))
	skrivBeregninger()	


