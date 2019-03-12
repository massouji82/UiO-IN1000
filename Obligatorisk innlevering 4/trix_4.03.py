# a) Definer en liste som inneholder følgende verdier:
# 6, -4, 7, -2, 8, -3, 9, -11.

lst = [6, -4, 7, -2, 8, -3, 9, -11]

# b) Bruk en for-løkke til å iterere igjennom alle 
# verdiene i listen og finn den minste verdien. 
# Skriv ut den minste verdien. Gjør dette uten å bruke 
# Python sin innebygde min-funksjon.

t = 0

for l in lst:
	if l > t:
		t += 1
print(l)


# c) Bruk en ny for-løkke tilsvarende oppgave b, 
# men finn og skriv ut den største verdien.

t = lst[0]

for l in lst:
	if l > t:
		t = l

print(t)
