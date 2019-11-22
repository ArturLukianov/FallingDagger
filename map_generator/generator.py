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


def generate_floor(x, y, n, m):
    floor = []
    for i in range(m):
        for j in range(n):
            object_name = 'floor'
            if (i + j) % 2:
                object_name = 'black_floor'
            floor.append(ModelMapping(object_name, x + i * 2, y + j * 2, 1, 0))
    return floor


def save_map(map_to_save, filename):
    with open(filename, 'w') as map_file:
        map_file.write('\n'.join(map(str, map_to_save)))


generated_map = []
generated_map += generate_floor(0, 0, 10, 10)

save_map(generated_map, '../resourses/maps/map')
