#! /usr/bin/env python

import sys
import math
import logging

from OpenGL.GL import *
from OpenGL.GLUT import *

# Creating logger for debug output (use -v when invoking script)
logger = logging.getLogger("maman11")
ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
logger.addHandler(ch)

# All below values are [pixels]
INITIAL_WINDOW_WIDTH = 500
INITIAL_WINDOW_HEIGHT = 500
INITIAL_WINDOW_X = 100
INITIAL_WINDOW_Y = 100


""" Objects' coordinates:
The ground and button depend on the window dimensions and requires
	rendering at reshape.
The rest of the objects are independent of the window dimensions,
	their coordinates are calculated once (when this module is loaded).
"""


GROUND_MIN_Y = 0.2

SUN_CENTER_X = -0.5
SUN_CENTER_Y = 0.5
SUN_RADIUS = 0.125
SUN_ANGLES_COUNT = 50  # More angles -> circle would be more accurate
SUN_COORDINATES = []
for i in range(0, SUN_ANGLES_COUNT):
	angle = 2.0 * math.pi * i / SUN_ANGLES_COUNT
	line_x = math.cos(angle) * SUN_RADIUS + SUN_CENTER_X
	line_y = math.sin(angle) * SUN_RADIUS + SUN_CENTER_Y
	SUN_COORDINATES.append((line_x, line_y))

HOUSE_MARGIN = 0.1
HOUSE_LEFT = HOUSE_MARGIN
HOUSE_TOP = -(HOUSE_MARGIN * 2)
HOUSE_RIGHT = 1-HOUSE_MARGIN
HOUSE_MID_X = (HOUSE_LEFT + HOUSE_RIGHT) / 2.0
HOUSE_BUTTOM = GROUND_MIN_Y - 1

ROOF_HEIGHT = 0.2

DOOR_LEFT = HOUSE_MID_X * 1.1
DOOR_TOP = HOUSE_TOP * 2.5
DOOR_RIGHT = HOUSE_RIGHT * 0.8

WINDOW_TOP = (1 + HOUSE_TOP) * 0.8 - 1
WINDOW_LEFT = HOUSE_LEFT * 2.0
WINDOW_RIGHT = HOUSE_MID_X * 0.9
WINDOW_BOTTOM = HOUSE_TOP * 3.5
WINDOW_MID_X = (WINDOW_LEFT + WINDOW_RIGHT) / 2.0
WINDOW_MID_Y = (WINDOW_TOP + WINDOW_BOTTOM) / 2.0

BUTTON_LEFT = 0.6
BUTTON_TOP = GROUND_MIN_Y - 1
BUTTON_RIGHT = 1.0
BUTTON_BOTTOM = -1.0

BUTTON_TEXT_X = BUTTON_LEFT * 1.1
BUTTON_TEXT_Y = BUTTON_TOP * 1.1

TITLE_X = -0.8
TITLE_Y = -0.5

NAME_X = TITLE_X
NAME_Y = TITLE_Y * 1.2


def render_and_draw_string(x: float, y: float, string: str, font):
	logger.debug("render_and_draw_string: x={}, y={}, string={}, font={}".format(
		x, y, string, font))
	glRasterPos2f(x, y)
	for c in string:
		# ord(c) converts character c to type int
		glutBitmapCharacter(font, ord(c))


""" Outer view rendering and drawings """


def render_ground():
	logger.debug("render ground: inner_view.min_len={}".format(inner_view.min_len))
	if glutGet(GLUT_WINDOW_HEIGHT):
		render_ground.y = -(inner_view.min_len * (1-GROUND_MIN_Y) / glutGet(GLUT_WINDOW_HEIGHT))
	else:
		render_ground.y = GROUND_MIN_Y


def draw_ground():
	glColor3f(0.4, 0.2, 0.1)  # Brown
	glRectf(-1.0, render_ground.y, 1.0, -1.0)
	
	
def draw_button():
	glColor3f(1.0, 1.0, 1.0)  # White background
	glRectf(BUTTON_LEFT, BUTTON_TOP, BUTTON_RIGHT, BUTTON_BOTTOM)
	
	glColor3f(0.0, 0.0, 0.0)  # Black border
	glLineWidth(1)
	glBegin(GL_LINE_LOOP)
	glVertex2f(BUTTON_LEFT, BUTTON_TOP)
	glVertex2f(BUTTON_RIGHT, BUTTON_TOP)
	glVertex2f(BUTTON_RIGHT, BUTTON_BOTTOM)
	glVertex2f(BUTTON_LEFT, BUTTON_BOTTOM)
	glEnd()
	
	render_and_draw_string(BUTTON_TEXT_X, BUTTON_TEXT_Y
		, "EXIT", GLUT_BITMAP_8_BY_13)

	
""" Inner view (scene) objects drawings """


def draw_sun():
	glColor3f(1.0, 1.0, 0.0)  # Yellow
	glBegin(GL_POLYGON)
	for line_x, line_y in SUN_COORDINATES:
		glVertex2f(line_x, line_y)
	glEnd()


def draw_wall():
	glColor3f(1.0, 1.0, 1.0)  # White
	glRectf(HOUSE_LEFT, HOUSE_TOP, HOUSE_RIGHT, HOUSE_BUTTOM)


def draw_roof():
	glColor3f(1.1, 0.3, 0.1)  # Red
	glBegin(GL_TRIANGLES)
	glVertex2f(HOUSE_LEFT, HOUSE_TOP)
	glVertex2f(HOUSE_MID_X, ROOF_HEIGHT)
	glVertex2f(HOUSE_RIGHT, HOUSE_TOP)
	glEnd()


def draw_door():
	glColor3f(0.6, 0.4, 0.0)  # Brown
	glRectf(DOOR_LEFT, DOOR_TOP, DOOR_RIGHT, HOUSE_BUTTOM)


def draw_window_outline():
	glBegin(GL_LINE_LOOP)
	glVertex2f(WINDOW_LEFT, WINDOW_TOP)
	glVertex2f(WINDOW_RIGHT, WINDOW_TOP)
	glVertex2f(WINDOW_RIGHT, WINDOW_BOTTOM)
	glVertex2f(WINDOW_LEFT, WINDOW_BOTTOM)
	glEnd()
	
	
def draw_window_inline():
	# vertical line
	glBegin(GL_LINE_STRIP)
	glVertex2f(WINDOW_MID_X, WINDOW_TOP)
	glVertex2f(WINDOW_MID_X, WINDOW_BOTTOM)
	glEnd()
	# horizontal line
	glBegin(GL_LINE_STRIP)
	glVertex2f(WINDOW_LEFT, WINDOW_MID_Y)
	glVertex2f(WINDOW_RIGHT, WINDOW_MID_Y)
	glEnd()


def draw_window():
	glColor3f(0.7, 0.7, 0.7)  # Gray background
	glRectf(WINDOW_LEFT, WINDOW_TOP, WINDOW_RIGHT, WINDOW_BOTTOM)
	glColor3f(0.0, 0.0, 0.0)  # Black border
	glLineWidth(3)
	draw_window_outline()
	draw_window_inline()


def draw_house():
	draw_wall()
	draw_roof()
	draw_door()
	draw_window()


""" Inner view setting used by reshape callback """
	
	
def inner_view(width: int, height: int):
	"""Get the smallest height or width length of the current window
	Set inner Viewport as the biggest cube that fits in the window
	Align the cube to be in the middle of the window
	"""
	logger.debug("inner  view: width={}, height={}".format(width, height))
	if width > height:
		inner_view.min_len = height
		inner_view.start_x = int((width-inner_view.min_len) / 2)
		inner_view.start_y = 0
	else:
		inner_view.min_len = width
		inner_view.start_x = 0
		inner_view.start_y = int((height-inner_view.min_len) / 2)


""" Callbacks """


def mouse(button: int, state: int, x: int, y: int) -> None:
	logger.debug("mouse: button={}, state={}, x={}, y={}".format(button, state, x, y))
	
	x_limit = glutGet(GLUT_WINDOW_WIDTH) * 0.5 * (1.0 + BUTTON_LEFT)
	y_limit = glutGet(GLUT_WINDOW_HEIGHT) * 0.5 * (1.0 - BUTTON_TOP)
	logger.debug("x_limit={}, y_limit={}".format(x_limit, y_limit))
	
	if button == GLUT_RIGHT_BUTTON:
		if x > x_limit and y > y_limit:
			glutDestroyWindow(glutGetWindow())


def reshape(width: int, height: int) -> None:
	logger.debug("reshape: w={}, h={}".format(width, height))
	inner_view(width=width, height=height)
	render_ground()


def display() -> None:
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	
	# Set inner Viewport
	glViewport(inner_view.start_x, inner_view.start_y
		, inner_view.min_len, inner_view.min_len)
	draw_sun()
	draw_house()
	
	# Full window Viewport
	glViewport(0, 0, glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT))
	# Draw ground below inner view so it won't appear "floating in the air"
	draw_ground()
	# Draw button above all other drawings
	draw_button()
	
	# Set full window width and above ground height Viewport
	glViewport(0, inner_view.start_y
		, glutGet(GLUT_WINDOW_WIDTH), int(inner_view.min_len * -render_ground.y))
	# Write title and name on top of the scene
	glColor3f(0.0, 1.0, 0.0)  # Green
	render_and_draw_string(TITLE_X, TITLE_Y
		, "Hello, World!", GLUT_BITMAP_TIMES_ROMAN_24)
	glColor3f(0.4, 0.0, 0.4)  # Purple
	render_and_draw_string(NAME_X, NAME_Y
		, "Sarah Gaidi", GLUT_BITMAP_HELVETICA_18)
	
	glFlush()


""" Initial configuration and main loop """


def main():
	if "-v" in sys.argv:
		# Enable verbosity
		logger.setLevel(logging.DEBUG)

	glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
	glutInitWindowPosition(INITIAL_WINDOW_X, INITIAL_WINDOW_Y)
	glutInitWindowSize(INITIAL_WINDOW_WIDTH, INITIAL_WINDOW_HEIGHT)
	# Override any of the above configuration with the input arguments
	glutInit(sys.argv)
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
