# a) Skriv en prosedyre skriv_med_trykk som tar en tekststreng 
# som parameter. Prosedyren skal skrive ut tekststrengen med et 
# utropstegn på slutten.

def skriv_med_trykk(tekststreng):
	print(tekststreng+'!')

# b) Skriv en løkke som skal kjøres 5 ganger. For hver gang skal 
# brukeren bes om å oppgi et kraftuttrykk. Programmet skal kalle 
# skriv_med_trykk med brukerinput som parameter.

# i = 0
# for i in range(5):
# 	kraft = input('Gi meg et kraftuttrykk: ')
# 	i += 1
# 	skriv_med_trykk(kraft)

# c) Utvid programmet slik at vi er ferdige hvis brukeren 
# skriver "nei" når de blir bedt om input.

gyldig = True
i = 0

while i < 5 and gyldig == True:
		kraft = input('Gi meg et kraftuttrykk: ')
		i += 1
		if kraft.lower() == 'nei':
			gyldig = False
		else:
			skriv_med_trykk(kraft)
		
