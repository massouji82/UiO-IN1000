# Denne oppgaven har tre deloppgaver som er uavhengige av hverandre. I hver av deloppgavene skal du skrive en funksjon.

# Deloppgave 1
# Skriv en funksjon som returnerer antall sifre i et tall. For eksempel er det 3 sifre i tallet 104.

def sifre(tall):
	antall = 0
	for n in str(tall):
		antall += 1	
	return antall

print(sifre(1322323))

# Deloppgave 2
# Skriv en funksjon som gir hvor mange av en viss bokstav det er i et ord. For eksempel er det 2 forekomster av bokstaven "e" i ordet kakespade.

def mange(ord, bokstav):
	antall = 0
	for tegn in ord:
		if tegn == bokstav:
			antall += 1
	return antall
 
print(mange('lese', 'e'))

# # Deloppgave 3
# # Skriv en funksjon som tar enn en streng og et tall, og som returnerer True eller False basert på om strengens lengde er høyere enn tall.

def lengde(streng, tall):
	antall = 0
	høyde = 0
	for n in streng:
		antall += 1
	for x in str(tall):
		høyde += 1
	if antall > høyde:
		return True
	return False

print(lengde('lese', 2))