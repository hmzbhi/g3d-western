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
# ------------------------ Horse class ------------------------
class Horse(Node):
    """ Horse object """

    def __init__(self, shader):
        """ Initialize the Horse """
        super().__init__()
        self.transform = translate(0, 26.5-100.2, 39) @ scale(0.005, 0.005, 0.005) @ rotate(vec(1, 0, 0), 90) @ rotate(vec(0, 1, 0), 180) @ rotate(vec(0, 0, 1), 90)
        self.add(*load('src/res/horse/horse.obj', shader))
        