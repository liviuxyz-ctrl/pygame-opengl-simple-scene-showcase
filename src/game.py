import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

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
camera_distance = 10.0
camera_rotation = [0, 0]
glMatrixMode(GL_MODELVIEW)
gluLookAt(0, -camera_distance, 0, 0, 0, 0, 0, 0, 1)


# Function for drawing objects
def draw_objects():
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-1.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    glEnd()


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

    draw_objects()

    pygame.display.flip()
    pygame.time.wait(10)
