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
# ------------------------ Cloud class ------------------------
class Cloud(Node):
    """ Cloud object """

    def __init__(self, shader, light_dir):
        """ Initialize the cloud """
        self.transform = scale(15)
        self.count = 0
        self.translate = 0.2
        super().__init__()
        #self.transform = translate(0, 26.5-80, 39) @ scale(5, 5, 5) @ rotate(vec(1, 0, 0), 90) @ rotate(vec(0, 1, 0), 90) @ rotate(vec(0, 0, 1), 90)
        self.add(*load('src/res/cloud/cloud.obj', shader, light_dir = light_dir))
        
    def draw(self, **other_uniforms):
        """ Draw the cloud """
        self.transform = translate(self.count,0,0) @ scale(15)
        self.count += self.translate
        if self.count > 100:
            self.translate = -self.translate
        elif self.count < -100:
            self.translate = -self.translate
        super().draw( **other_uniforms)
        