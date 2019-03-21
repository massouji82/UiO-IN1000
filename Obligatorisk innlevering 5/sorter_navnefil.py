# P Martin
# H Trofast
# H Tapper
# H Rex
# P Simen
# P Elin
# H Tara
# P Svein 

# Teksten over er en liste over navn. De linjene som starter med P, 
# nneholder et navn til en person, mens linjene som starter med H er 
# for en hund. Start med å kopiere over listen til en fil du kaller navn.txt.

# Skriv et program som leser inn denne filen og sorterer navnene i to 
# lister, en du kaller personer og en du kaller hunder.

# personer = []
# hunder = []

# with open('navn.txt', 'r') as n:
# 	for line in n:
# 		if line.startswith('P'): 
# 			personer.extend(line.split())
# 			personer.remove('P')
# 		if line.startswith('H'):
# 			hunder.extend(line.split())
# 			hunder.remove('H')

# print(f'Personer:\n{personer}')
# print(f'Hunder:\n{hunder}')

personer = []
hunder = []

n = open('navn.txt', 'r')
for line in n:
	if line[0] == 'P': 
		personer.append(line[2:].split())
	elif line[0] == 'H':
		hunder.append(line[2:].split())

n.close()

print(f'Personer:\n{personer}')
print(f'Hunder:\n{hunder}')



