import matrixPrint as mP
import sys
import math
import time

[call, os, w, h] = sys.argv[0:4]
screen = mP.printer(os, int(w), int(h))

i = 0

while True:
	data = []
	for x in range(-200, 200):
		data.append([x/10, 10 * math.asinh(.25 * x/10 + i)])
	screen.quickplot(data)
	screen.draw()
	i += .1
	time.sleep(1)