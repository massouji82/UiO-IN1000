# a) Bruk open for å åpne filen "navn.txt". Se under for å se hvordan denne filen skal se ut.

fil = open('navn.txt', 'r')

# b) Lag en tom liste.

lst = []

# c) Legg til en løkke i programmet som går så lenge det finnes uleste linjer i filen. Legg til hver linje fra filen til listen.

for line in fil:
	lst.extend(line.split())

fil.close()

# d) Skriv ut listen til skjermen.

print(lst)