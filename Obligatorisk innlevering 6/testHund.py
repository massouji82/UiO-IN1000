# 5.Skriv en ​hovedprogram​-prosedyre i ​testHund.py​, der du oppretter
# et hundeobjekt.Sjekk objektet ved å kalle på ​spring ​og ​spis​ minst 
# 2 ganger hver, og skriv ut hundens vekt​ hver gang. Husk å kalle 
# på ​hovedprogram​ i filen din.

from hund import Hund

def hovedprogram():
	Lucie = Hund(5, 11)
	
	Lucie.alder()
	Lucie.spring()
	Lucie.spring()
	Lucie.spring()
	Lucie.spring()
	Lucie.spring()
	Lucie.spring()
	Lucie.spring()
	Lucie.vekt()
	Lucie.spis(3)
	Lucie.vekt()
	Lucie.spis(2)
	Lucie.vekt()

hovedprogram()



