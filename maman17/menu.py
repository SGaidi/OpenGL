#! /usr/bin/env python
import sys
import logging

from OpenGL.GL import *
from OpenGL.GLUT import *

from buttons_click_callbacks import ambient_light, help, quit


# Creating logger for debug output (use -v when invoking main.py script)
logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
logger.addHandler(ch)


# TODO: maybe make parent class of Rect with (left, top, right, bottom, color) attributes
# then make Button and menu the children of Rect?


class Button:

	def __init__(self, name: str, click_callback, left: int, top: int, right: int, bottom: int):
		logger.warning("Button.__init__(name={}, click_callback={}, left={}, top={}, right={}, bottom={})".format(
			name, click_callback, left, top, right, bottom))
		self.name = name
		self.click_callback = click_callback
		self.left = left
		self.top = top
		self.right = right
		self.bottom = bottom
		
	def draw(self):
		logger.warning("Button.draw(left={}, top={}, right={}, bottom={})".format(self.left, self.top, self.right, self.bottom))
		
		#glViewport(self.left, self.top, self.right, self.bottom)
		glViewport(0, 0, 100, 100)
		glColor3f(0.690, 0.878, 0.902)  # Powder-Blue
		glRectf(-1.0, 1.0, 1.0, -1.0)
		
		glColor3f(0.0, 0.0, 0.0)  # Black text
		glRasterPos2f(self.left + 5, self.top + 5)
		for c in self.name:
			# ord(c) converts character c to type int
			glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(c))

	
class Menu:

	BUTTONS_MARGIN = 40  # pixels
	BUTTONS_HEIGHT = 50  # pixels

	def __init__(self, left: int, top: int, right: int, bottom: int):
		logger.warning("Menu.__init__(left={}, top={}, right={}, bottom={})".format(left, top, right, bottom))
		self.left = left
		self.top = top
		self.right = right
		self.bottom = bottom
		
		buttons_left = left + Menu.BUTTONS_MARGIN
		buttons_top = top + Menu.BUTTONS_MARGIN
		buttons_right = right - Menu.BUTTONS_MARGIN
		buttons_bottom = buttons_top + Menu.BUTTONS_HEIGHT
		buttons_space =  + Menu.BUTTONS_HEIGHT + Menu.BUTTONS_MARGIN
		self.buttons = [ Button("adjust ambient light", ambient_light.call, buttons_left, buttons_top, buttons_right, buttons_bottom),
			#Button("help", help.call, buttons_left, buttons_top + buttons_space, buttons_right, buttons_bottom + buttons_space),
			#Button("wuit", quit.call, buttons_left, buttons_top + buttons_space * 2, buttons_right, buttons_bottom + buttons_space * 2)
			]
		
	def draw_buttons(self):
		logger.debug("Menu.draw_buttons")
		for button in self.buttons:
			button.draw()
		
	def draw_background(self):
		logger.debug("Menu.draw_background")
		glViewport(self.left, self.top, self.right, self.bottom)
		glColor3f(0.663, 0.663, 0.663)  # Gray
		glRectf(-1.0, 1.0, 1.0, -1.0)
		
	def draw(self):
		logger.debug("Menu.draw")
		self.draw_background()
		self.draw_buttons()
