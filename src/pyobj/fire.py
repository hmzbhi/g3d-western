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

# ------------------------ Fire class ------------------------
class Fire(Node):
    """ Fire object """

    def __init__(self, shader):
        """ Initialize the Horse """
        super().__init__()
        self.transform = translate(10, 26.5-100.2, 45) @ scale(1) 
        self.add(*load('src/res/fire/fire.obj', shader))
        