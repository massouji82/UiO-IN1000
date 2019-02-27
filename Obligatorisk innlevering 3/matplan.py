# I denne oppgaven skal vi se for oss at hver beboer 
# på et gitt sykehjem spiser tre måltider på en gitt dag.

# 1.Lag en ordbok hvor hver nøkkelverdi er navnet til en beboer, 
# og innholdsverdien er en liste med tre måltider. 
# Måltidene skal være henholdsvis frokost, lunsj og middag.
# For eksempel spiser Kari Nordmann brød til frokost, 
# egg til lunsj og pølser til middag.

# 2.Lag så en prosedyre hvor brukeren kan skrive navnet til en 
# beboer i terminalen, og få skrevet ut matplanen til den beboeren. 
# Skriv ut en melding til brukeren hvis beboeren ikke er registrert.

matplan = {'julie':['Brødskiver', 'Grøt', 'Spaghetti'],
		'muhammed':['Cornflakes', 'Shawarma','Hamburgere'],
		'elin':['Knekkebrød','Omelett','Laks']
		}

def mat():
	beboer = input('Hva er navnet til bebober? ')
	beboer = beboer.lower()
	if beboer in matplan:
		return(matplan[beboer])
	else:
		return(f'{beboer} er ikke registrert.')

print(mat())