from src import gfx
from src import world



import curses
import sys, traceback

stdscr = None


class Game(object):
	def __init__(self):
		self.world = world.World()
		self.x,self.y = 0,0

	def step(self, c):
			curses.curs_set(0)
			if c == "up": 		self.world.player_y -= 1
			elif c == "down": 	self.world.player_y +=1
			elif c == "left": 	self.world.player_x -=1
			elif c == "right": 	self.world.player_x +=1

	#starts interactive session of the game with the player.
	def play(self):
		gfx.start()
		try: 
			running = True
			while running:
				c = gfx.get_input()
				self.step(c)
				if c == "q": running = False
				self.world.draw()
		except Exception as err:
			gfx.stop()
			print("Error: " + str(err))
			sys.exit(-1)


		gfx.stop()