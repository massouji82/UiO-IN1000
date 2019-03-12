# I denne oppgaven skal du lage et spill for to, der en 
# spiller skal gjemme en skatt i et todimensjonalt skattekart, 
# og den andre spilleren skal gjette hvor skatten er.

# a) Spillet skal begynne med å tegne opp skattekartet. 
# Kartet består av en nøstet liste som vi for enkelhets skyld 
# gjør kvadratisk. Dette betyr at vi kun trenger å holde styr 
# på en variabel for å vite lengden og bredden på listen. 
# En grei størrelse på kartet kan være 5 ganger 5.

skattekart = []
stoerrelse = 5

for e in range(stoerrelse):
	a = []
	for e in range(stoerrelse):
		a.append('O')
	skattekart.append(a)

# for e in skattekart:
# 	for f in e:
# 		print(f, end='')
# 	print('')

# b) Deretter må vi be spiller nummer 1 om input. Spiller 1 oppgir x 
# og y-koordinater, og hvis koordinatene er gyldige (les: innenfor 
# de mulige plassene på kartet) blir de tegnet inn som en "X" i kartet. 
# For å få til dette kan du for eksempel gjøre følgende:
# * Lag en løkke som spør etter input til den har fått gyldige koordinater.
# * I denne løkken, ta imot input fra brukeren og gjør nødvendige sjekker 
# (er det tall? Er det gyldige koordinater?).
# * Hvis alt ser greit ut, legg koordinatet inn i kartet og la spillet gå videre.

print('Spiller 1, hvor vil du gjemme skatten?')

skatt = False

while skatt != True:
	in_x = input('Tast inn x-koordinat (1 til 5): ')
	in_y = input('Tast inn y-koordinat (1 til 5): ')
	if in_x.isdigit() and in_y.isdigit():
		x = int(in_x)
		y = int(in_y)
		if (x <= stoerrelse and x > 0 and y <= stoerrelse and y > 0):
			skattekart[y-1][x-1] = 'X'
			skatt = True
		else:
			print('Ugyldig plassering!')
	else:
		print('Ugyldig input!')

# c) Så skal vi hente input fra spiller nummer to. For å unngå at spiller 
# 2 ser koordinatene som er oppgitt kan det først være lurt å lage en løkke 
# som skriver ut en del linjeskift, slik at skjermen tilsynelatende blir tømt.

# La spiller 2 få tre forsøk på å finne skatten. Selve sjekkingen kan du gjøre 
# mye på samme måte som i oppgave b, men du vil også ha en løkke som lar brukeren 
# fortsette å gjette til de er tomme for forsøk eller til de har funnet skatten. 
# Hvis spilleren gjetter feil kan du lagre gjetningen som et firkantsymbol ("#") 
# på kartet. Hvis skatten blir funnet skal spilleren gratuleres, ellers vinner spiller 1.

for e in range(80): 
	print('')

skattekart2 = []
stoerrelse = 5

for e in range(stoerrelse):
	a = []
	for e in range(stoerrelse):
		a.append('O')
	skattekart2.append(a)

print('Spiller 2, du får 3 forsøk på å gjette hvor Spiller 1 gjemte skatten.')

i = 0

for i in range(3):
	in_x2 = input('Tast inn x-koordinat (1 til 5): ')
	in_y2 = input('Tast inn y-koordinat (1 til 5): ')
	if in_x2.isdigit() and in_y2.isdigit():
		x2 = int(in_x2)
		y2 = int(in_y2)
		if (x2 <= stoerrelse and x2 > 0 and y2 <= stoerrelse and y2 > 0):
			if x2 == x and y2 == y:
				print('***Gratulerer Spiller 2! Du gjettet riktig***!')
				quit()
			else:
				print('Du gjettet feil!')
				skattekart[y2-1][x2-1] = '#'
				i += 1
		else:
			print('Ugyldig plassering!')
	else:
		print('Ugyldig input!')

# d) Til slutt kan du skrive ut kartet til spillerne på nytt, 
# slik at de kan se hvilke gjetninger som ble gjort og hvor skatten ble gjemt.

for e in skattekart:
	for f in e:
		print(f, end='')
	print('')







