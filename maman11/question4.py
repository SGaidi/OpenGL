#! /usr/bin/env python

import sys
import math

from OpenGL.GL import *
from OpenGL.GLUT import *


MY_HOUSE_TOP = -0.2
MY_HOUSE_LEFT = -0.8
MY_HOUSE_RIGHT = -0.2
MY_HOUSE_MID_X = (MY_HOUSE_LEFT + MY_HOUSE_RIGHT) / 2.0

MY_WINDOW_TOP = (1 + MY_HOUSE_TOP) * 0.8 - 1
MY_WINDOW_LEFT = MY_HOUSE_LEFT * 0.9
MY_WINDOW_RIGHT = MY_HOUSE_MID_X * 1.1
MY_WINDOW_BOTTOM = MY_HOUSE_TOP * 3.5
MY_WINDOW_MID_X = (MY_WINDOW_LEFT + MY_WINDOW_RIGHT) / 2.0
MY_WINDOW_MID_Y = (MY_WINDOW_TOP + MY_WINDOW_BOTTOM) / 2.0

CIRCLE_SMOOTHNESS = 50

CIRCLE_OUTLINE = []
for i in range(0, CIRCLE_SMOOTHNESS):
	angle = 2.0 * math.pi * i / CIRCLE_SMOOTHNESS
	x = math.cos(angle) * 0.1 + 0.5
	y = math.sin(angle) * 0.1 + 0.5
	CIRCLE_OUTLINE.append((x, y))


def error_check():
	code = glGetError()
	if code != GL_NO_ERROR:
		print("OpenGL error: {}".format(gluErrorString(code)))
	return code


def display():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	
	# White-colored house
	glColor3f(1.0, 1.0, 1.0);
	glRectf(MY_HOUSE_LEFT, MY_HOUSE_TOP
		, MY_HOUSE_RIGHT, -1.0)
		
	# Red roof on top of the house
	glColor3f(1.1, 0.3, 0.1);
	glBegin(GL_TRIANGLES);
	glVertex2f(MY_HOUSE_LEFT, MY_HOUSE_TOP)
	glVertex2f(MY_HOUSE_MID_X, 0.2)
	glVertex2f(MY_HOUSE_RIGHT, MY_HOUSE_TOP)
	glEnd()
	
	# Brown door in house
	glColor3f(0.6, 0.4, 0.0)
	glRectf(MY_HOUSE_MID_X * 0.9, MY_HOUSE_TOP * 2.5
		, MY_HOUSE_RIGHT * 1.5, -1.0)
		
	# Window gray background
	glColor3f(0.7, 0.7, 0.7)
	glRectf(MY_WINDOW_LEFT, MY_WINDOW_TOP
		, MY_WINDOW_RIGHT, MY_WINDOW_BOTTOM)
		
	# Black window
	glColor3f(0.0, 0.0, 0.0)
	glLineWidth(3)
	
	# Window outline
	glBegin(GL_LINE_LOOP)
	glVertex2f(MY_WINDOW_LEFT, MY_WINDOW_TOP)
	glVertex2f(MY_WINDOW_RIGHT, MY_WINDOW_TOP)
	glVertex2f(MY_WINDOW_RIGHT, MY_WINDOW_BOTTOM)
	glVertex2f(MY_WINDOW_LEFT, MY_WINDOW_BOTTOM)
	glEnd()
	
	# Window inline
	glBegin(GL_LINE_STRIP)
	glVertex2f(MY_WINDOW_MID_X, MY_WINDOW_TOP)
	glVertex2f(MY_WINDOW_MID_X, MY_WINDOW_BOTTOM)
	glEnd()
	glBegin(GL_LINE_STRIP)
	glVertex2f(MY_WINDOW_LEFT, MY_WINDOW_MID_Y)
	glVertex2f(MY_WINDOW_RIGHT, MY_WINDOW_MID_Y)
	glEnd()
	
	# Yellow sun
	glColor3f(1.0, 1.0, 0.0)
	glBegin(GL_POLYGON)
	for x, y in CIRCLE_OUTLINE:
		glVertex2f(x, y)
	glEnd()
	
	glFlush()
	
	
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
	glutInitWindowPosition(100, 100)
	glutInitWindowSize(500, 500)
	# Window title is the file name
	glutCreateWindow(__file__)
	
	# Set bright-blue sky as background
	glClearColor(0.8, 0.9, 1.0, 0.0)
	glMatrixMode(GL_PROJECTION)
	glutDisplayFunc(display)
	glutMainLoop()
	

if __name__ == '__main__': main()