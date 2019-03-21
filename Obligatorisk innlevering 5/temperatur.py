# For å løse denne oppgaven skal du lese inn data fra en fil. 
# Oppgaven kan løses i både Linux og Windows, men vær klar over 
# at det er noen forskjeller i hvordan filstier brukes. Legg 
# for sikkerhets skyld ​temperatur.txt​ i samme mappe som ​temperatur.py.

# 1.Vi har en fil ​temperatur.txt​ som inneholder 12 linjer hvor 
# hver linje ergjennomsnittstemperaturen for en måned i et år. 
# Første linje tilsvarer januar, andrelinje tilsvarer februar, osv. 
# Vi har rundet av temperaturene til heltall. Les inntemperaturene 
# en etter en og putt verdiene inn i en liste.

x = []

with open('temperatur.txt') as t:
	for line in t:
		x.extend(line.split())

print(x)

# 2.Skriv en funksjon som tar i mot en liste og returnerer gjennomsnittet
# av verdiene i listen ved hjelp av en for-løkke. Kall denne funksjonen 
# med listen av temperaturersom argument, og skriv ut resultatet.

def average(lst):
	total = 0
	for i in range(0, len(x)):
		total += int(x[i])
	av = total/len(x) 
	print(f'Gjennomsnittet av temperaturene er: \n {av}')

average(x)

