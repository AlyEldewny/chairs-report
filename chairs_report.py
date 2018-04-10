
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from numpy import *


def init():
    glMatrixMode(GL_PROJECTION)
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    gluPerspective(60, 1, 0.1, 50)
    gluLookAt(10, 10, 10, 0, 0, 0, 0, 1, 0)


def draw_chair():
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(1, 1,1)
    glTranslate(-4.6, 0, 0)
    glScale(2, 2, .2)
    glutSolidCube(2)
    glPopAttrib()
    glPopMatrix()
    ################################
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0, 0, 1)
    glTranslate(-4.5, -2, 2)
    glScale(2, .5, 2)
    glutSolidCube(2)
    glPopAttrib()
    glPopMatrix()
    ##################################
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0, 0, 1)
    glTranslate(-6, -4, 0)
    glScale(.5, 4, .5)
    glutSolidCube(1)
    glPopAttrib()
    glPopMatrix()
    ############################
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0, 0, 1)
    glTranslate(-6, -4, 3.5)
    glScale(.5, 4, .5)
    glutSolidCube(1)
    glPopAttrib()
    glPopMatrix()
    ######################
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0, 0, 1)
    glTranslate(-2.5, -4, .5)
    glScale(.5, 4, .5)
    glutSolidCube(1)
    glPopAttrib()
    glPopMatrix()
    ####################
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0, 0, 1)
    glTranslate(-2.5, -4, 3.5)
    glScale(.5, 4, .5)
    glutSolidCube(1)
    glPopAttrib()
    glPopMatrix()


def draw_cube():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)
    draw_chair()
    glTranslate(6, 0, 0)
    draw_chair()
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"chairs_report")
glutDisplayFunc(draw_cube)
glutIdleFunc(draw_cube)
init()
glutMainLoop()
