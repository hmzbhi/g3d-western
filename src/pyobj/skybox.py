from itertools import cycle
import glfw
import numpy as np
from OpenGL import GL
from tools.core import Mesh
from texture import Texture, TextureSquare, Textured, TextureIntiniteSky

# ------------------------ Skybox class ------------------------

class SkyBox(Textured):

    def __init__(self, shader, tex_files):
        coords = (
            (-1, -1, -1), 
            (-1, 1, -1), 
            (1, 1, -1), 
            (1, -1, -1), 
            (-1, -1, 1), 
            (-1, 1, 1), 
            (1, 1, 1), 
            (1, -1, 1), 
        )
        
        scaled = 100 * np.array(coords, np.float32)
        
        index = np.array(
            (
                (0, 2, 1),
                (0, 3, 2),
                (3, 0, 4),
                (3, 4, 7),
                (0, 5, 4),
                (0, 1, 5),
                (1, 6, 5),
                (1, 2, 6),
                (3, 7, 6),
                (3, 6, 2),
                (4, 5, 7),
                (7, 5, 6),
            ),
            np.uint32,
        )
        
        mesh = Mesh(shader, attributes=dict(position=scaled), index=index)
        texture = TextureSquare(tex_files)
        super().__init__(mesh, diffuse_map=texture)