# a) Lag et program som tar et tall som input fra 
# bruker, og printer alle tall fra 0 opp til dette 
# tallet (hint: while ...).

# tall = int(input('Tast inn et heltall: '))
# teller = 0
# while teller < tall:
# 	print(teller)
# 	teller += 1

# b) Utvid programmet med en ny while-løkke som ber
#  om input fra bruker for hver "runde". Når brukeren 
#  taster tallet 10, skal programmet avsluttes.

tall = 0

while tall != 10:
	tall = int(input('Tast inn et heltall: '))
	print(f'Du tastet {tall}, programmet avsluttes.')


	
