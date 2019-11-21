import pygame
import os
from core.configuration import *
from core.graphics.object3d import Object3D, distance
from core.graphics.vertex import Vertex
from core.player import Player
from core.position import Position
from core.delta_position import DeltaPosition
from core.loaders import load_model, parse_object3d

game_running = False

if FULLSCREEN:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player(Position(0, 0),
                velocity=DeltaPosition(0, 0),
                name="Player")

model_files = os.listdir(MODELS_PATH)
models = {}

for model_filename in model_files:
    models[model_filename] = load_model(model_filename)

with open(MAPS_PATH + "map") as current_map_file:
    current_map = current_map_file.read().split("\n")

objects3d = []
for object3d in current_map:
    objects3d.append(parse_object3d(object3d, models))

game_running = True

while game_running:
    # Apply physical forces
    player.apply_velocity()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.velocity.x = 0.005
            elif event.key == pygame.K_DOWN:
                player.velocity.x = -0.005
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP and player.velocity.x > 0:
                player.velocity.x = 0
            if event.key == pygame.K_DOWN and player.velocity.x < 0:
                player.velocity.x = 0

    rendering_points = []
    for object3d in objects3d:
        for vertex in object3d.verticles:
            z = vertex.z + object3d.position.z - player.position.z
            need_rendering = 1
            if round(z, 3) == 0:
                need_rendering = 0
                distance_koef = 200 / 1
            else:
                distance_koef = 200 / z
            if z < 0:
                need_rendering = 0
                distance_koef *= -2
            x = int((vertex.x + object3d.x - player.position.x) * distance_koef + HALF_SCREEN_WIDTH)
            y = int((vertex.y + object3d.y - player.position.y) * distance_koef + HALF_SCREEN_HEIGHT)
            depth = distance(vertex, [0, 0, 0])
            rendering_points.append([[x, y], depth, need_rendering])

    # Sorting polygon points for rendering
    order = []
    offset = 0
    for object3d in objects3d:
        for object_face in object3d.faces:
            face = []
            depth = 0
            rendering_vertex_count = 0
            for vertex_index in range(len(object_face)):
                face.append(rendering_points[offset + vertex_index][0])
                depth += rendering_points[offset + vertex_index][1]
                rendering_vertex_count += rendering_points[offset + vertex_index][2]
            depth /= len(object_face)
            order.append([depth, face, rendering_vertex_count])
        offset += len(object3d.verticles)

    # Rendering
    screen.fill(COLOR_BLACK)
    for polygon in reversed(sorted(order)):
        if polygon[2] > 0:
            pygame.draw.polygon(screen, COLOR_WHITE, polygon[1])
    pygame.display.update()
pygame.quit()
