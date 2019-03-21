# 1 Skriv oppgavetekst til en oppgave som handler om 
# innlesing fra fil og funksjoner. Eller du kan følge 
# dette forslaget: Skriv et beregningsprogram for 
# skreddere med en funksjon som leser inn en fil der 
# hver linje beskriver et navn på et mål og selve målet 
# i tommer. Formatet vil se slik ut:

# Skulderbredde 4
# Halsvidde 3.2
# Livvidde 10

# Hint​: du kan bruke funksjonen ​split​ for å gjøre dette.

# La programmet legge disse målene i en ordbok med navn 
# på målet som nøkkelverdi og returner ordboken. Lag 
# deretter en prosedyre som tar imot en liste av mål og 
# benytter seg av ​tommerTilCm​ som du skrev tidligere for 
# å skrive ut målene i centimeter

# 2.Løs oppgaven! Du skal levere både oppgaveteksten og 
# besvarelsen (skrivoppgaveteksten som kommentarer over løsningen din).

from regnefunksjoner import tommerTilCm

def skredder():
	ordbok = {}

	with open('egen_oppgave.txt', 'r') as egen:
		for line in egen:
			(key, val) = line.split()
			ordbok[key] = val
		return list(ordbok.values())

def konverter(ordbokVerdier):
    tommerListe = []
    for tommer in ordbokVerdier:
        tommerListe.append(tommerTilCm(float(tommer)))

    return tommerListe

print(konverter(skredder()))


