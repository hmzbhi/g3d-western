#!/usr/bin/env python3

import sys
from itertools import cycle
import OpenGL.GL as GL              # standard Python OpenGL wrapper
import glfw                         # lean window system wrapper for OpenGL
import numpy as np                  # all matrix manipulations & OpenGL args

from tools.core import Shader, Viewer, Mesh, load, Node
from texture import Texture, Textured

from tools.transform import translate, rotate, scale, identity, vec

# -------------- Cactus class ---------------------------------
class Cactus_Base(Textured):
    """ Cactus_Base object """
    def __init__(self, shader, tex_file):
        # prepare texture modes cycling variables for interactive toggling
        self.wraps = cycle([GL.GL_REPEAT, GL.GL_MIRRORED_REPEAT,
                            GL.GL_CLAMP_TO_BORDER, GL.GL_CLAMP_TO_EDGE])
        self.filters = cycle([(GL.GL_NEAREST, GL.GL_NEAREST),
                              (GL.GL_LINEAR, GL.GL_LINEAR),
                              (GL.GL_LINEAR, GL.GL_LINEAR_MIPMAP_LINEAR)])
        self.wrap, self.filter = next(self.wraps), next(self.filters)
        self.file = tex_file

        # setup Cactus_Base mesh to be textured
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
            
# -------------- Cactus_Branch class ---------------------------------
class Cactus_Branch(Textured):
    """ Cactus_Branch object """
    def __init__(self, shader, tex_file):
        # prepare texture modes cycling variables for interactive toggling
        self.wraps = cycle([GL.GL_REPEAT, GL.GL_MIRRORED_REPEAT,
                            GL.GL_CLAMP_TO_BORDER, GL.GL_CLAMP_TO_EDGE])
        self.filters = cycle([(GL.GL_NEAREST, GL.GL_NEAREST),
                              (GL.GL_LINEAR, GL.GL_LINEAR),
                              (GL.GL_LINEAR, GL.GL_LINEAR_MIPMAP_LINEAR)])
        self.wrap, self.filter = next(self.wraps), next(self.filters)
        self.file = tex_file

        # setup Cactus_branch mesh to be textured
        base_coords = ((1.5, 0, -.25), (1.5, 1, -.25), (1.5, 1, -.5), (1.5, 0, -.5), (0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 0, 5), (1, 0, 5), (1, 1, 5), (0, 1, 5))
        scaled =  np.array(base_coords, np.float32)
        indices = np.array((3, 2, 1, 3, 1, 0, 0, 1, 6, 0, 6, 5, 3, 2, 7, 3, 7, 4, 1, 2, 7, 1, 7, 6, 3, 0, 5, 3, 5, 4, 4, 5, 9, 4,9,8,5,6,10,5,10,9,6,7,11,6,11,10,7,4,8,7,8,11,8,9,10,8,10,11), np.uint32)
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

class Cactus(Node):
    """ Cactus object """

    def __init__(self, shader, viewer):
        """ Initialize the Cactus """
        super().__init__()
        
        # Load the cactus 1 object
        
        cactus_node = Node(transform=translate(2.5, -68, 90) @ rotate(vec(1, 0, 0), 90))
        cactus_node.add(Cactus_Base(shader, "src/res/cactus/cactus.jpg"))
        
        cactus_branch_node1 = Node(transform=translate(2.5, 0, 4) @ rotate(vec(0, 1, 0), 180))
        cactus_branch_node1.add(Cactus_Branch(shader, "src/res/cactus/cactus.jpg"))

        cactus_branch_node2 = Node(transform=translate(-1.5, 1, 8) @ rotate(vec(0, 1, 0), 180) @ rotate(vec(0, 0, 1), 180))
        cactus_branch_node2.add(Cactus_Branch(shader, "src/res/cactus/cactus.jpg"))      
        
        cactus_node.add(cactus_branch_node1)
        cactus_node.add(cactus_branch_node2)

        viewer.add(cactus_node)


        # Load the cactus 2 object
        
        cactus_node_2 = Node(transform=translate(25, -65, 60) @ rotate(vec(1, 0, 0), 90) @ rotate(vec(0, 0, 1), 77))
        cactus_node_2.add(Cactus_Base(shader, "src/res/cactus/cactus.jpg"))
        
        cactus_branch_node1_2 = Node(transform=translate(2.5, 0, 4) @ rotate(vec(0, 1, 0), 180))
        cactus_branch_node1_2.add(Cactus_Branch(shader, "src/res/cactus/cactus.jpg"))

        cactus_branch_node2_2 = Node(transform=translate(-1.5, 1, 8) @ rotate(vec(0, 1, 0), 180) @ rotate(vec(0, 0, 1), 180))
        cactus_branch_node2_2.add(Cactus_Branch(shader, "src/res/cactus/cactus.jpg"))      
        
        cactus_node_2.add(cactus_branch_node1_2)
        cactus_node_2.add(cactus_branch_node2_2)

        viewer.add(cactus_node_2)


        # Load the cactus 3 object
        
        cactus_node_3 = Node(transform=translate(80, -75, 22) @ rotate(vec(1, 0, 0), 90) @ rotate(vec(0, 0, 1), 37))
        cactus_node_3.add(Cactus_Base(shader, "src/res/cactus/cactus.jpg"))
        
        cactus_branch_node1_3 = Node(transform=translate(2.5, 0, 4) @ rotate(vec(0, 1, 0), 180))
        cactus_branch_node1_3.add(Cactus_Branch(shader, "src/res/cactus/cactus.jpg"))

        cactus_branch_node2_3 = Node(transform=translate(-1.5, 1, 8) @ rotate(vec(0, 1, 0), 180) @ rotate(vec(0, 0, 1), 180))
        cactus_branch_node2_3.add(Cactus_Branch(shader, "src/res/cactus/cactus.jpg"))      
        
        cactus_node_3.add(cactus_branch_node1_3)
        cactus_node_3.add(cactus_branch_node2_3)

        viewer.add(cactus_node_3)



        # Load the cactus 4 object
        
        cactus_node_4 = Node(transform=translate(-60, -75, -10) @ rotate(vec(1, 0, 0), 90) @ rotate(vec(0, 0, 1), 129))
        cactus_node_4.add(Cactus_Base(shader, "src/res/cactus/cactus.jpg"))
        
        cactus_branch_node1_4 = Node(transform=translate(2.5, 0, 4) @ rotate(vec(0, 1, 0), 180))
        cactus_branch_node1_4.add(Cactus_Branch(shader, "src/res/cactus/cactus.jpg"))

        cactus_branch_node2_4 = Node(transform=translate(-1.5, 1, 8) @ rotate(vec(0, 1, 0), 180) @ rotate(vec(0, 0, 1), 180))
        cactus_branch_node2_4.add(Cactus_Branch(shader, "src/res/cactus/cactus.jpg"))      
        
        cactus_node_4.add(cactus_branch_node1_4)
        cactus_node_4.add(cactus_branch_node2_4)

        viewer.add(cactus_node_4)



         # Load the cactus 5 object
        
        cactus_node_5 = Node(transform=translate(-90, -70, 64) @ rotate(vec(1, 0, 0), 90) @ rotate(vec(0, 0, 1), 159))
        cactus_node_5.add(Cactus_Base(shader, "src/res/cactus/cactus.jpg"))
        
        cactus_branch_node1_5 = Node(transform=translate(2.5, 0, 4) @ rotate(vec(0, 1, 0), 180))
        cactus_branch_node1_5.add(Cactus_Branch(shader, "src/res/cactus/cactus.jpg"))

        cactus_branch_node2_5 = Node(transform=translate(-1.5, 1, 8) @ rotate(vec(0, 1, 0), 180) @ rotate(vec(0, 0, 1), 180))
        cactus_branch_node2_5.add(Cactus_Branch(shader, "src/res/cactus/cactus.jpg"))      
        
        cactus_node_5.add(cactus_branch_node1_4)
        cactus_node_5.add(cactus_branch_node2_4)

        viewer.add(cactus_node_5)
        
