from matrixPrint import printer
from artist import artist
import sys
import math
import time

[call, os] = ["", "windows"]
[w, h] = [180, 45]
screen = printer(os, int(w), int(h))
a = artist(screen)
smol = printer(os, 120, 31, silent=True)

i = 0

while True:
	a.push([i,i])
	a.rect([0,0], [4,4], str(i), str(i))
	screen.draw()
	i+= 1
	time.sleep(1)
