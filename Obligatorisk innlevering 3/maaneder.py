# a) Skriv et program som inneholder en String-liste som inneholder alle månedsnavnene.
# b) Ta imot et heltall fra brukeren og skriv ut hvilken måned dette tilsvarer.
# c) Legg til en feilmelding dersom tallet ikke er et gyldig valg.

måned = ['Januar','Februar','Mars','April','Mai','Juni','Juli','August','September','Oktober','November','Desember']

tall = int(input('Tast inn et månedsnummer: '))

if tall >= 1 and tall <= 12:
	print(f'Dette tilsvarer {måned[tall-1]}.')
else:
	print('Du tastet et ugyldig månedsnummer!')
