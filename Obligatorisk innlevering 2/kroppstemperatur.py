'''Hos friske mennesker varierer kroppstemperaturen 
vanligvis mellom 36.5 og 37.5 grader. 
Lag et program som avgjør om en persons 
kroppstemperatur ligger henholdsvis under, 
innenfor eller over normal kroppstemperatur. 
Programmet skal lese kroppstemperaturen fra terminal.

(Hint: Her må du lese inn desimaltall fra terminalen! 
Vi kan bruke float() for å konvertere String til desimaltall).'''


temp = float(input('Hva er din temperatur? '))
if temp < 36.5: 
	print('Du har lavere kroppstemperatur enn normalen.')
elif temp > 37.5:
	print('Du har høyere kroppstemperatur enn normalen.')
else:
	print('Du har normal kroppstemperatur.')


