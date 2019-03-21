def​ minFunksjon​():
	for​ x ​in​ range​(​2​):    
		c ​=​ 2​
		print​(​c)    
		c ​+=​ 1    
		b ​=​​10    
		b ​+=​ a​
		print​(​b​)
	return​(​b​)

def hovedprogram():
	a ​=​​ 42
	b ​=​ 0
	print​(​b​)
	b ​=​ a
	a ​=​ minFunksjon​()
	print​​(​b​)
	print​​(​a​)

hovedprogram()

# # 'Først defineres funksjonen "minFunksjon​", som ikke skal ta imot noen parametere.
# # Deretter defineres prosedyren ​"hovedprogram​" som heller ikke har noen parametere. 
# # Deretter kalles hovedprogram​. Inne i hovedprogram​ opprettes variabel a med verdi 42.
# # Deretter opprettes variabel b med verdi 0. Så printes variabel b til terminal som gir
# verdien 0. Deretter redefineres variabel b til a. Deretter redefineres variabel a til 
# resultate av minFunksjon​() og funksjonen kalles. Funksjonen kjøres x ganger i range(2).
# Først opprettes variabel c med verdi 2. Så printes c til terminal som gir verdien 2.
# Deretter økes c med 1. Deretter redefineres b til verdien 10. Så økes variabel b med 
# variabel a. Dette fører til en NameError ettersom variabel a ikke er definert inne i 
# funksjonen minFunksjon​ og programmet stopper. 
