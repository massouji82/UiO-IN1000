'''Lag et program som kommuniserer med brukeren slik
 at det tar inn et navn og et bosted fra terminalen. 
 Eksempel på hvordan en kjøring av programmet skal se ut:
 > python3 utskriftsfunksjon.py
 Skriv inn navn: Espen Askeladd
 Hvor kommer du fra? OsloHei, Espen Askeladd! 
 Du er fra Oslo.'''

navn = input('Skriv inn et navn: ')
sted = input('Hvor kommer du fra? ')
print(f'Hei {navn}! Du er fra {sted}.')

'''Flytt koden som leser inn informasjon og skriver ut en
 hilsen til en egen prosedyre. Kall denne prosedyren 3 
 ganger slik at du får lest inn og skrevet ut informasjon 
 om 3 personer.'''

def gjenta():
	navn = input('Skriv inn et navn: ')
	sted = input('Hvor kommer du fra? ')
	return(f'Hei {navn}! Du er fra {sted}.')

gjenta()
gjenta()

# Jeg skjønner ikke helt hvorfor den gjentar 3 ganger når jeg bare caller funksjonen 2 ganger?


