#! /usr/bin/env python

import sys
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

name = "Section 3-5 in Book"


def error_check():
	code = glGetError()
	if code != GL_NO_ERROR:
		error_str = gluErrorString(code)
		print("OpenGL error: {}".format(error_str))
	return code
	

def init():
	glClearColor(1.0, 1.0, 1.0, 0.0)
	glMatrixMode(GL_PROJECTION)
	gluOrtho2D(0.0, 200.0, 0.0, 150.0)
	error_check()


def display():
	glClear(GL_COLOR_BUFFER_BIT)
	
	glColor3f(0.0, 0.4, 0.2)
	glBegin(GL_LINES)
	glVertex2i(180, 15)
	glVertex2i(10, 145)
	glEnd()
	
	glFlush()
	error_check()


def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowPosition(50, 100)
	glutInitWindowSize(400, 300)
	glutCreateWindow(name)
	
	init()
	glutDisplayFunc(display)
	error_check()
	glutMainLoop()

if __name__ == '__main__': main()