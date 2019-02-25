''' 1.Les om formatering av utskrift på side 54-57 i læreboken (Python for Everyone) eller i Python-dokumentasjonen (https://docs.python.org/3/tutorial/inputoutput.html).
2.Skriv et program som inneholder tre forskjellige navn inneholdt i tre forskjellige variabler. Pass på at navnene er av forskjellig lengde.
3.Skriv ut navnene, men sørg for at navnene blir skrevet ut justert til høyre. Se under for eksempelutskrift:

Navn 1:      Arne
Navn 2:       Dag
Navn 3:     Ellen'''

navn1 = 'Arne'.rjust(10)
navn2 = 'Dag'.rjust(10)
navn3 = 'Ellen'.rjust(10)

print(f'Navn 1: {navn1}\nNavn 2: {navn2}\nNavn 3: {navn3}')

