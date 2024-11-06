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

from tools.transform import translate, rotate, scale, vec, perspective

import time
from tools.core import Viewer, Shader, Mesh
from scene import Scene

# -------------- main program and scene setup --------------------------------
def main():
    """ create window, add shaders & scene objects, then run rendering loop """

    print("AVANT DE RUN LE PROJET, VEUILLEZ LIRE LE README.txt S'IL VOUS PLAIT")
    print("beginning loading...")
    start = time.time()

    viewer = Viewer()
    
    scene = Scene(viewer)
    viewer.add(scene)
    
    end = time.time()
    print(f"loading took {end - start} seconds")
    
    # start rendering loop
    viewer.run()


if __name__ == "__main__":
    main()