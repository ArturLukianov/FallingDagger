import pygame
import os
from core.configuration import *
from core.graphics.vertex import Vertex
from core.characters.player import Player
from core.characters.position import Position
from core.characters.delta_position import DeltaPosition
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

current_map = []

with open(MAPS_PATH + "map") as current_map_file:
    current_map = current_map_file.read().split("\n")

objects3d = []
for object3d in current_map:
    objects3d.append(parse_object3d(object3d, models))

game_running = True

while game_running:
    for object3d in objects3d:
        object3d.rotate(player.position.to_vertex(), player.angle_velocity)
    # Apply physical forces
    player.apply_velocity()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.velocity.y = PLAYER_VELOCITY
            elif event.key == pygame.K_DOWN:
                player.velocity.y = -PLAYER_VELOCITY
            elif event.key == pygame.K_RIGHT:
                player.angle_velocity = -PLAYER_ANGLE_VELOCITY
            elif event.key == pygame.K_LEFT:
                player.angle_velocity = PLAYER_ANGLE_VELOCITY
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP and player.velocity.y > 0:
                player.velocity.y = 0
            if event.key == pygame.K_DOWN and player.velocity.y < 0:
                player.velocity.y = 0
            elif event.key == pygame.K_RIGHT and player.angle_velocity < 0:
                player.angle_velocity = 0
            elif event.key == pygame.K_LEFT and player.angle_velocity > 0:
                player.angle_velocity = 0

    rendering_points = []
    for object3d in objects3d:
        for vertex in object3d.vertices:
            z = vertex.y + object3d.position.y - player.position.y
            need_rendering = 1
            if round(z, 3) == 0:
                need_rendering = 0
                distance_koef = HALF_SCREEN_HEIGHT
            else:
                distance_koef = HALF_SCREEN_HEIGHT / z
            if z < 0:
                need_rendering = 0
                distance_koef *= -2
            x = int((vertex.x + object3d.position.x - player.position.x) * distance_koef + HALF_SCREEN_WIDTH)
            y = int((vertex.z + object3d.position.z - player.position.z) * distance_koef + HALF_SCREEN_HEIGHT)
            depth = vertex.distance(player.position.to_vertex())
            rendering_points.append(((x, y), depth, need_rendering, vertex))

    # Sorting polygon points for rendering
    order = []
    offset = 0
    for object3d in objects3d:
        for ind, object_face in enumerate(object3d.faces):
            face = []
            rendering_vertex_count = 0
            mean_x = 0
            mean_y = 0
            mean_z = 0
            for vertex_index in range(len(object_face)):
                rendering_point = rendering_points[offset + vertex_index]
                face.append(rendering_point[0])
                mean_x += rendering_point[3].x + object3d.position.x
                mean_y += rendering_point[3].y + object3d.position.y
                mean_z += rendering_point[3].z + object3d.position.z
                rendering_vertex_count += rendering_point[2]
            mean_x /= len(object_face)
            mean_y /= len(object_face)
            mean_z /= len(object_face)
            depth = player.position.to_vertex().distance(Vertex(mean_x, mean_y, mean_z))
            order.append((depth, face, rendering_vertex_count, object3d.colors[ind]))
        offset += len(object3d.vertices)

    # Rendering
    screen.fill(BACKGORUND)
    for polygon in reversed(sorted(order)):
        if polygon[2] > 0 and polygon[0] < 20:
            depth = polygon[0]
            r, g, b = (min(color_value / depth * 4, 255)
                       for color_value in polygon[3] if depth != 0)
            if depth == 0:
                r, g, b = 255, 255, 255
            pygame.draw.polygon(screen, (r, g, b), polygon[1])
    pygame.display.update()
pygame.quit()
