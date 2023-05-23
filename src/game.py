import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from src.objects.game_plane import draw_plane
from src.objects.pseudo_tree import render_tree_model
from src.objects.pseudo_rock import render_rock

# Window dimensions
WIDTH = 800
HEIGHT = 600

# Initialize Pygame and OpenGL
pygame.init()
pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)

# Set up the 3D perspective
glViewport(0, 0, WIDTH, HEIGHT)
glMatrixMode(GL_PROJECTION)
gluPerspective(45, (WIDTH / HEIGHT), 0.1, 50.0)

# Position the camera
camera_distance = 25.0
camera_rotation = [0, 0]
glMatrixMode(GL_MODELVIEW)
gluLookAt(0, -camera_distance, 0, 0, 0, 0, 0, 0, 1)

# OpenGL Flags

glLightfv(GL_LIGHT0, GL_POSITION, (-40, 200, 100, 0.0))
glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
glEnable(GL_LIGHT0)
glEnable(GL_LIGHTING)
glEnable(GL_COLOR_MATERIAL)
glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LESS)
glShadeModel(GL_SMOOTH)

# Enable texture mapping
glEnable(GL_TEXTURE_2D)
glClearColor(0.0, 0.0, 0.0, 0.0)
glClearDepth(1.0)


# Function for handling events
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEMOTION:
            x, y = event.rel
            camera_rotation[0] += y
            camera_rotation[1] += x


# Main rendering and event loop
while True:
    handle_events()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Apply camera transformations
    glTranslatef(0.0, 0.0, -camera_distance)
    glRotatef(camera_rotation[0], 1.0, 0.0, 0.0)
    glRotatef(camera_rotation[1], 0.0, 1.0, 0.0)

    draw_plane(20.0)
    render_tree_model()
    render_rock()

    pygame.display.flip()
    pygame.time.wait(10)
