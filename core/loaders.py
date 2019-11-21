from .configuration import *
from .graphics.object3d import Object3D
from .graphics.vertex import Vertex


def load_model(model_filename):
    with open(MODELS_PATH + model_filename) as model_file:
        model_text = model_file.read().split("\n")

    vertices_text = list(map(float, model_text[0].split(",")))
    faces = [list(map(int, face_text.split(",")))
             for face_text in model_text[1].split("|")]

    vertices = []
    for j in range(len(vertices_text) // 3):
        vertices.append(Vertex(vertices_text[0],
                               vertices_text[2],
                               vertices_text[1]))

    return vertices, faces


def parse_object3d(object3d_text, models):
    data = object3d_text.split(",")
    name = data[0]
    x = float(data[1])
    y = float(data[2])
    z = float(data[3])
    angle = float(data[4])
    vertices = []
    for j in models[name][0]:
        vertices.append(j[::])
    return Object3D([x, y, z], vertices, models[name][1], angle)
