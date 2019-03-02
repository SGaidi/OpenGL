#! /usr/bin/env python

import sys
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

name = 'PowerPoint Example 1 - 3D Boxes'


def display():
	glClear(GL_COLOR_BUFFER_BIT)
	
	# Set color to black
	glColor3f(0.0, 0.0, 0.0)
	# Draw two rectangular boxes
	# Unit box around origin
	glutWireCube(1.0)
	# Move in x-direction
	glTranslatef(2.0, 0.0, 0.0)
	# Rotate 30 degress around z-axis
	glRotate(30, 0.0, 0.0, 1.0)
	# Scale in z-direction
	glScalef(1.0, 1.0, 2.0)
	# Translated, rotated, scaled box
	glutWireCube(1.0)
	
	glFlush()


def main():
	glutInit(sys.argv)
	glutCreateWindow(name)
	
	glClearColor(1.0, 1.0, 1.0, 0.0)
	# Select part of window
	glViewport(0, 0, 500, 500)
	# Set projection
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glFrustum(-1.0, 1.0, -1.0, 1.0, 4.0, 20.0)
	# Set camera
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(3.0, 6.0, 5.0 # Eye point
		, 1.0, 0.0, 0.0 # Center point
		, 0.0, 0.0, 1.0 # Up axis
		)

	glutDisplayFunc(display)
	glutMainLoop()
	

if __name__ == '__main__': main()