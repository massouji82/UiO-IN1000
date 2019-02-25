'''1.Skriv oppgavetekst til en oppgave som har 
med beslutninger å gjøre (if/else). Et forslag er å 
skrive et quiz-program som stiller spørsmål til bruker 
og gir tilbakemelding på om svarene er korrekte.

2.Løs oppgaven! Du skal levere både oppgaveteksten og 
besvarelsen (skrivoppgaveteksten som kommentarer over 
løsningen din).'''

print('***Velkommen til QUIZ!***')
cap = input('Hva er hovedstaden i Mongolia? ')
if cap.lower() == 'ulaanbaatar':
	print('Korrekt!')
else:
	print('Sorry! Feil Svar.')
box = input('Hvor gammel var Mike Tyson når han ble verdensmester i tungvektsklassen i boksing? ')
if box == '20':
	print('Korrekt!')
else:
	print('Sorry! Feil Svar.')
laura = input('Hvem drepte Laura Palmer? ')
if laura.lower() == 'bob':
	print('Korrekt!')
else:
	print('Sorry! Feil Svar.')



