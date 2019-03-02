#!/usr/bin/env python

import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def display():
    # Background color
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    # Draw line
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex2i(1, 1)
    glVertex2i(-1, -1)
    glEnd()
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitWindowSize(150, 250)
    glutCreateWindow(__file__)
    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == '__main__': main()