# I denne oppgaven skal dere lage to funksjoner som begge 
# utfører operasjoner på strenger.Så skal dere lage et program 
# som bruker disse funksjonene på input fra brukeren, og skriver
# ut informasjon i terminalen.

# 1.Lag en funksjon som, gitt et ord, returnerer antall bokstaver i ordet.

# def bokstaver(ord):
# 	return len(ord)

# print(bokstaver('leke'))

# 2.Lag en funksjon som, gitt en setning, returnerer ei ordbok hvor hvert 
# (unike) ord i setningen er en nøkkelverdi, med antall ganger det ordet 
# finnes i setningen, som innholdsverdi.

def setning(streng):
    streng_dict = {}
    for wd in streng.split():
        if wd in streng_dict:
            streng_dict[wd] += 1
        else:
            streng_dict[wd] = 1
    return streng_dict

# print(setning('Dette er en setning med forskjellige ord i en setning .'))

# 3.Lag et program som tar inn en setning fra brukeren. Bruk så funksjonene 
# fra deloppgave 1 og ​2​. Skriv også til brukeren hvor mange ord det er i 
# setningen, og bruk så resultatene fra de to funksjonene til å skrive hvor 
# mange ganger hvert unike ord forekommer, og hvor mange bokstaver hvert 
# ord består av. Dere kan skrive tegnsetting som “!”, ”.” og ”,”, etc. med 
# mellomrom, og dere kan også behandle disse tegnene som ord.

def setning():

	ord = input('Tast inn en setning:\n')

	antall = print(f'Det er {len(ord.split())} ord i setningen din.')
	
	streng_dict = {}
	for wd in ord.split():
		if wd in streng_dict:
			streng_dict[wd] += 1
		else:
			streng_dict[wd] = 1 
	
	for k,v in streng_dict.items():
		if len(k) == 1 and v == 1:
			print(f'Ordet \'{k}\' forekommer {v} gang, og har {len(k)} bokstav.')
		elif len(k) == 1 and v > 1:
			print(f'Ordet \'{k}\'  forekommer {v} ganger, og har {len(k)} bokstav.')
		elif len (k) > 1 and v == 1:
			print(f'Ordet \'{k}\'  forekommer {v} gang, og har {len(k)} bokstaver.')
		else:
			print(f'Ordet \'{k}\'  forekommer {v} ganger, og har {len(k)} bokstaver.')

setning()













