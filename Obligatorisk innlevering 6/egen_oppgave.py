# Skriv oppgavetekst til en oppgave som handler om klasser 
# og objekter! Eller du kan prøve følgende forslag:

# Skriv en klasse Person med en konstruktør som tar imot navn og alder. 
# I tillegg skal konstruktøren ha en tom liste ​hobbyer​. Skriv en metode ​
# leggTilHobby​ som tar imot en tekststreng og legger den til i ​hobbyer​-listen. 
# Skriv også en metode ​skrivHobbyer​. Denne metoden skal skrive alle hobbyene 
# etter hverandre på en linje. Gi deretter Person-klassen en metode ​skrivUt​ 
# som i tillegg til å skrive ut navn og alder kaller på metoden ​skrivHobbyer​. 
# La brukeren skrive inn navn og alder, og lag et Person-objekt med informasjonen 
# du får. Deretter skal brukeren ved hjelp av en løkke få legge til så mange 
# hobbyer de vil. Når brukeren ikke lenger ønsker å oppgi hobbyer skal statistikk 
# om brukeren skrives ut.

class Person():
	def __init__(self, navn, alder, hobbyer=[]):
		self.navn = navn
		self.alder = alder
		self.hobbyer = hobbyer

	def leggTilHobby(self, hobby):
		self.hobbyer.append(hobby)

	def skrivHobbyer(self):
		for n in self.hobbyer:
			print(n)

	def skrivUt(self):
		print(f'Navn: {self.navn}, Alder: {self.alder}')
		print(f'Hobbyer:') 
		print(person.skrivHobbyer())

navn = input('Tast inn ditt navn: ')
alder = input('Tast inn din alder: ')

person = Person(navn, alder)

go = True
while go == True:
	igjen = input('Vil du legge til en hobby?(ja/nei): ')
	if igjen.lower() == 'ja':
		hobby = input('Hva er din hobby? ')
		person.leggTilHobby(hobby)
	elif igjen.lower() == 'nei':
		person.skrivUt()
		go = False
	else:
		print('Vennligst svar "ja" eller "nei".')


	

