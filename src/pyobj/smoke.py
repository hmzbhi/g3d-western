# Python built-in modules
import os                           # os function, i.e. checking file status
from itertools import cycle         # allows easy circular choice list
import atexit                       # launch a function at exit

# External, non built-in modules
import OpenGL.GL as GL              # standard Python OpenGL wrapper
import glfw                         # lean window system wrapper for OpenGL
import numpy as np                  # all matrix manipulations & OpenGL args
import assimpcy                     # 3D resource loader

from tools.core import Node, Shader, Mesh, load
from tools.transform import translate, rotate, scale, identity, vec
from math import sin

# ------------------------ Smoke Particule class ------------------------

class Smoke(Mesh):
    """ Smoke Particule set """
    def __init__(self, shader):
        GL.glPointSize(2)
        self.count = 0
        self.translate = 0.5

        x_start, x_step = 95, 5
        x_stop = x_start + 6

        y_start, y_step = -690, 5
        y_stop = y_start + 100
        
        z_start, z_step = 446, 5
        z_stop = z_start + 6

        x_values = np.arange(x_start, x_stop + x_step, x_step)
        y_values = np.arange(y_start, y_stop + y_step, y_step)
        z_values = np.arange(z_start, z_stop + z_step, z_step)

        xx, yy, zz = np.meshgrid(x_values, y_values, z_values)
        px, py, pz = xx.flatten(), yy.flatten(), zz.flatten()
        points = np.column_stack((px, py, pz))
        
        self.coords = points
        self.primitive_type = GL.GL_POINTS

        super().__init__(shader, attributes=dict(position=self.coords),usage=GL.GL_STREAM_DRAW, global_color=(1, 0.65, 0), primitive_type=GL.GL_POINTS)
    
    def draw(self, primitives=GL.GL_POINTS, attributes=None, **uniforms):

        self.transform = translate(1,0,100)
        dp = [[0,5*sin(i + glfw.get_time()), 0] for i in range(len(self.coords))]

        coords = np.array(self.coords, 'f') + np.array(dp, 'f')
        super().draw(primitives, attributes=dict(position=coords), **uniforms)

