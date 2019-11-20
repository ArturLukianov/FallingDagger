import pygame
from classes import Object, dist

screen = pygame.display.set_mode((400, 400))

done = False

model_names = ["wall"]

Models = []

Map = open("map").read().split("\n")

objects = []

for i in model_names:
    f = open(i)
    f = f.read().split("\n")
    f[0] = f[0].split(",")
    verts = []
    for j in range(len(f[0]) // 3):
        x = float(f[0][j * 3])
        y = float(f[0][j * 3 + 1])
        z = float(f[0][j * 3 + 2])
        verts.append([x, y, z])
    faces = []
    f[1] = f[1].split("|")
    for j in f[1]:
        faces.append(list(map(int, j.split(","))))
    Models.append([i, [verts, faces]])

Models = dict(Models)

ppos = [0, 0, 0]
pv = [0, 0, 0]

for i in Map:
    data = i.split(",")
    name = data[0]
    x = float(data[1])
    y = float(data[2])
    z = float(data[3])
    deg = float(data[4])
    verts = []
    for j in Models[name][0]:
        verts.append(j[::])
    objects.append(Object([x, y, z], verts, Models[name][1], deg))

while not done:
    ppos[0] += pv[0]
    ppos[1] += pv[1]
    ppos[2] += pv[2]
    #objects[0].rotate([0, 5, 0], 0.2)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = True
        if e.type == pygame.KEYDOWN:
            if e.scancode == 17:
                pv[1] = 0.005
            elif e.scancode == 31:
                pv[1] = -0.005
        if e.type == pygame.KEYUP:
            if e.scancode == 17 and pv[1] > 0: 
                pv[1] = 0
            if e.scancode == 31 and pv[1] < 0: 
                pv[1] = 0
            
    screen.fill((0, 0, 0))

    points = []
    for i in objects:
        for j in i.verts:
            z = j[1] + i.pos[1] - ppos[1]
            t = 1
            if round(z, 3) == 0:
                t = 0
                f = 200 / 1
            else:
                f = 200 / z
            if z < 0:
                t = 0
                f *= -2
            x = int((j[0] + i.pos[0] - ppos[0]) * f + 200)
            y = int((j[2] + i.pos[2] - ppos[2]) * f + 200)
            d = dist(j, [0, 0, 0])
            points.append([[x, y], d, t])
    order = []
    k = 0
    for i in objects:
        for f in i.faces:
            face = []
            d = 0
            s = []
            for j in f:
                face.append(points[k + j][0])
                d += points[k + j][1]
                s.append(points[k + j][2])
            d /= len(f)
            order.append([d, face, sum(s)])
        k += len(i.verts)
    order = sorted(order)[::-1]
    for i in order:
        if i[2] > 0:
            pygame.draw.polygon(screen, (255, 255, 255), i[1])
    pygame.display.flip()
pygame.quit()
