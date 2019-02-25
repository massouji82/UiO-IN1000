'''Du skal skrive et verktøy for å konvertere 
en gitt temperatur fra fahrenheit til celsius.

1.Skriv et program med en variabel som er temperatur 
i fahrenheit, bestem selv hvatemperaturen skal være 
og hva variabelen skal hete.'''

# fahrenheit = '100'

fahrenheit = input('Skriv inn temperaturen i fahrenheit: ')

#2.Skriv ut temperaturen i fahrenheit.

print(fahrenheit)

'''3.Definer en ny variabel som bruker variabelen i 
punkt 1 til å finne temperaturen icelsius. 
For å regne om fra fahrenheit til celsius kan du 
ruke denne formelen:
((temperatur i fahrenheit) − 32) ∗ 5/9.'''

celsius = (int(fahrenheit)-32)*5/9

#4.Skriv ut temperaturen i celsius.

print(celsius)

'''5.Modifiser programmet slik at variabelen for 
fahrenheit blir gitt via brukerinput. ​
Sørg for at variabelen får en tallverdi!​ 
Sjekk så programmet ditt ved å kjøre det og 
tasteinn tallet 100. Får du ca 37,78 grader celsius? 
Hvis ikke, sjekk at du har fulgt formelen gitt over.'''





