import time
import os
import math
import sys

class printer:

	matrix_rows = []
	m_width = 30
	m_height = 10
	offset = [0,0]

	tail_output = [""]
	tail_visible = 10

	os_clear_cmd = ""

	def write(me, output: str):
		#global tail_output
		me.tail_output.insert(0, output)

	def erase(me, keep: int = 0):
		#global tail_output
		tail_output = tail_output[0:keep]

	# initializes necessary variables for running on different platforms
	def init(me, os: str):
		#global os_clear_cmd
		if os == "windows" or os == "ms" or os == "msdos":
			me.os_clear_cmd = "cls"
		elif os == "linux" or os == "unix":
			me.os_clear_cmd = "clear"
		else:
			me.os_clear_cmd = "$----- no known clear for: '" + os + "'. ------"

	# sets the top-left margin
	def off(me, origin: list):
		#global offset
		me.offset = origin[0:2]

	# sets the screen's dimensions and clears it.
	def size(me, columns: int, rows: int, max_tail: int = 10):
		#global m_height, m_width, tail_visible
		me.m_height = rows
		me.m_width = columns
		for row in range(0, rows):
			col = [" "] * columns
			me.matrix_rows.append(col)
		me.tail_visible = max_tail

	# resets all on-matrix values to empty or a provided character.
	def clr(me, fill: chr = " "):
		rows = len(me.matrix_rows)
		cols = len(me.matrix_rows[0])
		for y in range(0, rows):
			for x in range(0, cols):
				me.matrix_rows[y][x] = str(fill)[0]

	# prints the matrix out into the standard output.
	def draw(me):
		mat = ""
		for y in range(0, me.offset[1]):
			mat += " \n" if y < me.offset[1]-1 else (" " * (me.offset[0]-1) + "+--\n")
		for row in range(0, len(me.matrix_rows)):
			if row < 2:
				mat += (" " * (me.offset[0]-1)) + "|" + "".join(me.matrix_rows[row]) + "\n"
			else:
				mat += (" " * me.offset[0]) + "".join(me.matrix_rows[row]) + "\n"
		try: 
			if me.os_clear_cmd[0] != "$":
				os.system(me.os_clear_cmd)
			else:
				print(me.os_clear_cmd)
		except:
			pass
		print( mat )
		print("  ---")
		tails = len(me.tail_output)
		for line in me.tail_output[0:min(tails, me.tail_visible)]:
			print("> " + line)
		if tails < me.tail_visible:
			for empty in range(0, me.tail_visible - tails):
				print(".")
		print("  ---")

	########------- END INITIALIZATIONS, BEGIN PROGRAMS -------########

	# sets a single 'pixel' of the matrix
	def set(me, x: float, y: float, value: str):
		if x < 0 or x >= me.m_width or y < 0 or y >= me.m_height:
			#write("out of bounds: " + str(x) + ", " + str(y))
			pass
		else:
			me.matrix_rows[int(y)][int(x)] = value[0]

	# finds the adjusted min and max of a set of [x,y] data
	def dataExtrema(me, data: list):
		# adjusts min and max to be at most 1 away from true min/max
		x_min = data[0][0] 
		x_max = data[0][0] + 1
		y_min = data[0][1] 
		y_max = data[0][1] + 1
		for [x, y] in data[1:]:
			if x < x_min: 
				x_min = x
			if x > x_max: 
				x_max = x
			if y < y_min: 
				y_min = y
			if y > y_max: 
				y_max = y
		return [x_min, x_max, y_min, y_max]

	# automatically scales a set of data plotted [x,y]
	def quickplot(me, data: list, dot: chr = '+'):
		ext = me.dataExtrema(data)
		me.write(str(ext))
		x_scale = float(me.m_width) / (ext[1] - ext[0])
		y_scale = float(me.m_height) / (ext[3] - ext[2])
		me.write(str(x_scale) + ", " + str(y_scale))
		me.clr(".")
		for [x, y] in data:
			me.set((x - ext[0]) * x_scale , me.m_height - ((y - ext[2]) * y_scale ), dot)
		horiz = me.m_height - (0 - ext[2]) * y_scale
		for x in range(0, me.m_width):
			me.set(x, horiz, "=")

	# process execution variables
	# def getArgv(index: int, default = "unspecified"):
		# index += 1 # selects first argument rather than the file
		# return sys.argv[index] if len(sys.argv)-1 >= index else default

	def __init__(self, os: str, width: int, height: int):
		self.init(os)
		self.size(width, height)
		self.off([5,2])

