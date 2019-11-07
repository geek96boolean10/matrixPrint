from matrixPrint import printer
from artist import artist
import sys
import math
import time

[call, os] = sys.argv[0:2]
[w, h] = [180, 45]
screen = printer(os, int(w), int(h))
a = artist(screen)
smol = printer(os, 120, 31, silent=True)

i = 0

while True:
	screen.erase(2)
	data = []
	for x in range(-200, 200):
		data.append([x/10, 10 * math.sin(.25 * x/10 + 5 * math.sin(i))])
	screen.pnplot(data)
	smol.pnplot(data)
	a.pip(screen, [30,7,120,31], .667, alpha=True)
	screen.draw()
	i += .02
	time.sleep(.1)
