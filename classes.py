import numpy as np
from math import sin, cos, radians, sqrt

h = 2

def dist(p1, p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    z = p1[2] - p2[2]
    return sqrt(x*x + y*y + z*z)

def rotate(vert, center, deg):
    vert[0] -= center[0]
    vert[1] -= center[1]
    vert[2] -= center[2]
    vert = np.array(vert)
    deg = radians(deg)
    Matrix = [[cos(deg), -sin(deg), 0],
              [sin(deg), cos(deg), 0],
              [0, 0, 1]]
    Matrix = np.array(Matrix)
    vert = vert.dot(Matrix)
    vert = list(vert)
    vert[0] += center[0]
    vert[1] += center[1]
    vert[2] += center[2]
    return vert

class Object:
    def __init__(self, pos, verts, faces, deg):
        self.pos = pos
        self.verts = verts
        self.faces = faces
        self.deg = 0
        self.rotate(self.pos, deg)

    def rotate(self, ppos, deg):
        self.deg += deg
        for i in range(len(self.verts)):
            vert = self.verts[i]
            vert[0] += self.pos[0]
            vert[1] += self.pos[1]
            vert[2] += self.pos[2]
            vert = rotate(vert, ppos, deg)
            vert[0] -= self.pos[0]
            vert[1] -= self.pos[1]
            vert[2] -= self.pos[2]
            self.verts[i] = vert
