# #1.Lag en ordbok (dictionary) som skal inneholde varer i 
# en butikk og pris. Du skal brukevarenavn som nøkkelverdier 
# og varepriser (i form av flyttall) som innholdsverdier.
# Opprett ordboka med følgende varer med tilhørende pris: 
# melk - kr 14.90, brød - kr 24.90, yoghurt - 12.90 og pizza - 39.90. 
# Skriv ut innholdet i ordboken med en enkelprint-setning.

varer = {
		'melk':'kr 14.90',
		'brød':'kr 24.90',
		'yoghurt':'kr 12.90',
		'pizza':'kr 39.90'
		}

print(varer)

# 2.Les inn to varenavn og priser fra brukeren og legg disse 
# til i ordboken. Skriv utordboken på nytt.

vare = input('Tast inn en vare: ')
pris = input('Tast inn prisen på varen: ')
vare2 = input('Tast inn en vare til: ')
pris2 = input('Tast inn prisen på denne: ')

bruker = {vare:pris,vare2:pris2}

varer.update(bruker)

print(varer)



