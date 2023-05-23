from vedo import load
from OpenGL.GL import *

from src.flags.render import enable_efficient_draw
from src.utils.efficient_draw import draw_array


def _load_tree_model():
    obj = load("/home/decemyn/PycharmProjects/gui-project/src/models/Lowpoly_tree_sample.obj")
    return obj.points()


def render_tree_model():
    tree_model_points = _load_tree_model()

    # Apply scaling factor
    scale_factor = 0.2  # Modify this value to adjust the scale

    # Apply coordinate offset
    offset = [5.0, 0.0, 3.0]  # Modify this value to adjust the offset

    # Color data
    color = (0, 1, 0, 0)

    if not enable_efficient_draw:
        # Draw the vedo object using OpenGL commands
        glBegin(GL_QUADS)
        for vertex in tree_model_points:
            glColor4fv(color)
            scaled_vertex = [coord * scale_factor + offset[i] for i, coord in enumerate(vertex)]
            glVertex3fv(scaled_vertex)
        glEnd()
    else:
        draw_array(tree_model_points, color, scale_factor, offset)
