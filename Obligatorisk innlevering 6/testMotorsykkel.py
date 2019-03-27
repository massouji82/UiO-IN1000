# 5.I denne deloppgaven skal du teste programmet ditt. 
# Opprett en ny fil testMotorsykkel.py​. Øverst i filen 
# skal du importere klassen ​Motorsykkel​. Deretter skal 
# du skrive en prosedyre ​hovedprogram()​, slik som i oppgave 1.

from motorsykkel import Motorsykkel

def hovedprogram():

# 6.Inne i ​hovedprogram​ skal du opprette et objekt av 
# klassen ​Motorsykkel​ med et merke, et registreringsnummer 
# og en kilometerstand. Opprett to objekter til. Kall deretter 
# metoden ​skrivUt​ på alle objektene du har laget.

	sykkel1 = Motorsykkel('BMW', 'ER3335', 50)
	sykkel2 = Motorsykkel('Ducati', 'NO4554', 230)
	sykkel3 = Motorsykkel('Honda', 'RR3321', 115)

	sykkel1.skrivUt()
	sykkel2.skrivUt()
	sykkel3.skrivUt()

# 7.Øk kilometerstanden på den motorsykkelen du laget sist med 
# 10 km, og sjekk at kilometerstanden ble oppdatert ved å 
# skrive ut resultatet av ​hentKilometerstand​.

	sykkel3.kjor(10)
	print(f'Kilometerstand siste sykkel: {sykkel3.hentKilometerstand()}')

# 8.Husk å kalle på ​hovedprogram​ for å teste programmet.

hovedprogram()