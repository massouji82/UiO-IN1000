# Vi skal i denne oppgaven lage en enkel telefonbok, der bruker kan søke på navn for å hente telefonnummer.

# a) Opprett en ordbok (dictionary).

ordbok = {}

# b) Fyll ordboken med følgende relasjoner. Navnet skal være nøkkel og telefonnummeret skal være verdien:
# ("Arne", 22334455)
# ("Lisa", 95959595)
# ("Jonas", 97959795)
# ("Peder", 12345678)

relasjoner = {
			"Arne":22334455,
			 "Lisa":95959595, 
			 "Jonas":97959795, 
			 "Peder":12345678
			 }

ordbok.update(relasjoner)

# c) La brukeren skrive inn et navn, skriv så ut telefonnummeret som hører til dette navnet. Hvis brukeren skriver inn et navn som ikke eksisterer i ordboken, gi en feilmelding som forteller at vi ikke har lagret dette nummeret.

navn = input('Tast inn et navn: ')
if navn in ordbok:
	print(f'Telefonnummeret til {navn} er {ordbok[navn]}.')
else:
	print(f'{navn} finnes ikke i vår telefonbok.')
