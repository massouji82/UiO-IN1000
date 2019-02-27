# I denne oppgaven skal du lage et system som beregner 
# billettpris avhengig av kjøperens alder.

# 1.Lag en prosedyre, velg navnet selv. Prosedyren skal 
# inneholde en variabel ​alder​ og be brukeren om å skrive 
# inn alderen sin.

# 2.Utvid prosedyren med en variabel ​billettpris​, som du 
# foreløpig gir tallverdien 0.	

# 3.Videre skal prosedyren inneholde en if-else-sjekk. 
# Den skal sjekke følgende:

# a.Hvis brukeren er under eller akkurat 17 år gammel 
# skal billettprisen​​være 30 kroner (barnebillett).

# b.Ellers, hvis brukeren er over 17 år gammel, 
# blir billettprisen 50 kroner.

# c.Ellers, hvis brukeren er 63 år eller eldre, blir 
# billettprisen 35 kroner(pensjonistbillett).	

# 4.Til slutt skal prosedyren på en ryddig måte skrive ut 
# billettprisen til brukeren.

# 5.Kall prosedyren 4 ganger.

# 6.Hva er problemet med denne prosedyren? 
# Skriv svaret som en kommentar underprosedyren.

def billett():
	alder = int(input('Tast inn din alder: '))

	billettpris = '0'

	if alder <= 17:
		billettpris = 30

	elif alder > 17:
		billettpris = 50

	elif alder >= 63:
		billettpris = 35

	return(f'Din billett koster {billettpris} kr.')

print(billett())
print(billett())
print(billett())
print(billett())

# Problemet til denne prosedyren er at pensjonistbillett 
# alternativet aldri vil bli realisert ettersom 'over 17' kommer 
# først i if-else-sjekk rekkefølgen.





