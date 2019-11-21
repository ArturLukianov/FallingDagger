import numpy as np
from math import sin, cos, radians, sqrt
from .vertex import Vertex


def distance(point1, point2):
    return point1.distance(point2)


def rotate_vertex(vertex, center, angle):
    vertex -= center
    vertex = np.array(vertex.to_list())
    angle = radians(angle)
    matrix = np.array(
        [[cos(angle), -sin(angle), 0],
         [sin(angle), cos(angle), 0],
         [0, 0, 1]])
    vertex = list(vertex.dot(matrix))
    vertex += center
    return vertex


class Object3D:
    def __init__(self, position, vertices, faces, angle):
        self.position = position
        self.vertices = vertices
        self.faces = faces
        self.angle = 0
        self.rotate(self.position, angle)

    def rotate(self, center, angle):
        self.angle += angle
        for vertex in self.vertices:
            vertex += self.position
            vertex = rotate_vertex(vertex, center, angle)
            vertex -= self.position
