import numpy as np
from math import sin, cos, radians, sqrt

h = 2


def distance(point1, point2):
    x = point1[0] - point2[0]
    y = point1[1] - point2[1]
    z = point1[2] - point2[2]
    return sqrt(x * x + y * y + z * z)


def rotate_verticle(verticle, center, degrees):
    for i in range(3):
        verticle[i] -= center[i]
    verticle = np.array(verticle)
    degrees = radians(degrees)
    matrix = np.array(
        [[cos(degrees), -sin(degrees), 0],
         [sin(degrees), cos(degrees), 0],
         [0, 0, 1]])
    verticle = list(verticle.dot(matrix))
    for i in range(3):
        verticle[i] += center[i]
    return verticle


class Object3D:
    def __init__(self, position, verticles, faces, degrees):
        self.position = position
        self.verticles = verticles
        self.faces = faces
        self.degree = 0
        self.rotate(self.position, degrees)

    def rotate(self, player_position, degrees):
        self.degree += degrees
        for i in range(len(self.verticles)):
            verticles = self.verticles[i]
            for j in range(3):
                verticles[j] += self.position[j]
            verticles = rotate_verticle(verticles, player_position, degrees)
            for j in range(3):
                verticles[j] -= self.position[j]
            self.verticles[i] = verticles
