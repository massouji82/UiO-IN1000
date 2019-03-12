# 1. Skriv oppgavetekst til en oppgave som handler om løkker og lister. 
# Et forslag er å programmere et system som lar bruker holde styr på, 
# legge til og skrive ut venners bursdager.

# 2.Løs oppgaven! Du skal levere både oppgaveteksten og besvarelsen (skriv 
# oppgaveteksten som kommentarer over løsningen din).

bursdager = {}

print('\n***Velkommen til busdagsoversikten!***\n')
name = input('Tast inn navn på bursdagsbarnet: ')
date = input('Tast inn personens fødselsnummer: ')
bursdager[name] = date	

while True:
	flere = input('Vil du legge til flere bursdager? (ja/nei): ').lower()
	if flere == 'ja':
		name = input('Tast inn navn: ')
		date = input('Tast inn fødselsnummer: ')
		bursdager[name] = date	
	elif flere == 'nei':
		dato = input('Vil du se liste over bursdager? (ja/nei): ').lower()	
		if dato == 'ja':
			for k, v in bursdager.items():
				print(f'{k} har bursdag {v}.')
		elif dato == 'nei':
			print('\nFarvel!\n')
			break	
		else:
			print('Vennligst svar ja/nei.')
	else:
		print('Vennligst svar ja/nei.')

# for k, v in bursdager.items():
# 	print(f'{k} har bursdag {v}.')
