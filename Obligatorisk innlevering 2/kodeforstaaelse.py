'''Dette er en teorioppgave. Besvar teorispørsmålene 
som kommentarer øverst i kodeforstaaelse.py​.

Les følgende kode grundig og forsøk å svare på 
deloppgavene under. Test deretterbesvarelsen din ved å 
lime inn koden i ​kodeforstaaelse.py​ og kjøre programmet.'''

a = input('Tast inn et heltall: ')
b = int(a)
if b < 10:
	print(b + 'Hei!')

#	1.Er dette lovlig kode? Begrunn svaret.
#	Nei, det er ikke mulig å streng sammenkoble en int og en str.


#	2.Hvilke problemer vil vi kunne møte på når vi kjører denne koden?
#	Vi vil få en TypeError fordi + tegnet ikke kan brukes mellom en int og en str.
