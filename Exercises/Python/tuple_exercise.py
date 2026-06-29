import math

a = (3,4)
origin = (0,0)

x1, y1 = a
x2, y2 = origin

distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

print(distance)