# 1. Lag et grafikkvindu ​win​ med et kanvas ved navn ​can​ 
# som du kan tegne på som beskrevet i pensumboka.

from ezgraphics import GraphicsWindow

win = GraphicsWindow()
canvas = win.canvas()

# 2.Opprett to variabler: En ​teller​ med verdien 0, og en ​
# x_pos​ med verdien 10.

teller = 0
x_pos = 10
stoerrelse = 50

# 3.Skriv en while-løkke som fortsetter 
# så lenge ​teller​ er mindre enn 9. For hver gangløkken 
# kjører skal det tegnes en sirkel, slik:

# can​.​drawOval​ (​x_pos​,​​100​,​​50​,​​50​)

# ... der de tre siste parametrene betegner henholdsvis y-posisjon, 
# høyde og breddepå sirkelen. Etter at en sirkel er tegnet skal 
# du øke ​x_pos​ med et tall du velger selv. Husk også å inkrementere ​teller​.

while teller < 9:
	canvas.drawOval(x_pos, 150, stoerrelse, stoerrelse)
	x_pos += 14
	teller += 1
	stoerrelse += 5

# 4.Lag en variabel ​stoerrelse​ før løkken din, med en valgfri verdi. 
# Endre løkken din slik at høyde og bredde på sirkelen bestemmes av ​
# stoerrelse​. La størrelsen økes med 5 for hver gjennomkjøring av løkken.

win.wait()
