import numpy as np
import shapely
from shapely.geometry import LineString

cache = {}

def s(n):
    if n == 0:
        return 290797
    elif n in cache:
        return cache[n]
    else:
        cache[n] = pow(s(n - 1), 2) % 50515093
        return cache[n]

def t(n):
    return s(n) % 500


points_found = set()
LIMIT = 20000
data = [LineString([(t(i), t(i+1)), (t(i+2), t(i+3))]) for i in range(1, LIMIT + 1, 4)]

for i in range(len(data)):
    print(i, len(points_found))
    for j in range(i + 1, len(data)):
        candidate = data[i].intersection(data[j])
        if type(candidate) == shapely.geometry.Point and (candidate.x, candidate.y) not in data[i].coords and (candidate.x, candidate.y) not in data[j].coords:
            points_found.add((candidate.x, candidate.y))

print(points_found)
print(len(points_found))
