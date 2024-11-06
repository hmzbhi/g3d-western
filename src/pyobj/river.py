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

# -------------- River class ---------------------------------

class River(Mesh):

    def __init__(self, shader):
        self.position = 1000 * np.array(((-1.03, -.9, -1), (.97, -.9, -1), (.97, -.9, 0), (-1.03, -.9, 0)), 'f')
        self.color = (0, 0.5, 1)
        self.opacity = 0.5
        index = np.array((0, 2, 1, 0, 3, 2), np.uint32)

        self.translate = 0.5
        self.count = 0

        super().__init__(shader, attributes=dict(position=self.position), index=index,usage=GL.GL_STREAM_DRAW, primitive_type=GL.GL_TRIANGLES)

    def draw(self, primitives=GL.GL_TRIANGLES, **uniforms):
        GL.glEnable(GL.GL_BLEND)
        GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA)
        self.count+=self.translate
        if self.count > 10:
            self.translate = -self.translate
        elif self.count < -30:
            self.translate = -self.translate
        self.position = 1000 * np.array(((-1.03, -.9 +self.count/1000, -1), (.97, -.9 + self.count/1000, -1), (.97, -.9 + self.count/1000, 0), (-1.03, -.9 + self.count/1000, 0)), 'f')

        super().draw(primitives=primitives, attributes=dict(position=self.position), global_color=self.color, alpha=self.opacity, **uniforms)
        GL.glDisable(GL.GL_BLEND)
