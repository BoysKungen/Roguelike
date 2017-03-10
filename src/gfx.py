import curses
import platform
import os
screen = None

keymap ={curses.KEY_BACKSPACE: "backspace",
          curses.KEY_UP:        "up",
          curses.KEY_DOWN:      "down",
          curses.KEY_LEFT:      "left",
          curses.KEY_RIGHT:     "right",
          curses.KEY_ENTER:     "enter",
          curses.KEY_END:       "end",
          curses.KEY_HOME:      "home",
          curses.KEY_F0:        "f0",
          curses.KEY_F1:        "f1",
          curses.KEY_F2:        "f2",
          curses.KEY_F3:        "f3",
          curses.KEY_F4:        "f4",
          curses.KEY_F5:        "f5",
          curses.KEY_F6:        "f6",
          curses.KEY_F7:        "f7",
          curses.KEY_F8:        "f8",
          curses.KEY_F9:        "f9",
          curses.KEY_F10:       "f10",
          curses.KEY_F11:       "f11",
          curses.KEY_F12:       "f12",
          curses.KEY_F13:       "f13",
          curses.KEY_F14:       "f14",
          curses.KEY_F15:       "f15",
          curses.KEY_RESIZE:    "resize",
          curses.KEY_PPAGE:     "page_up",
          curses.KEY_NPAGE:     "page_down",
          -1:                   None}



#Starts up Curses
def start():
	global screen
	screen = curses.initscr()
	curses.noecho()
	curses.cbreak()
	curses.nonl()
	curses.curs_set(0)
	screen.keypad(1)
	screen.timeout(0)
	screen.scrollok(False)

def stop():
	global screen
	curses.nocbreak()
	screen.timeout(-1)
	screen.keypad(0)
	curses.curs_set(1)
	curses.echo()
	curses.endwin()
	screen = None
	if platform.system() == "Windows":
		os.system("cls")
	elif platform.system() == "Linux":
		os.system("clear")


def get_input():
	global screen, keymap
	if screen:
		c = screen.getch()
		if c > 0 and c < 256: return chr(c)
		elif c in keymap: return keymap[c]
	return None

def scr():
	global screen
	return screen

def draw(x, y, char : str):
		if screen:
			h,w = screen.getmaxyx()
		if x>= 0 and x < w and y >= 0 and y < h and (x,y)!=(w-1,h-1):
			screen.addch(y,x,char)

def clear():
	return screen.clear()
