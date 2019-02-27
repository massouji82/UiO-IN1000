'''1.Lag en liste fylt med 3 tall du velger selv. 
Legg deretter til et nytt tall på slutten av lista.
Skriv ut det første og tredje elementet i lista.'''

liste = ['banan', 'viskelær', 'hund']

liste.append('elg')

print(liste[::2])

# 2.Lag en ny, tom liste. Be deretter brukeren om å oppgi 
# 4 navn, og legg disse inn ilista.

liste2 = []

en = input('Oppgi fire navn. Første navn: ')
to = input('Andre navn: ')
tre = input('Tredje navn: ')
fire = input('Fjerde navn: ')

liste2.extend([en,to,tre,fire])

# 3.Bruk en if-sjekk for å se om brukeren har lagt inn 
# navnet ditt i lista. Hvis brukeren har gjort det skal du 
# skrive ut “Du husket meg!”. Hvis navnet ditt ikke finnes 
# i lista skal duskrive ut “Glemte du meg?”. 

if 'mass'.lower() in liste2:
	print('Du husket meg!')
else:
	print('Du glemte meg?')

# 4.Lag en ny liste ved å slå sammen de to listene du har 
# laget til nå, og skriv ut den nyelisten. Fjern deretter de 
# to siste elementene fra lista, og skriv så ut listen på nytt.

liste3 = liste + liste2

print(liste3)

del liste3[-2:]

print(liste3)





