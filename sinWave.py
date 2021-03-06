from matrixPrint import printer
from artist import artist
import sys
import math
import time

[call, os, w, h] = sys.argv[0:4]
screen = printer(os, int(w), int(h))
a = artist(screen)

i = 0

while True:
	#screen.erase(2)
	data = []
	for x in range(-200, 200):
		data.append([x/10, 10 * math.sin(.25 * x/10 + i)])
	screen.pnplot(data)
	a.line([0,0], [4,4], "a")
	screen.draw()
	i += .1
	time.sleep(.1)
