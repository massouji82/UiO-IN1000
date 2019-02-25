# Dette er en tekstoppgave. Du kan gjøre den med penn og papir 
# og ta et bilde eller scanneinn arket, eller du kan gjøre den på 
# datamaskin. Du skal levere oppgaven som en PDF-filsammen med de 
# andre kodefilene i Devilry. 

# Du skal forklare programflyten til et program, det vil si i hvilken 
# rekkefølge de forskjelligelinjene utføres når vi kjører programmet. 
# Du skal gjøre dette ved å skrive tall foran linjene iprogrammet. 
# Tallene beskriver i hvilken rekkefølge programsetningene utføres, 
# slik at 1 er den første setningen som utføres, 2 er den neste, og så videre.
# Her er et eksempel (leggmerke til tallrekkefølgen oppgitt til venstre!):

# # 1​  a ​=​ 13
# # 2​  if​ a ​<​​10:​
# # 		print​(​"Mindre!"​)
# # 3​  else:
# # 4  		​​print​(​"Ikke mindre!"​)

# Som vi ser definerer vi først en variabel ​a​ med verdien 13. 
# Så sjekker vi om ​a​ er mindre enn 10. Ettersom dette ikke stemmer 
# utføres ikke neste linje, men vi går istedet videre til ​else​ 
# og utfører setningen vi finner der.

# Hvis en linje kjøres flere ganger (for eksempel ved flere kall på 
# samme funksjon) kan du skrive flere tall ved siden av setningen.
# Beskriv programflyten når følgende program kjøres. 
# Som du ser tar programmet input frabruker, og ​du skal her anta at 
# brukeren under kjøring av programmet taster inn tallet 8​.

1 4 11 def​ print_prosa​():    
  5	12 print​(​"Melding til alle gaardeiere:"​)    
  6	13 print​(​"Antall dyr paa gaarden: "​)

2 antall_dyr ​=​ 4
3 print_prosa​()
7 print​(​antall_dyr)
8 antall_nye_dyr ​=​​int​(​input​(​"Hvor mange nye dyr kommer til gaarden: "​))
9 antall_dyr ​=​ antall_dyr ​+​ antall_nye_dyr
10 print_prosa​()
14 print​(​antall_dyr)

if​ antall_dyr ​>​​12:    
	print​(​"Det er mer enn ett dusin dyr paa gaarden!"​)
15 elif​ antall_dyr ​==​​12:    
	16 print​(​"Det er ett dusin dyr paa gaarden!"​)
else:    
	print​(​"Det er mindre enn ett dusin dyr paa gaarden!"​)