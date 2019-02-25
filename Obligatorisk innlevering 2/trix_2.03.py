#1.Skriv et program som tar imot en flyttall radius fra bruker.

radius = float(input('Tast inn radius: '))

#2.Beregn så diameter, areal og omkrets av sirkelen i tre nye variabler.

diameter = (radius * 2)
areal = radius * radius * 3.14
omkrets = diameter * 3.14

'''3.Skriv ut disse verdiene, men vis kun 2 desimaler. 
Sørg også for at tallene blir plassert like langt til høyre. 
Se under for eksempel på utskrift:'''

di = 'Diameter:'.ljust(10)
ar = 'Areal:'.ljust(10)
om = 'Omkrets:'.ljust(10)

print(f'{di} {diameter:.2f}\n{ar} {areal:.2f}\n{om} {omkrets:.2f}')

#Løste denne på en kronglete måte. Må finnes en bedre måte?



