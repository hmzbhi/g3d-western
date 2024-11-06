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
# ------------------------ HorseCart class ------------------------
class HorseCart(Node):
    """ HorseCart object """

    def __init__(self, shader):
        """ Initialize the HorseCart """
        super().__init__()
        self.transform = translate(10+10, 26.5-98.5, 39) @ scale(0.05, 0.05, 0.05)
        self.add(*load('src/res/horse-cart/Cart.obj', shader))
        