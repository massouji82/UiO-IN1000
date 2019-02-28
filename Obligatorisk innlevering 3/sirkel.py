 # I denne oppgaven skal du importere en ​modul​ for å 
 # gjøre en enkel grafikkoppgave. Modulendu skal hente 
 # heter EzGraphics og er gratis som en del av pensumboken 
 # Python for Everyone. Følg disse stegene:

 # 1.Les side 63-69 i Python for Everyone om hvordan du 
 # kan importere modulen og tegne figurer.

 # 2.Last ned ezgraphics-2.1.tar.gz herfra.

 # 3.Bruk pip i terminalen for å installere ezgraphics på 
 # ifi-brukeren din slik:pip install ​ezgraphics-2.1.tar.gz

 # 4.I ​sirkel.py​, importer ​ezgraphics.py​ og bruk informasjonen 
 # fra pensumboka for å tegne en rød sirkel.

from ezgraphics import GraphicsWindow

#Lag vindu og få tilgang til canvasen
win = GraphicsWindow(500, 500)
canvas = win.canvas()

#Tegn på canvasen
canvas.setColor('red')
canvas.drawOval(120, 120, 240, 240)

#Vent på at brukeren stenger vinduet
win.wait()