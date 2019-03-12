# 1. Skriv et program der du lager en tom ordbok personer.

def program():
	personer = {}

# 2. Skriv en while-løkke som tar info fra brukeren så lenge 
# den svarer "y" på spørsmål om å fortsette input. Brukeren skal 
# oppgi to ting hver gang: Et navn og en alder. For hver gang 
# skal navn og alder inn i personer.
	
# 	fortsett = ''
# 	while fortsett != 'n':
# 		navn = input('Oppgi et navn: ')
# 		alder = input('Oppgi en alder: ')
# 		fortsett = input('Vil du fortsette?(y/n): ')
# 		personer.update({navn:alder})

# program()

# 3. Når brukeren ikke lenger taster y skal programmet gå videre 
# og spørre brukeren om å oppgi en bokstav. Bruk en løkke for å 
# fortsette å be om input frem til det blir oppgitt gyldig input 
# (En streng som er nøyaktig ett tegn langt).

# 	fortsett = ''

# 	while fortsett != 'n':
# 		navn = input('Oppgi et navn: ')
# 		alder = input('Oppgi en alder: ')
# 		fortsett = input('Vil du fortsette?(y/n): ')
# 		personer.update({navn:alder})
# 	if fortsett != 'y':
# 		bokstav = input('Oppgi en bokstav: ')
# 		while len(bokstav) != 1:
# 			bokstav = input('Oppgi en bokstav: ')

# program()

# 4. Bruk en for-løkke for å gå gjennom nøklene i ordboken. For 
# hver nøkkel skal du se om den første bokstaven tilsvarer bokstaven 
# brukeren oppgav. Isåfall skal du skrive ut navn og alder på personen.

	fortsett = ''

	while fortsett != 'n':
		navn = input('Oppgi et navn: ')
		alder = input('Oppgi en alder: ')
		fortsett = input('Vil du fortsette?(y/n): ')
		personer.update({navn:alder})
	if fortsett != 'y':
		bokstav = input('Oppgi en bokstav: ')
		while len(bokstav) != 1:
			bokstav = input('Oppgi en bokstav: ')
		bokstav = bokstav.lower()
	for k in personer:
		if k[0].lower() == bokstav:
			print(k, personer[k])


program()

# Hint: Når du sjekker bokstavene mot hverandre kan det lønne seg å 
# bruke funksjonen .lower(), som konverterer strenger til liten bokstav.

# Ekstrautfordring: Kan du sørge for at brukeren blir bedt om å oppgi 
# alder frem til den har oppgitt en gyldig verdi (heltall)?
