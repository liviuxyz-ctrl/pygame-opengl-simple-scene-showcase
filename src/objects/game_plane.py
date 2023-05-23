import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def init(width, height):
    pygame.init()
    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)

    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (width / height), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)


def _load_texture(file_path):
    texture_surface = pygame.image.load(file_path)
    texture_data = pygame.image.tostring(texture_surface, "RGB", 1)

    width = texture_surface.get_width()
    height = texture_surface.get_height()

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)

    return texture_id


def draw_plane(scale):
    texture_id = _load_texture("/home/decemyn/PycharmProjects/gui-project/src/models/grass-min.jpg")

    glBindTexture(GL_TEXTURE_2D, texture_id)

    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0 * scale, 0.0, -1.0 * scale)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0 * scale, 0.0, -1.0 * scale)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0 * scale, 0.0, 1.0 * scale)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0 * scale, 0.0, 1.0 * scale)
    glEnd()
