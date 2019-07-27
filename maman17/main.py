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
MENU_WIDTH, MENU_HEIGHT = 300, WINDOW_HEIGHT
MENU_LEFT = WINDOW_WIDTH - MENU_WIDTH

"""components of display"""


menu = Menu(MENU_LEFT, 0, MENU_WIDTH, MENU_HEIGHT)


"""callbacks"""


def mouse(button: int, state: int, x: int, y: int) -> None:
	logger.debug("mouse: button={}, state={}, x={}, y={}".format(button, state, x, y))


def reshape(width: int, height: int) -> None:
	"""Ignore input and make window size static"""
	logger.debug("reshape: w={}, h={}".format(width, height))
	glutReshapeWindow(WINDOW_WIDTH, WINDOW_HEIGHT)

"""
def draw_button(left: int = BUTTONS_LEFT, top: int = BUTTONS_TOP, right: int = BUTTONS_RIGHT, bottom: int = BUTTONS_BOTTOM, counter: int = 0):
	glColor3f(0.690, 0.769, 0.871)  # LightSteel
	top += BUTTONS_HEIGHT * counter
	bottom += BUTTONS_HEIGHT * counter
	glViewport(BUTTONS_LEFT, BUTTONS_TOP, BUTTONS_RIGHT, BUTTONS_BOTTOM)
	glRectf(-1.0, 1.0, 1.0, -1.0)
	
	glColor3f(0.0, 0.0, 0.0)  # Black border
	glLineWidth(1)
	glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
	glRectf(-1.0, 1.0, 1.0, -1.0)
	glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
	
	return
	glBegin(GL_LINE_LOOP)
	glVertex2f(left, top)
	glVertex2f(right, top)
	glVertex2f(right, bottom)
	glVertex2f(left, bottom)
	glEnd()
	
	render_and_draw_string(BUTTON_TEXT_X, BUTTON_TEXT_Y
		, "EXIT", GLUT_BITMAP_8_BY_13)
"""

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
