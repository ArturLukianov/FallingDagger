from .configuration import *
from .graphics.object3d import Object3D


def load_model(model_filename):
    with open(MAPS_PATH + model_filename) as model_file:
        object_face = model_file.read().split("\n")
    object_face[0] = object_face[0].split(",")
    verticles = []
    for j in range(len(object_face[0]) // 3):
        verticle = []
        for k in range(3):
            verticle.append(float(object_face[0][j * 3 + k]))
        verticles.append(verticle)
    faces = []
    object_face[1] = object_face[1].split("|")
    for j in object_face[1]:
        faces.append(list(map(int, j.split(","))))


def parse_object3d(object3d_text, models):
    data = object3d_text.split(",")
    name = data[0]
    x = float(data[1])
    y = float(data[2])
    z = float(data[3])
    deg = float(data[4])
    verticles = []
    for j in models[name][0]:
        verticles.append(j[::])
    return Object3D([x, y, z], verticles, models[name][1], deg)