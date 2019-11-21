from .configuration import *
from .graphics.object3d import Object3D


def load_model(model_filename):
    with open(MAPS_PATH + model_filename) as model_file:
        model_text = model_file.read().split("\n")

    model_text[0] = model_text[0].split(",")
    model_text[1] = model_text[1].split("|")

    verticles = []
    for j in range(len(model_text[0]) // 3):
        verticle = []
        for k in range(3):
            verticle.append(float(model_text[0][j * 3 + k]))
        verticles.append(verticle)

    faces = []
    for j in model_text[1]:
        faces.append(list(map(int, j.split(","))))
    return verticles, faces


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
