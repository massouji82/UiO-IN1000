# a) Lag et program med en funksjon forekommer. Funksjonen 
# skal sjekke forekomster av tegn i en tekst og returnere True 
# hvis tegnet forekommer i tekststrengen. Hvis tegnet ikke 
# forekommer i tekststrengen skal funksjonen returnere False. 
# Funksjonen skal ta inn to parametere: et tegn og en tekststreng.

def forekommer(tekststreng, tegn):
	if tegn in tekststreng:
		return True
	return False

print(forekommer('inf1001', 'i'))

# b) Lag deretter en metode som skal hete uten_repetisjon som tar 
# imot en tekststreng, fjerner alle repetisjoner av tegn i tekststrengen 
# og returnerer resultatet.

def uten_repetisjon(tekststreng):
	tekst = ''
	for i in tekststreng:
		if i not in tekst:
			tekst += i
	return tekst

print(uten_repetisjon('aababbabbac'))

# c) Lag en funksjon som heter antall_forskjellige og som returnerer antall 
# forskjellige tegn som forekommer i en tekststreng.

def antall_forskjellige(tekststreng):
	return len(uten_repetisjon(tekststreng))

print(antall_forskjellige('aababbabbac'))
