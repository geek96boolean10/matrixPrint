import math
from .matrixPrint import printer 

# forcefully edits a 2D matrix to display advanced graphics options
class artist:
	
	# requires a canvas that this artist normally paints on
	def __init__(me, mycanvas: printer):
		me.canvas = mycanvas
		
	# creates a line between the starting and ending points
	def line(me, start: list, end: list, value: chr = "#", resolution: float = 0.1):
		x_total = int(int(end[0]) - int(start[0]))
		x_step = float(x_total * resolution)
		y_total = int(int(end[1]) - int(start[1]))
		y_step = float(y_total * resolution)
		me.canvas.write([x_total, x_step, y_total, y_step])
		
		for i in range(0, int(x_total / resolution), 1 if x_step > 0 else -1):
			x = int(start[0]) + math.floor(i * resolution)
			y = int(start[1]) + math.floor(i * resolution)
			me.canvas.set(x, y, value)
	
	# takes the result of a printer and copies it into this canvas
	# target is a size-4 list, [x,y,width,height]. if the dimensions are smaller than the
	# source matrix, cropping will occur unless the scale is set accordingly.
	# alpha prevents ' '(space) characters from overwriting existing points
	def pip(me, source: printer, target: list, scale: float = 1, alpha: bool = False):
		# scale determines how many canvas pixels are used per source pixel
		for x in range(0, int(int(target[2]) * scale), 1):
			for y in range(0, int(int(target[3]) * scale), 1):
				# these x and y refer to canvas pixels
				src = source.get(int(x/scale), int(y/scale))
				if not (alpha and src == " "):
					me.canvas.set(x + int(target[0]), y + int(target[1]), src)

	# prints the given string with the provided cropping options
	# in a 1-to-1 manner, where each character occupies one pixel.
	# does not handle multiline.
	# returns the number of un-drawn characters
	def text(me, s:str, origin:list, maxwidth:int=-1, maxheight:int=1):
		if maxwidth > -1 and maxheight < 1:
			return # this is a skippable print; nothing will be visible
		charsleft = len(s)
		y = origin[1]
		while charsleft > 0:
			if y >= me.canvas.m_height or charsleft <= 0:
				break # exit while
			for x in range(origin[0], origin[0] + (len(s) if maxwidth < 1 else min(len(s), maxwidth))):
				if x < me.canvas.m_width and charsleft > 0:
					#print("set: " + str(x) + str(y)+str(len(s)-charsleft))
					me.canvas.set(x,y,s[len(s)-charsleft])
					charsleft -= 1
				else:
					break # exit for
			y += 1
		if charsleft > 0:
			return charsleft
		return 0

		