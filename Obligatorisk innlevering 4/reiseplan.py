# I denne oppgaven skal du lage et program som lar en 
# bruker legge planer for en reise. Dette skal du gjøre 
# ved hjelp av en ​nøstet​ liste, det vil si en liste av lister.

# 1.Lag en tom liste ​steder​, og gi brukeren mulighet til å fylle 
# den med 5 reisemål vedhjelp av en for-løkke.

steder = []

print('Oppgi 5 reisemål.')
for n in range(5):
	sted = input('Reisemål: ')
	steder.append(sted)
	n += 1

# 2.Lag to lister til ved navn ​klesplagg​ og ​avreise datoer​, og la 
# brukeren fylle inn disse på samme måte, med fem elementer i hver 
# liste.

klesplagg = []
avreisedatoer = []

print('Oppgi 5 klesplagg.')
for n in range(5):
	klesp = input('Klesplagg: ')
	klesplagg.append(klesp)
	n += 1

print('Oppgi 5 avreisedatoer.')
for n in range(5):
	avreise = input('Avreisedatoer: ')
	avreisedatoer.append(avreise)
	n += 1

# 3.Nå skal du lage en liste som kan inneholde de andre listene du 
# har skrevet. Oppretten liste ​reiseplan​, og legg til ​steder​, ​klesplagg ​
# og ​avreisedatoer​ i lista.

reiseplan = [] 

reiseplan.append(steder)
reiseplan.append(klesplagg)
reiseplan.append(avreisedatoer)

# 4.Bruk en enkel for-løkke for å skrive ut innholdet i ​reiseplan​, 
# og se at det skrives ut tre lister med hvert sitt innhold.

for n in reiseplan:
	print(n)

# 5.Følg disse stegene for å la brukeren oppgi en plass i ​reiseplan​ og 
# skrive ut elementet på den oppgitte plassen.

# a.Først henter du inn en indeks ​i1​ som representerer en av de tre listene 
# i reiseplan​, der gyldig input vil være mellom 0 og lengden til ​reiseplan ​
# minus 1 (som vi har gått gjennom starter indeksen på 0, og en liste med 5 
# elementer vil derfor ha 4 som høyeste indeks).

# b.Deretter en indeks ​i2​ som representerer et av de fem elementene i den 
# valgte listen, der gyldig input vil være mellom 0 og lengden til listen minus 1.

# c.Bruk en if-sjekk til å teste at de to tallene brukeren har oppgitt er 
# gyldige verdier. Dersom tallene er mulige plasser i listene skal de brukes 
# til å skrive utreiseplan ​[i1][i2]​.​ Hvis tallene ikke er gyldige plasseringer 
# skal du skrive ut “Ugyldig input!”

kat = input('Oppgi kategori:\n1.Sted\n2.Klesplagg\n3.Avreisedato\n')
nr = input('Oppgi element i valgte kategori(1 til 5): ')
kat = int(kat)
nr = int(nr)
if kat > 3 or kat < 1:
	print('Ugyldig input!')
elif nr > 5 or nr < 1:
	print('Ugyldig input!')
else:
	print(reiseplan[kat-1][nr-1])

