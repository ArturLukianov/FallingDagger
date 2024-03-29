import random
import math
from core.configuration import *


class ModelMapping:
    def __init__(self, object_name, x, y, z, angle):
        self.object_name = object_name
        self.x = x
        self.y = y
        self.z = z
        self.angle = angle

    def __str__(self):
        return '%s,%d,%d,%d,%d' % (self.object_name, self.x, self.y, self.z, self.angle)

    def __repr__(self):
        return str(self)


def generate_floor(x, y, columns, rows):
    floor = []
    for i in range(rows):
        for j in range(columns):
            object_name = 'floor'
            if (i + j) % 2:
                object_name = 'black_floor'
            floor.append(ModelMapping(object_name, x + i * BRICK_SIZE, y + j * BRICK_SIZE, 1, 0))
    return floor


def save_map(map_to_save, filename):
    with open(filename, 'w') as map_file:
        map_file.write('\n'.join(map(str, map_to_save)))


def generate_labyrinth(x, y, columns, rows):
    labyrinth = generate_floor(x, y, columns, rows)
    used = [[0 for j in range(rows)]
            for i in range(columns)]
    wall = [[[1, 1, 1, 1]
             for j in range(rows)]
            for i in range(columns)]
    dfs_mask = [(0, 1, 0), (1, 0, 1),
                (0, -1, 2), (-1, 0, 3)]

    def random_dfs(offset_x, offset_y):
        used[offset_y][offset_x] = 1
        for (xm, ym, wall_direction) in random.sample(dfs_mask, len(dfs_mask)):
            new_x_offset = offset_x + xm
            new_y_offset = offset_y + ym
            is_x_on_field = columns > new_x_offset >= 0
            is_y_on_field = columns > new_y_offset >= 0
            if not (is_x_on_field and is_y_on_field):
                continue
            if used[new_y_offset][new_x_offset]:
                continue
            used[new_y_offset][new_x_offset] = 1
            wall[offset_y][offset_x][wall_direction] = 0
            wall[new_y_offset][new_x_offset][(wall_direction + 2) % 4] = 0
            random_dfs(new_x_offset, new_y_offset)

    random_dfs(0, 0)
    wall_color = ['wall', 'black_wall']

    for i in range(columns):
        for j in range(rows):
            for (xn, yn, ind) in dfs_mask:
                if wall[i][j][ind]:
                    if ind % 2:
                        labyrinth.append(ModelMapping(wall_color[random.randint(0, 1)], x + xn + j * BRICK_SIZE,
                                                        y + yn + i * BRICK_SIZE, 0, 90))
                    else:
                        labyrinth.append(ModelMapping(wall_color[random.randint(0, 1)], x + xn + j * BRICK_SIZE,
                                                        y + yn + i * BRICK_SIZE, 0, 0))
    return labyrinth


def generate():
    generated_map = []
    generated_map += generate_labyrinth(0, 0, 10, 10)

    save_map(generated_map, 'resourses/maps/map')
