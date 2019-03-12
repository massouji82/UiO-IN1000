# 1.Skriv et program med en funksjon ​adder (tall1, tall2)​ 
# som tar to heltall som parametere. Funksjonen skal summere 
# tallene og returnere resultatet. Kall på funksjonen to ganger 
# med argumenter du selv velger, og skriv ut resultatene med en
# passende tekst.

def adder(tall1=1, tall2=1):
	sum = tall1 + tall2
	return(f'Summen av dine to tall blir {sum}.')

print(adder(20,3))

# 2.Be så brukeren om å skrive inn en tekststreng, og deretter en 
# bokstav. Programmet skal så skrive ut hvor mange ganger den 
# oppgitte bokstaven forekommer i den oppgitte tekststrengen. 
# Du skal ikke regne stor og liten bokstav som like (for eksempel 
# vil det si at det er 0 forekomster av “​E”​ i ordet ​“hei”​).

def tellForekomst():
	tekst = input('Skriv en tekststreng: ')
	bokstav = input('Skriv en bokstav: ')

	antall = (tekst.count(bokstav))

	return(f'Din valgte bokstav forekom {antall} gang(er) i din tekst.')

print(tellForekomst())

# 3.Skriv en funksjon ​tellForekomst (minTekst, minBokstav)​. 
# Funksjonen skal telle hvor mange ganger en bokstav ​minBokstav​ 
# forekommer i teksten ​minTekst​, og returnere dette tallet. 
# Skriv deretter om kodelinjene fra punkt 2 til å benytte denne 
# funksjonen, men sørg for at programmet fremstår helt likt for 
# brukeren når det kjøres. Lever programmet slik det ser ut etter 
# at du har gjort denne endringen (du trenger altså ikke å levere 
# to versjoner av programmet).

# def tellForekomst(minTekst, minBokstav):
# 	return(minTekst.count(minBokstav))

# print(tellForekomst('Jeg gikk en tur i skogen.','J'))

