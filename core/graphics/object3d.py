import numpy as np
from math import sin, cos, radians, sqrt
from .vertex import Vertex
from ..configuration import *


def distance(point1, point2):
    return point1.distance(point2)


class Object3D:
    def __init__(self, position, vertices, faces, angle, color=COLOR_BLACK):
        self.position = position
        self.vertices = vertices
        self.faces = faces
        self.angle = 0
        self.rotate(self.position, angle)
        self.color = color

    def rotate(self, center, angle):
        self.angle += angle
        for ind in range(len(self.vertices)):
            vertex = self.vertices[ind].copy()
            vertex += self.position
            vertex -= center
            vertex = np.array(vertex.to_list())
            angle = radians(angle)
            matrix = np.array(
                [[cos(angle), -sin(angle), 0],
                 [sin(angle), cos(angle), 0],
                 [0, 0, 1]])
            vertex = list(vertex.dot(matrix))
            vertex += center
            vertex -= self.position
            self.vertices[ind] = vertex
