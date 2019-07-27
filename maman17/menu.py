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


# TODO: maybe make parent class of Rect with (x, height, width, y, color) attributes
# then make Button and menu the children of Rect?


class Button:

	def __init__(self, name: str, click_callback, x: int, y: int, width: int, height: int):
		logger.warning("Button.__init__(name={}, click_callback={}, x={}, y={}, width={}, height={})".format(
			name, click_callback, x, height, width, y))
		self.name = name
		self.click_callback = click_callback
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		# align text positions to middle of width and height
		# 8 and 13 are because of GLUT_BITMAP_8_BY_13
		self.text_x, self.text_y = -8*len(self.name)/(self.width), -13/self.height
		
	def draw_background(self):
		glColor3f(0.251, 0.878, 0.816)  # Turquoise
		glRectf(-1.0, 1.0, 1.0, -1.0)
	
	def draw_border(self):
		glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
		glColor3f(0.0, 0.0, 0.0)  # Black
		glRectf(-1.0, 1.0, 1.0, -1.0)
		glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
		
	def draw_text(self):
		glColor3f(0.0, 0.0, 0.0)  # Black
		glRasterPos2f(self.text_x, self.text_y)
		for c in self.name:
			# ord(c) converts character c to type int
			glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(c))
		
	def draw(self):
		glViewport(self.x, self.y, self.width, self.height)
		self.draw_background()
		self.draw_border()
		self.draw_text()


class Menu:

	MARGIN = 40  # pixels
	BUTTON_HEIGHT = 30  # pixels
	
	def add_buttons(self):
		buttons_x = self.x + Menu.MARGIN
		buttons_y = self.height - Menu.MARGIN - Menu.BUTTON_HEIGHT
		buttons_width = self.width - 2 * Menu.MARGIN
		buttons_space = Menu.BUTTON_HEIGHT + Menu.MARGIN
		self.buttons = [ Button("adjust ambient light", ambient_light.call, buttons_x, buttons_y, buttons_width, Menu.BUTTON_HEIGHT),
			Button("help", help.call, buttons_x, buttons_y - buttons_space, buttons_width, Menu.BUTTON_HEIGHT),
			Button("quit", quit.call, buttons_x, buttons_y - buttons_space * 2, buttons_width, Menu.BUTTON_HEIGHT)
			]

	def __init__(self, x: int, y: int, width: int, height: int):
		logger.warning("Menu.__init__(x={}, y={}, width={}, height={})".format(x, y, width, height))
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.add_buttons()
		
	def draw_background(self):
		glViewport(self.x, self.y, self.width, self.height)
		glColor3f(0.663, 0.663, 0.663)  # Gray
		glRectf(-1.0, 1.0, 1.0, -1.0)
		
	def draw_buttons(self):
		for button in self.buttons:
			button.draw()
		
	def draw(self):
		self.draw_background()
		self.draw_buttons()
