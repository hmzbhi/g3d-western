#!/usr/bin/env python3
"""
Python OpenGL practical application.
"""
# Python built-in modules
import os                           # os function, i.e. checking file status
import sys                          # for sys.exit

# External, non built-in modules
import OpenGL.GL as GL              # standard Python OpenGL wrapper
import glfw                         # lean window system wrapper for OpenGL
import numpy as np                  # all matrix manipulations & OpenGL args

from tools.transform import translate, rotate, scale, vec, perspective, identity, quaternion, quaternion_from_euler
from tools.core import Viewer, Shader, Mesh, Node, load
from tools.animation import KeyFrameControlNode

from pyobj.skybox import SkyBox
from pyobj.horse import Horse
from pyobj.horse_cart import HorseCart
from pyobj.pancarts import Pancarts
from pyobj.river import River
from pyobj.terrain import Terrain
from pyobj.cloud import Cloud
from pyobj.cactus import Cactus
from pyobj.fire import Fire
from pyobj.smoke import Smoke

from texture import Texture, TextureSquare, TextureIntiniteSky

import assimpcy
# ------------------------ Scene class ------------------------

class Scene(Node):
    """  Scene object containing all the objects to be rendered """

    def __init__(self, viewer):
        """ Initialize the scene with viewer """
        super().__init__()
        self.viewer = viewer
        self.viewer.transform = scale(10)

        ########## Add objects to the scene ##########
        
        # Load the skybox object
        
        skybox_textures = ['src/res/skybox/left.png', 
                           'src/res/skybox/right.png', 
                           'src/res/skybox/top.png', 
                           'src/res/skybox/bottom.png', 
                           'src/res/skybox/back.png', 
                           'src/res/skybox/front.png']
        skybox_shaders = Shader("src/shaders/skybox/skybox.vert", "src/shaders/skybox/skybox.frag")
        viewer.add(SkyBox(skybox_shaders, skybox_textures))
        

        # Load the terrain object
        
        shader = Shader("src/shaders/ground/terrain.vert", "src/shaders/ground/terrain.frag")
        viewer.add(Terrain(shader))

        # Load the horse object
        
        shader = Shader("src/shaders/horse/horse.vert", "src/shaders/horse/horse.frag")
        viewer.add(Horse(shader))

        # Load the horse-cart object
        
        shader = Shader("src/shaders/horse-cart/cart.vert", "src/shaders/horse-cart/cart.frag")
        viewer.add(HorseCart(shader))


        # Load the pancarts object create by us with hierarchical dependencies
        
        shader = Shader("src/shaders/pancart/pancart.vert", "src/shaders/pancart/pancart.frag")
        viewer.add(Pancarts(shader, viewer))

        # Load the river
        
        shader = Shader("src/shaders/river/river.vert", "src/shaders/river/river.frag")
        viewer.add(River(shader))
        
        # Load the cactus object
        shader = Shader("src/shaders/cactus/cactus.vert", "src/shaders/cactus/cactus.frag")
        viewer.add(Cactus(shader, viewer))

        # Load the fire object
        shader = Shader("src/shaders/fire/fire.vert", "src/shaders/fire/fire.frag")
        viewer.add(Fire(shader))
        
        # Load Cloud Object made with Blender and animated and with light_dir
        
        shader = Shader("src/shaders/cloud/cloud.vert", "src/shaders/cloud/cloud.frag")   
        viewer.add(Cloud(shader, light_dir=vec(1,0,0)))
        
        # Load Smoke particules
        
        shader = Shader("src/shaders/smoke/smoke.vert", "src/shaders/smoke/smoke.frag")
        viewer.add(Smoke(shader))
        
        
    def draw(self, model=identity(), **other_uniforms):
        """ Draw all the objects in the scene """
        super().draw(model=model, **other_uniforms)
