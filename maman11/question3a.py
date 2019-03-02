#!/usr/bin/env python

import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def display():
    # do nothing
    pass


def main():
    glutInit(sys.argv)
    # ccordinates calculated by:
    # x = 200-100 = 100
    # y = 200-75 = 125
    glutInitWindowPosition(100, 125)
    glutInitWindowSize(100, 75)
    glutCreateWindow(__file__)
    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == '__main__': main()
