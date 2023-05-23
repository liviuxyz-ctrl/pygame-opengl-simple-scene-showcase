from vedo import load
from OpenGL.GL import *

from src.flags.render import enable_efficient_draw
from src.utils.efficient_draw import draw_array


def _load_rock_model():
    obj = load("/home/decemyn/PycharmProjects/gui-project/src/models/RockPackByPava.obj")
    return obj.points()


def render_rock():
    rock_model_points = _load_rock_model()

    # Apply scaling factor
    scale_factor = 5.0  # Modify this value to adjust the scale

    # Apply coordinate offset
    offset = [0.0, 3.0, 0.0]  # Modify this value to adjust the offset

    # Color data
    color = (1, 1, 0, 0)

    if not enable_efficient_draw:
        # Draw the vedo object using OpenGL commands
        glBegin(GL_TRIANGLES)
        for vertex in rock_model_points:
            glColor4fv(color)
            scaled_vertex = [coord * scale_factor + offset[i] for i, coord in enumerate(vertex)]
            glVertex3fv(scaled_vertex)
        glEnd()
    else:
        draw_array(rock_model_points, color, scale_factor, offset)
