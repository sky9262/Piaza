# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def find_island(islands, x, y, R):
    for i, (cx, cy, cr) in enumerate(islands):
        if distance(cx, cy, x, y) <= 2*R:
            return i
    return None

def combine_islands(islands, i, j):
    xi, yi, ri = islands[i]
    xj, yj, rj = islands[j]
    cx = (xi + xj) / 2
    cy = (yi + yj) / 2
    cr = max(distance(xi, yi, cx, cy) + ri, distance(xj, yj, cx, cy) + rj)
    islands.pop(j)
    islands[i] = (cx, cy, cr)

def count_islands(N, R, coordinates):
    islands = []
    for x, y in coordinates:
        island_index = find_island(islands, x, y, R)
        if island_index is not None:
            islands[island_index] = (x, y, R)
        else:
            islands.append((x, y, R))

    islands_copy = islands[:]

    for i in range(len(islands_copy)):
        for j in range(i+1, len(islands_copy)):
            if distance(islands_copy[i][0], islands_copy[i][1], islands_copy[j][0], islands_copy[j][1]) < 2*R:
                combine_islands(islands, i, j)

    return len(islands)



N, R = map(int, input().split())
coordinates = [tuple(map(int, input().split())) for _ in range(N)]

result = count_islands(N, R, coordinates)
print(result)
