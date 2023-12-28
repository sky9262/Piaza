from collections import deque

def calculate_points(layer, step):
    total_points = 0
    for position in step:
        x, y = position
        total_points += layer[x][y] if isinstance(layer[x][y], int) else 0
    return total_points

def maxPoint(layer, steps):
    max_point = 0
    best_step = None

    for step in steps:
        points = calculate_points(layer, step)
        if points > max_point:
            max_point = points
            best_step = step
    # print("Best step:", best_step)
    # print("Maximum points:", max_point)
    return max_point

def get_neighbors(matrix, row, col):
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]) and matrix[new_row][new_col] != 'S':
            neighbors.append((new_row, new_col))

    return neighbors

def find_shortest_paths(matrix, start, end):
    queue = deque([(start, [start])])
    visited = set()

    paths = []

    while queue:
        current, path = queue.popleft()
        visited.add(current)

        if current == end:
            paths.append(path)
            continue

        for neighbor in get_neighbors(matrix, *current):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    # print(paths)
    return paths

# Read the size of the layer
H, W = map(int, input("").split())

# Read the number of layers
N = int(input(""))

layers = []

# Read each layers
for _ in range(N):
    layer = []
    for _ in range(H):
        row = input().split()
        row = [int(num) if num.isdigit() else num for num in row] # Convert numbers to integers
        layer.append(row)
    layers.append(layer)


shortest_paths = []
for layer in layers:
    start_position = None
    end_position = None

    for i in range(len(layer)):
        for j in range(len(layer[0])):
            if layer[i][j] == 'S':
                start_position = (i, j)
            elif layer[i][j] == 'G':
                end_position = (i, j)

    shortest_paths.append(find_shortest_paths(layer, start_position, end_position))

totalPoints = 0
for i, path in enumerate(shortest_paths):
    totalPoints += maxPoint(layers[i], path)
print(totalPoints)
