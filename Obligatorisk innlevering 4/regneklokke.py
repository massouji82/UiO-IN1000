# 1.Lag et program som bruker en while-løkke for å  
# lese inn tall fra brukeren helt til brukeren taster 0, 
# uten å gjøre noe mer med tallene.

# def null():
# 	tall = ''
# 	while tall != 0:
# 		tall = int(input('Tast inn et tall: '))

# null()
	
# 2.Utvid programmet ved å lage en tom liste før while-løkken. 
# Deretter skal du endreløkken slik at den for hver gjennomkjøring 
# lagrer tallet brukeren taster inn i  denne listen.

# def null():
# 	liste = []
# 	tall = ''
# 	while tall != 0:
# 		tall = int(input('Tast inn et tall: '))
# 		liste.append(tall)
		
# null()

# 3.Etter at while-løkken er ferdig, skriv en for-løkke som 
# går gjennom lista og skriver uthvert enkelt element.

# def null ():
# 	liste = []
# 	tall = ''
# 	while tall != 0:
# 		tall = int(input('Tast inn et tall: '))
# 		liste.append(tall)
# 	for item in liste:
# 		print(item) 

# null()

# 4.Utvid programmet med en variabel ​minSum​. Skriv så en ny for-løkke 
# som går gjennom listen du laget tidligere og legger verdien til ​
# minSum​. Skriv deretter ut summen til brukeren.

# def null ():
# 	liste = []
# 	minSum = 0
# 	tall = ''
# 	while tall != 0:
# 		tall = int(input('Tast inn et tall: '))
# 		liste.append(tall)
# 	for item in liste:
# 		print(item) 
# 		minSum += item
# 	return(f'Summen er {minSum}.')

# print(null())

# 5.Bruk to separate for-løkker til å finne henholdsvis det minste og 
# det største elementet i lista, og skriv ut disse.

def null ():
	liste = []
	minSum = 0
	tall = ''
	while tall != 0:
		tall = int(input('Tast inn et tall: '))
		liste.append(tall)
	for item in liste:
		if item != 0: # Put in !=0 because 0 is used to terminate the while loop.
			print(item) 
			minSum += item	
	minst = liste[0]
	størst = liste[0]
	for item in liste:	
		if item < minst and item != 0: #Put in !=0 because 0 is used to terminate the while loop.
			minst = item
		if item > størst and item != 0: #Put in !=0 because 0 is used to terminate the while loop.
			størst = item
	print(f'Summen er {minSum}.')
	print(f'Minste elementet er {minst}.')
	return(f'Største elementet er {størst}.')

print(null())



