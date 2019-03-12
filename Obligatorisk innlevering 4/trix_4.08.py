
# a) Lag en tom liste oliste. Bruk en for-løkke for å legge til strengen "o" i denne listen 5 ganger.

oliste = []

for n in range(5):
	oliste.append('o')

# b) Lag en tom liste stjerneliste og legg til strengen "*" 5 ganger på samme måte som i a.

stjerneliste = []

for n in range(5):
	stjerneliste.append('*')

# c) Lag en tom liste rutenett. Legg oliste inn i rutenett med rutenett.append(oliste).

rutenett = []

rutenett.append(oliste)

# d) Legg stjerneliste inn i rutenett på samme måte. Legg deretter inn oliste en gang til.

rutenett.append(stjerneliste)

rutenett.append(oliste)

# e) Skriv ut rutenett[0], rutenett [1] og rutenett[2] på hver sin linje. Test programmet ditt.

# print(rutenett[0])
# print(rutenett[1])
# print(rutenett[2])

# f) Endre programmet slik at innholdet av rutenett skrives ut ved hjelp av en enkel for-løkke. Test programmet på nytt.

for n in rutenett:
	print(n)

