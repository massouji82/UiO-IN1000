# a) Skriv et program som leser inn en fil tall.txt, 
# som har et tall på hver linje, og legg disse inn i en liste. 

l = []
with open('tall.txt', 'r') as t:
	for line in t:
		l.append(int(line))

# # b) Skriv en funksjon antall_forekomster som tar imot en liste 
# # og et heltall. Funksjonen skal finne ut hvor mange ganger tallet 
# # som tas imot forekommer i listen og returnere antallet forekomster.

def antall_forekomster(lst, heltall):
	times = 0
	for i in lst:
		if heltall == i:
			times += 1
	return times

# c) Skriv en funksjon flest_forekomster som tar imot en liste og 
# finner og returnerer det tallet som forekommer flest ganger. 
# Du trenger ikke ta høyde for at flere tall kan forekomme like ofte.

def flest_forekomster(lst):
	return max(lst, key=lst.count)

# d) Test begge funksjonene dine!

print('Tallet 2 forekommer', antall_forekomster(l, 2), 'ganger.')
print('Tallet', flest_forekomster(l), 'forekommer flest ganger.')