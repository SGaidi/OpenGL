#! /usr/bin/env python
import sys
import logging

from OpenGL.GL import *
from OpenGL.GLUT import *

from menu import Menu


# Creating logger for debug output (use -v when invoking script)
logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
logger.addHandler(ch)


"""constants"""


WINDOW_WIDTH, WINDOW_HEIGHT = 1100, 500
MENU_WIDTH, MENU_HEIGHT = 250, WINDOW_HEIGHT
MENU_LEFT = WINDOW_WIDTH - MENU_WIDTH


"""components of display"""


menu = Menu(MENU_LEFT, 0, MENU_WIDTH, MENU_HEIGHT)


"""callbacks"""


def mouse(button: int, state: int, x: int, y: int) -> None:
	logger.debug("mouse: button={}, state={}, x={}, y={}".format(button, state, x, y))
	if state == 1:
		comp_x, comp_y = x, WINDOW_HEIGHT - y
		for button in menu.buttons:
			if button.is_clicked(comp_x, comp_y):
				button.click_callback()
				break


def reshape(width: int, height: int) -> None:
	"""Ignore input and make window size static"""
	logger.debug("reshape: w={}, h={}".format(width, height))
	glutReshapeWindow(WINDOW_WIDTH, WINDOW_HEIGHT)


def display() -> None:
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
	
	menu.draw()

	glFlush()


""" Initial configuration and main loop """


def main():
	if "-v" in sys.argv:
		# Enable verbosity
		logger.setLevel(logging.DEBUG)
		from menu import logger as menu_logger
		menu_logger.setLevel(logging.DEBUG)
	glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
	glutInitWindowPosition(100, 100)
	glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
	glutInit()
	# Window title is the file name
	glutCreateWindow(__file__)
	
	# Callbacks
	glutMouseFunc(mouse)
	glutReshapeFunc(reshape)
	glutDisplayFunc(display)

	glMatrixMode(GL_PROJECTION)
	# Set bright-blue sky as background
	glClearColor(0.8, 0.9, 1.0, 0.0)
	
	glutMainLoop()	


if __name__ == '__main__': main()
