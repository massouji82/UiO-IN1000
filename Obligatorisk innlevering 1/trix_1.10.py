'''Skriv et program der du ber om brukerinput på ett eller flere trivia-spørsmål. 
Hvis du ikke kommer på et spørsmål får du et gratis her: 
"Hva heter hovedstaden i Marokko?" (svaret er "Rabat").

Lagre det rette svaret i en tekststreng.

Skriv en if-test for å sjekke om brukeren har svart rett på spørsmålet. 
Hvis de har svart riktig skal programmet skrive ut "Helt rett!". 
Hvis ikke skal programmet skrive ut "Beklager, svaret var" 
og deretter det riktige svaret du har lagret.'''

svar = input('Hva heter hovedstaden i Marokko? ')
rikSvar = 'Rabat'
if svar != rikSvar:
	print(f'Beklager, svaret var {rikSvar}.')
else:
	print('Helt rett!')