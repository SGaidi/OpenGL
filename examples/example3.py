#! /usr/bin/env python

import sys
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

name = 'PowerPoint Example 1 - 2D Line'


def display():
	glClear(GL_COLOR_BUFFER_BIT)
	
	# Set color to red
	glColor3f(1.0, 0.0, 0.0)
	# Draw line
	glBegin(GL_LINES)
	# First point
	glVertex2i(180, 15)
	# Second point
	glVertex2i(10, 145)
	# Ready with line
	glEnd()
	
	glFlush()


def main():
	glutInit(sys.argv)
	glutCreateWindow(name)
	
	glClearColor(1.0, 1.0, 1.0, 0.0)
	# Set transformation
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0, 200, 0, 150)
	
	glutDisplayFunc(display)
	glutMainLoop()
	

if __name__ == '__main__': main()