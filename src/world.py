from src import gfx
from src import log

def adjacent(x,y,r):
	adj = []
	odd = True if y % 2 == 1 else False

	x += r
	adj.append((x,y))
	for i in range(r):
		if not odd: x -= 1
		y -= 1
		adj.append((x,y))
		odd = not odd
	for i in range(r):
		x -= 1
		adj.append((x,y))
	for i in range(r):
		if not odd: x -= 1
		y += 1
		adj.append((x,y))
		odd = not odd
	for i in range(r):
		if odd: x += 1
		y += 1
		adj.append((x,y))
		odd = not odd
	for i in range(r):
		x += 1
		adj.append((x,y))
	for i in range(r):
		if odd: x += 1
		y -= 1
		adj.append((x,y))
		odd = not odd
	
	return adj

	#log.log("Adjacent tile calculation: x: %d, y: %d"%(x,y))
	#log.log("Adjacent = [%s]"%(str(adjacent)))

def view(x,y,rad):
	distance = []


	return disctance 
class World(object):
	def __init__(self):
		self.w = 20
		self.h = 20
		self.player_x = 4
		self.player_y = 4


	def draw(self):
		gfx.clear()
		#log.log("DRAWING")
		adjacent_tiles = adjacent(self.player_x, self.player_y, 2)
		for y in range(self.h):
			odd = True if y % 2 == 1 else False
			for x in range(self.w):
				dx = x*2 + (1 if odd else 0)
				if (self.player_x, self.player_y) == (x,y):
					gfx.draw(dx,y,'@') 
				elif (x,y) in adjacent_tiles:
					gfx.draw(dx,y,'.')
		#log.log("DONE DRAWING\n\n")

