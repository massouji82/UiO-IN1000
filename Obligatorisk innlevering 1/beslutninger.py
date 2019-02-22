'''1.Skriv et program som ber brukeren om å svare “ja” eller “nei” 
på om de kunne tenke seg en brus. Lagre svaret i en variabel.'''

brus = input('Kunne du tenke deg en brus?(ja/nei) ')

'''2.Skriv en if-sjekk som tester hva brukeren har skrevet inn:
a.Hvis brukeren har svart ​“ja”​ skal programmet skrive ut ​“Her har du en brus!”
b.Hvis brukeren har svart ​“nei”​ skal setningen​ “Den er grei.”​ skrives ut.
c.Hvis brukeren har svart noe helt annet skal programmet skrive ut ​“Det forstod jeg ikke helt.”'''

if brus == 'ja':
	print('Her har du en brus!')
elif brus == 'nei':
	print('Den er grei.')
else:
	print('Det forsto jeg ikke helt.')
