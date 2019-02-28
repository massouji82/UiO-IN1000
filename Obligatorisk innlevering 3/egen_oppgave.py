# 1.Skriv oppgavetekst til en oppgave som handler om lister 
# eller ordbøker. Et forslag kan være å skrive en quiz som i 
# forrige uke, men ved å bruke lister. Eller du kan bruke dette 
# forslaget: Skriv et program som tar imot koordinater samt 
# høyde og bredde fra bruker, legger disse etter hverandre i en 
# liste og deretter bruker innholdet i listen til å tegne opp en 
# form med EzGraphics.

# 2.Løs oppgaven! Du skal levere både oppgaveteksten og besvarelsen 
# (skriv oppgaveteksten som kommentarer over løsningen din).

from ezgraphics import GraphicsWindow

#Lag vindu og få tilgang til canvasen
win = GraphicsWindow(500, 500)
canvas = win.canvas()

#Få koordinater fra bruker
x = input('Tast inn en x-koordinat: ')
y = input('Tast inn en y-koordinat: ')
høyde = input('Tast inn høyde: ')
bredde = input('Tast inn bredde: ')

bruker = [x,y,høyde,bredde]

#Tegn på canvasen
canvas.setColor('red')
canvas.drawOval(*bruker)

#Vent på at brukeren stenger vinduet
win.wait()

