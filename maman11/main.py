#! /usr/bin/env python

import sys
import math

from OpenGL.GL import *
from OpenGL.GLUT import *


INITIAL_WINDOW_WIDTH = 500  # [pixels]
INITIAL_WINDOW_HEIGHT = 500  # [pixels]


""" Objects' coordinates:
The ground depends on the window dimensions and requires rendering at reshape.
The rest of the objects are independent of the window dimensions
	and their coordinates are calculated once (when this module is loaded).
"""


MY_SUN_CENTER_X = -0.5
MY_SUN_CENTER_Y = 0.5
MY_SUN_RADIUS = 0.125
MY_SUN_ANGLES_COUNT = 50
MY_SUN_COORDINATES = []
for i in range(0, MY_SUN_ANGLES_COUNT):
	angle = 2.0 * math.pi * i / MY_SUN_ANGLES_COUNT
	line_x = math.cos(angle) * MY_SUN_RADIUS + MY_SUN_CENTER_X
	line_y = math.sin(angle) * MY_SUN_RADIUS + MY_SUN_CENTER_Y
	MY_SUN_COORDINATES.append((line_x, line_y))

MY_HOUSE_MARGIN = 0.1
MY_HOUSE_LEFT = MY_HOUSE_MARGIN
MY_HOUSE_TOP = -(MY_HOUSE_MARGIN * 2)
MY_HOUSE_RIGHT = 1-MY_HOUSE_MARGIN
MY_HOUSE_MID_X = (MY_HOUSE_LEFT + MY_HOUSE_RIGHT) / 2.0

MY_ROOF_HEIGHT = 0.2

MY_DOOR_LEFT = MY_HOUSE_MID_X * 1.1
MY_DOOR_TOP = MY_HOUSE_TOP * 2.5
MY_DOOR_RIGHT = MY_HOUSE_RIGHT * 0.8

MY_WINDOW_TOP = (1 + MY_HOUSE_TOP) * 0.8 - 1
MY_WINDOW_LEFT = MY_HOUSE_LEFT * 2.0
MY_WINDOW_RIGHT = MY_HOUSE_MID_X * 0.9
MY_WINDOW_BOTTOM = MY_HOUSE_TOP * 3.5
MY_WINDOW_MID_X = (MY_WINDOW_LEFT + MY_WINDOW_RIGHT) / 2.0
MY_WINDOW_MID_Y = (MY_WINDOW_TOP + MY_WINDOW_BOTTOM) / 2.0

MY_TITLE_X = -0.7
MY_TITLE_Y = -0.7

MY_NAME_X = MY_TITLE_X
MY_NAME_Y = MY_TITLE_Y * 1.3


def render_ground(height: int):
	print("render ground: height={}".format(inner_view.min_len))
	if glutGet(GLUT_WINDOW_HEIGHT):
		render_ground.y = -(inner_view.min_len / glutGet(GLUT_WINDOW_HEIGHT))
	else:
		render_ground.y = 0


""" Objects drawings """


def draw_ground():
	glColor3f(0.4, 0.2, 0.1)  # Brown
	glRectf(-1.0, render_ground.y, 1.0, -1.0)


def draw_sun():
	glColor3f(1.0, 1.0, 0.0)  # Yellow
	glBegin(GL_POLYGON)
	for line_x, line_y in MY_SUN_COORDINATES:
		glVertex2f(line_x, line_y)
	glEnd()


def draw_wall():
	glColor3f(1.0, 1.0, 1.0)  # White
	glRectf(MY_HOUSE_LEFT, MY_HOUSE_TOP, MY_HOUSE_RIGHT, -1.0)


def draw_roof():
	glColor3f(1.1, 0.3, 0.1)  # Red
	glBegin(GL_TRIANGLES)
	glVertex2f(MY_HOUSE_LEFT, MY_HOUSE_TOP)
	glVertex2f(MY_HOUSE_MID_X, MY_ROOF_HEIGHT)
	glVertex2f(MY_HOUSE_RIGHT, MY_HOUSE_TOP)
	glEnd()


def draw_door():
	glColor3f(0.6, 0.4, 0.0)  # Brown
	glRectf(MY_DOOR_LEFT, MY_DOOR_TOP, MY_DOOR_RIGHT, -1.0)


def draw_window_outline():
	glBegin(GL_LINE_LOOP)
	glVertex2f(MY_WINDOW_LEFT, MY_WINDOW_TOP)
	glVertex2f(MY_WINDOW_RIGHT, MY_WINDOW_TOP)
	glVertex2f(MY_WINDOW_RIGHT, MY_WINDOW_BOTTOM)
	glVertex2f(MY_WINDOW_LEFT, MY_WINDOW_BOTTOM)
	glEnd()
	
	
def draw_window_inline():
	# vertical line
	glBegin(GL_LINE_STRIP)
	glVertex2f(MY_WINDOW_MID_X, MY_WINDOW_TOP)
	glVertex2f(MY_WINDOW_MID_X, MY_WINDOW_BOTTOM)
	glEnd()
	# horixontal line
	glBegin(GL_LINE_STRIP)
	glVertex2f(MY_WINDOW_LEFT, MY_WINDOW_MID_Y)
	glVertex2f(MY_WINDOW_RIGHT, MY_WINDOW_MID_Y)
	glEnd()


def draw_window():
	glColor3f(0.7, 0.7, 0.7)  # Gray background
	glRectf(MY_WINDOW_LEFT, MY_WINDOW_TOP, MY_WINDOW_RIGHT, MY_WINDOW_BOTTOM)
	glColor3f(0.0, 0.0, 0.0)  # Black border
	glLineWidth(3)
	draw_window_outline()
	draw_window_inline()


def draw_house():
	draw_wall()
	draw_roof()
	draw_door()
	draw_window()
	error_check()


""" utililtes """


def error_check():
	code = glGetError()
	if code != GL_NO_ERROR:
		print("OpenGL error: {}".format(gluErrorString(code)))
	return code


def inner_view(width: int, height: int):
	"""Get the smallest height or width length of the current window
	Set inner Viewport as the biggest cube that fits in the window
	Align the cube to be in the middle of th window
	"""
	print("inner  view")
	if width > height:
		inner_view.min_len = height
		inner_view.start_x = int((width-inner_view.min_len) / 2)
		inner_view.start_y = 0
	else:
		inner_view.min_len = width
		inner_view.start_x = 0
		inner_view.start_y = int((height-inner_view.min_len) / 2)


def render_and_draw_string(x: float, y: float, string: str, font):
	
	glRasterPos2f(x, y)
	for c in string:
		# ord(c) converts character c to type int
		glutBitmapCharacter(font, ord(c))


""" main callback functions """


def reshape(width: int, height: int):
	print("reshape: w={}, h={}".format(width, height))
	inner_view(width=width, height=height)
	render_ground(height=height)
	error_check()


def display():
	print("display")
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	# Full window Viewport
	glViewport(0, 0, glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT))
	# Draw ground below inner view so it won't appear "floating in the air"
	draw_ground()
	
	# Set inner Viewport
	glViewport(inner_view.start_x, inner_view.start_y
		, inner_view.min_len, inner_view.min_len)
	draw_sun()
	draw_house()
	
	# Back to full window Viewport
	glViewport(0, 0, glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT))
	# Write title and name on top of the scene
	glColor3f(0.0, 1.0, 0.0)  # Green
	render_and_draw_string(MY_TITLE_X, MY_TITLE_Y
		, "Hello, World!", GLUT_BITMAP_TIMES_ROMAN_24)
	glColor3f(0.4, 0.0, 0.4)  # Purple
	render_and_draw_string(MY_NAME_X, MY_NAME_Y
		, "Sarah Gaidi", GLUT_BITMAP_HELVETICA_18)
	
	glFlush()
	error_check()
				
								
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
	glutInitWindowPosition(100, 100)
	glutInitWindowSize(INITIAL_WINDOW_WIDTH, INITIAL_WINDOW_HEIGHT)
	# Window title is the file name
	glutCreateWindow(__file__)
	
	glutDisplayFunc(display)
	glutReshapeFunc(reshape)

	glMatrixMode(GL_PROJECTION)
	# Set bright-blue sky as background
	glClearColor(0.8, 0.9, 1.0, 0.0)
	
	glutMainLoop()
	error_check()		


if __name__ == '__main__': main()
