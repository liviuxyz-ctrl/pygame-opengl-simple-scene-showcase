from OpenGL.GL import *


def draw_array(vertices, color, scale, offset):
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, vertices, GL_STATIC_DRAW)

    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

    glColor4fv(color)  # Set the color for all vertices

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glTranslatef(offset[0], offset[1], offset[2])  # Apply translation transformation
    glScalef(scale, scale, scale)  # Apply scaling transformation

    glDrawArrays(GL_QUADS, 0, int(len(vertices) / 3))

    glPopMatrix()

    glDisableVertexAttribArray(0)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glDeleteBuffers(1, [vbo])

    glBindVertexArray(0)
    glDeleteVertexArrays(1, [vao])
