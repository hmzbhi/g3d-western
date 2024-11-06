#!/usr/bin/env python3

import sys
from itertools import cycle
import OpenGL.GL as GL              # standard Python OpenGL wrapper
import glfw                         # lean window system wrapper for OpenGL
import numpy as np                  # all matrix manipulations & OpenGL args

from tools.core import Shader, Viewer, Mesh, load, Node
from texture import Texture, Textured

from tools.transform import translate, rotate, scale, identity, vec

# -------------- Pancart class ---------------------------------
class Pancart(Textured):
    """ Simple first textured object """
    def __init__(self, shader, tex_file):
        # prepare texture modes cycling variables for interactive toggling
        self.wraps = cycle([GL.GL_REPEAT, GL.GL_MIRRORED_REPEAT,
                            GL.GL_CLAMP_TO_BORDER, GL.GL_CLAMP_TO_EDGE])
        self.filters = cycle([(GL.GL_NEAREST, GL.GL_NEAREST),
                              (GL.GL_LINEAR, GL.GL_LINEAR),
                              (GL.GL_LINEAR, GL.GL_LINEAR_MIPMAP_LINEAR)])
        self.wrap, self.filter = next(self.wraps), next(self.filters)
        self.file = tex_file

        # setup Pancart mesh to be textured
        base_coords = ((0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 0, 5), (1, 0, 5), (1, 1, 5), (0, 1, 5), (0.5, 0, 6), (0.5, 1, 6))
        scaled =  np.array(base_coords, np.float32)
        indices = np.array((0, 1, 2, 0, 2, 3, 4, 5, 6, 4, 6, 7, 0, 1, 5, 0, 5, 4, 1, 2, 6, 1, 6, 5, 2, 3, 7, 2, 7, 6, 3, 0, 4, 3, 4, 7, 4, 5, 8, 5, 6, 9, 5, 9, 8, 6, 7, 9, 7, 4, 8, 7, 8, 9), np.uint32)
        mesh = Mesh(shader, attributes=dict(position=scaled), index=indices)

        # setup & upload texture to GPU, bind it to shader name 'diffuse_map'
        texture = Texture(tex_file, self.wrap, *self.filter)
        super().__init__(mesh, diffuse_map=texture)

    def key_handler(self, key):
        # cycle through texture modes on keypress of F6 (wrap) or F7 (filtering)
        self.wrap = next(self.wraps) if key == glfw.KEY_F6 else self.wrap
        self.filter = next(self.filters) if key == glfw.KEY_F7 else self.filter
        if key in (glfw.KEY_F6, glfw.KEY_F7):
            texture = Texture(self.file, self.wrap, *self.filter)
            self.textures.update(diffuse_map=texture)
            
# -------------- Poteau class ---------------------------------
class Poteau(Textured):
    """ Poteau object """
    def __init__(self, shader, tex_file):
        # prepare texture modes cycling variables for interactive toggling
        self.wraps = cycle([GL.GL_REPEAT, GL.GL_MIRRORED_REPEAT,
                            GL.GL_CLAMP_TO_BORDER, GL.GL_CLAMP_TO_EDGE])
        self.filters = cycle([(GL.GL_NEAREST, GL.GL_NEAREST),
                              (GL.GL_LINEAR, GL.GL_LINEAR),
                              (GL.GL_LINEAR, GL.GL_LINEAR_MIPMAP_LINEAR)])
        self.wrap, self.filter = next(self.wraps), next(self.filters)
        self.file = tex_file

        # setup Poteau mesh to be textured
        base_coords = ((0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 0, 15), (1, 0, 15), (1, 1, 15), (0, 1, 15))
        scaled =  np.array(base_coords, np.float32)
        indices = np.array((0, 1, 2, 0, 2, 3, 4, 5, 6, 4, 6, 7, 0, 1, 5, 0, 5, 4, 1, 2, 6, 1, 6, 5, 2, 3, 7, 2, 7, 6, 3, 0, 4, 3, 4, 7), np.uint32)
        mesh = Mesh(shader, attributes=dict(position=scaled), index=indices)

        # setup & upload texture to GPU, bind it to shader name 'diffuse_map'
        texture = Texture(tex_file, self.wrap, *self.filter)
        super().__init__(mesh, diffuse_map=texture)

    def key_handler(self, key):
        # cycle through texture modes on keypress of F6 (wrap) or F7 (filtering)
        self.wrap = next(self.wraps) if key == glfw.KEY_F6 else self.wrap
        self.filter = next(self.filters) if key == glfw.KEY_F7 else self.filter
        if key in (glfw.KEY_F6, glfw.KEY_F7):
            texture = Texture(self.file, self.wrap, *self.filter)
            self.textures.update(diffuse_map=texture)

# ------------------------ Pancarts class ------------------------

class Pancarts(Node):
    """ Pancarts object """

    def __init__(self, shader, viewer):
        """ Initialize the Pancarts """
        super().__init__()
        
        # Load the pancart 1 object
        
        poteau_node = Node(transform= translate(-22, 26.5-86.2, 40) @ rotate(vec(1, 0, 0), 90))
        poteau_node.add(Poteau(shader, "src/res/pancart/pancart.jpeg"))
        
        pancart_node = Node(transform=translate(2, 1.5, 2) @ rotate(vec(1, 0, 0), 90) @ rotate(vec(0, 0, 1), 90))
        pancart_node.add(Pancart(shader, "src/res/pancart/pancart.jpeg"))     
        
        poteau_node.add(pancart_node)

        viewer.add(poteau_node)
        
