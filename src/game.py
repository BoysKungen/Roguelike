from src import gfx
import curses
import sys, traceback


stdscr = None


class Game(object):
	def __init__(self):
		pass

	def step(self):
		running = True
		x,y = 0,0
		while running:
			curses.curs_set(0)
			c = gfx.scr().getch()
			if c == curses.KEY_UP: 		y -= 1
			elif c == curses.KEY_DOWN: 	y+=1
			elif c == curses.KEY_LEFT: 	x -=1
			elif c == curses.KEY_RIGHT: x +=1
			elif c == ord('q'): running = False



			if c != -1:
				gfx.scr().clear()
				gfx.scr().addch(y,x,"@")
			

	#starts interactive session of the game with the player.
	def play(self):
		gfx.start()
		try: 
			self.step()
		except Exception as err:
			gfx.stop()
			#############################
			print("Error: " + str(err))
			sys.exit(-1)


		gfx.stop()