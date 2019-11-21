import pygame
import os
from .core.configuration import *
from .core.graphics.object3d import Object3D, distance
from .core.graphics.verticle import *
from .core.player import Player
from .core.position import Position
from .core.delta_position import DeltaPosition
from .core.loaders import load_model, parse_object3d

game_running = False

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player(Position(0, 0))

model_files = os.listdir(MODELS_PATH)
models = {}

for model_filename in model_files:
    models[model_filename] = load_model(model_filename)

player_position = player.position.to_3d()
player_velocity = [0, 0, 0]

with open(MAPS_PATH + "map") as current_map_file:
    current_map = current_map_file.read().split("\n")
objects3d = []

for object3d in current_map:
    objects3d.append(parse_object3d(object3d, models))

game_running = True

while game_running:
    # Move player
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game_running = False
        if e.type == pygame.KEYDOWN:
            if e.scancode == 17:
                player_velocity[1] = 0.005
            elif e.scancode == 31:
                player_velocity[1] = -0.005
        if e.type == pygame.KEYUP:
            if e.scancode == 17 and player_velocity[1] > 0:
                player_velocity[1] = 0
            if e.scancode == 31 and player_velocity[1] < 0:
                player_velocity[1] = 0

    screen.fill(COLOR_BLACK)

    rendering_points = []
    for object3d in objects3d:
        for j in object3d.verticles:
            z = j[1] + object3d.position[1] - player_position[1]
            t = 1
            if round(z, 3) == 0:
                t = 0
                object_face = 200 / 1
            else:
                object_face = 200 / z
            if z < 0:
                t = 0
                object_face *= -2
            x = int((j[0] + object3d.position[0] - player_position[0]) * object_face + 200)
            y = int((j[2] + object3d.position[2] - player_position[2]) * object_face + 200)
            depth = distance(j, [0, 0, 0])
            rendering_points.append([[x, y], depth, t])
    order = []
    k = 0
    for object3d in objects3d:
        for object_face in object3d.faces:
            face = []
            depth = 0
            s = []
            for j in object_face:
                face.append(rendering_points[k + j][0])
                depth += rendering_points[k + j][1]
                s.append(rendering_points[k + j][2])
            depth /= len(object_face)
            order.append([depth, face, sum(s)])
        k += len(object3d.verticles)
    for object3d in reversed(sorted(order)):
        if object3d[2] > 0:
            pygame.draw.polygon(screen, COLOR_WHITE, object3d[1])
    pygame.display.flip()
pygame.quit()
