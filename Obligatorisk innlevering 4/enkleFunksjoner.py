# a) Skriv en prosedyre velkommen som tar imot en variabel 
# bruker som parameter og skriver ut en velkomstmelding med 
# dette navnet. Test funksjonen ved å be bruker om en 
# tekststreng brukernavn og kalle på velkommen med dette som 
# parameter.

def velkommen(bruker):
	print(f'Velkommen {bruker}.')

brukernavn = input('Tast inn ditt brukernavn: ')

velkommen(brukernavn)

# b) Skriv en funksjon strenginator(streng1, streng2) som legger 
# ammen (konkatenerer) to strenger med et mellomrom og returnerer 
# den sammenslåtte strengen. Kall på metoden med to strenger med 
# verdi du velger selv og legg returverdien i en konkatenert. 
# Skriv ut konkatenert til terminal.

def strenginator(streng1, streng2):
	return streng1 + ' ' + streng2 + '.'

streng1 = 'Spis'
streng2 = 'mat'

konkatenert = strenginator(streng1, streng2)

print(konkatenert)



