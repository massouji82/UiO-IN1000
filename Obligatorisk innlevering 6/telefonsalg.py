# I denne oppgaven skal du skrive et program som tar inn data 
# fra fil og skriver ut statistikk for et telefonsalg-firma. 
# For å gjøre dette skal du lese inn tekst fra en fil som er 
# formatert slik at det er to ord på hver linje, adskilt av et 
# mellomrom, der det første ordet er et navn og det andre ordet 
# er et salgstall, slik:

# Heidi 133 
# John 97 
# Kari 48

# 1.Skriv en funksjon ​innlesing​, med et parameter ​filnavn​. Denne 
# funksjonen skal lese inn en fil ved hjelp av ​filnavn​ og legge 
# alle linjene i filen inn i en ordbok, der den ansattes navn blir 
# nøkkelverdien og antallet salg blir innholdsverdien (husk å 
# konvertere innholdsverdien til et heltall). Funksjonen skal deretter 
# returnere ordboken. 

def innlesing(filnavn):
	ordbok = {}
	with open(filnavn, 'r') as tele:
		for line in tele:
			(key, val) = line.split()
			ordbok[key] = val
		return ordbok

# print(innlesing('telefonsalg.txt'))

# Hint: ​Du kan bruke streng-funksjonen ​split​ med “ “ (mellomrom) som 
# parameter for å dele opp hver linje.

# 2.Lag en prosedyre ​maanedensSalgsperson​ som tar imot en ordbok, går 
# gjennom denne og skriver ut navn og antall salg for den personen som 
# solgte mest denmåneden.

def maanedensSalgsperson(ordbok):
	ordbok_int = {k:int(v) for k, v in ordbok.items()}
	
	max_value = max(ordbok_int.values()) 
	max_keys = max(ordbok_int, key=ordbok_int.get)
	
	print(f'\nMaanedens ansatte er {max_keys} med {max_value} salg.')

	# max_keys = [k for k, v in ordbok_int.items() if v == max_value]

# 3.Skriv en funksjon ​totaltAntallSalg ​som tar imot en ordbok og returnerer 
# summen av verdiene i ordboken.

def totaltAntallSalg(ordbok):
	ordbok_int = {k:int(v) for k, v in ordbok.items()}

	total = sum(ordbok_int.values())

	print(f'Totalt antall salg: {total}')

# 4.Lag en funksjon ​gjennomsnittSalg ​som tar imot en ordbok og 
# returnerergjennomsnittet av verdiene dens. ​Hint:​ Funksjonen ​totaltAntallSalg​ 
# gir deg allerede halvparten av løsningen her!

def gjennomsnittSalg(ordbok):
	ordbok_int = {k:int(v) for k, v in ordbok.items()}

	total = sum(ordbok_int.values())
	snitt = total/len(ordbok_int.keys())

	print(f'Gjennomsnittlig antall salg per salgsperson: {snitt}\n')

# 5.Til slutt skal du skrive en prosedyre ​hovedprogram()​. Inne i ​hovedprogram​ 
# skal du skrive ut den faktiske statistikken. Bruk funksjonene og prosedyrene 
# du har laget, og  skriv i tillegg ut antall selgere som ble lest inn. 
# Filen du skal bruke for å teste programmet ditt er ​salgstall.txt​ (legg gjerne 
# ved denne når du leverer oppgaven).

def hovedprogram(arg):
	maanedensSalgsperson(arg)
	selgere = len(arg.keys())
	print(f'\nAktive selgere denne maaneden: {selgere}')
	totaltAntallSalg(arg)
	gjennomsnittSalg(arg)

# 6.Kall på ​hovedprogram()​ for å teste programmet ditt.

hovedprogram(innlesing('salgstall.txt'))


