import time
import os
import math
import sys

matrix_rows = []
m_width = 30
m_height = 10
offset = [0,0]

tail_output = [""]
tail_visible = 10

os_clear_cmd = ""

def write(output: str):
	global tail_output
	tail_output.insert(0, output)

def erase(keep: int = 0):
	global tail_output
	tail_output = tail_output[0:keep]

# initializes necessary variables for running on different platforms
def init(os: str):
	global os_clear_cmd
	if os == "windows" or os == "ms" or os == "msdos":
		os_clear_cmd = "cls"
	elif os == "linux" or os == "unix":
		os_clear_cmd = "clear"
	else:
		os_clear_cmd = "$----- no known clear for: '" + os + "'. ------"

# sets the top-left margin
def off(origin: list):
	global offset
	offset = origin[0:2]

# sets the screen's dimensions and clears it.
def size(columns: int, rows: int, max_tail: int = 10):
	global m_height, m_width, tail_visible
	m_height = rows
	m_width = columns
	for row in range(0, rows):
		col = [" "] * columns
		matrix_rows.append(col)
	tail_visible = max_tail

# resets all on-matrix values to empty or a provided character.
def clr(fill: chr = " "):
	rows = len(matrix_rows)
	cols = len(matrix_rows[0])
	for y in range(0, rows):
		for x in range(0, cols):
			matrix_rows[y][x] = str(fill)[0]

# prints the matrix out into the standard output.
def draw():
	mat = ""
	for y in range(0, offset[1]):
		mat += " \n" if y < offset[1]-1 else (" " * (offset[0]-1) + "+--\n")
	for row in range(0, len(matrix_rows)):
		if row < 2:
			mat += (" " * (offset[0]-1)) + "|" + "".join(matrix_rows[row]) + "\n"
		else:
			mat += (" " * offset[0]) + "".join(matrix_rows[row]) + "\n"
	try: 
		if os_clear_cmd[0] != "$":
			os.system(os_clear_cmd)
		else:
			print(os_clear_cmd)
	except:
		pass
	print( mat )
	print("  ---")
	tails = len(tail_output)
	for line in tail_output[0:min(tails, tail_visible)]:
		print("> " + line)
	if tails < tail_visible:
		for empty in range(0, tail_visible - tails):
			print(".")
	print("  ---")

########------- END INITIALIZATIONS, BEGIN PROGRAMS -------########

# sets a single 'pixel' of the matrix
def set(x: float, y: float, value: str):
	if x < 0 or x >= m_width or y < 0 or y >= m_height:
		#write("out of bounds: " + str(x) + ", " + str(y))
		pass
	else:
		matrix_rows[int(y)][int(x)] = value[0]

# finds the adjusted min and max of a set of [x,y] data
def dataExtrema(data: list):
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
def quickplot(data: list, dot: chr = '+'):
	ext = dataExtrema(data)
	write(str(ext))
	x_scale = float(m_width) / (ext[1] - ext[0])
	y_scale = float(m_height) / (ext[3] - ext[2])
	write(str(x_scale) + ", " + str(y_scale))
	clr(".")
	for [x, y] in data:
		set((x - ext[0]) * x_scale , m_height - ((y - ext[2]) * y_scale ), dot)
	horiz = m_height - (0 - ext[2]) * y_scale
	for x in range(0, m_width):
		set(x, horiz, "=")

########------- END DEFINITIONS, BEGIN EXECUTION -------########

# process execution variables
def getArgv(index: int, default = "unspecified"):
	index += 1 # selects first argument rather than the file
	return sys.argv[index] if len(sys.argv)-1 >= index else default

OS = getArgv(0)
init(OS)
size(int(getArgv(1,m_width)), int(getArgv(2,m_height)))
off([5,2])

i = 0

while True:
	data = []
	for x in range(-200, 200):
		data.append([x/10, 10 * math.asinh(.25 * x/10 + i)])
	quickplot(data)
	draw()
	i += .1
	time.sleep(1)