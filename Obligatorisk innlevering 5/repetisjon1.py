# 1.Lag en tom liste ​mineOrd​.

mineOrd = []

# 2.Definer en funksjon som heter ​slaaSammen​. Funksjonen skal 
# ta imot to strenger,konkatenere dem (slå dem sammen) og 
# returnere den sammenslåtte verdien.

def slaaSammen(streng1, streng2):
	sammen = streng1 + streng2
	return sammen

# 3.Definer en prosedyre som heter ​skrivUt​. Prosedyren skal ta 
# imot en liste og skrive ut hvert element i listen på hver sin 
# linje ved hjelp av en for-løkke.

def skrivUt(lst):
	for l in lst:
		print(l)

# 4.Lag en while-løkke som skal kjøres så lenge brukeren ønsker 
# å fortsette. I løkken skal programmet ta i mot en streng fra 
# brukerinput:

# a.Hvis brukeren skriver inn ”i” skal programmet be om to 
# tekststrenger og deretter kalle på funksjonen ​slaaSammen​ med 
# disse som parametere. Resultatet av funksjonskallet skal legges 
# inn i listen ​mineOrd​.

# b.Hvis brukeren skriver inn ”u” skal du kalle prosedyren ​skrivUt​
#  med ​mineOrdsom parameter.

# c.Hvis brukeren skriver inn ”s” skal vi gå ut av løkken og avslutte programmet.

while True:
	bruker = input('Tast inn noe: ')
	bruker = bruker.lower()
	if bruker == 'i':
		streng1 = input('Skriv inn streng 1: ')
		streng2 = input('Skriv inn streng 2: ')
		resultat = slaaSammen(streng1,streng2)
		mineOrd.append(resultat)
	elif bruker == 'u':
		skrivUt(mineOrd)
	elif bruker == 's':
		raise SystemExit







