# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
puzzle = []
rows = int(input())
for _ in range(rows):
    row = input()
    puzzle.append([int(x) if x.isdigit() else x for x in row])

def valid_moves(puzzle, x, y):
    moves = []
    rows, cols = len(puzzle), len(puzzle[0])

    # Check if moving up is a valid move
    if x - 1 >= 0:
        moves.append((x - 1, y))

    # Check if moving down is a valid move
    if x + 1 < rows:
        moves.append((x + 1, y))

    # Check if moving left is a valid move
    if y - 1 >= 0:
        moves.append((x, y - 1))

    # Check if moving right is a valid move
    if y + 1 < cols:
        moves.append((x, y + 1))

    return moves

def find_same_neighbours(puzzle):
    rows, cols = len(puzzle), len(puzzle[0])
    result = []

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def get_neighbours(x, y):
        neighbours = [
            (x - 1, y),  # Up
            (x + 1, y),  # Down
            (x, y - 1),  # Left
            (x, y + 1),  # Right
        ]
        return [(nx, ny) for nx, ny in neighbours if is_valid(nx, ny)]

    def has_same_neighbours(x, y):
        if puzzle[x][y] == '.':
            return False
        value = puzzle[x][y]
        neighbours = get_neighbours(x, y)

        return all(is_valid(nx, ny) and puzzle[nx][ny] == value for nx, ny in neighbours)

    for i in range(rows):
        for j in range(cols):
            if has_same_neighbours(i, j):
                result.append((i, j))
                result.extend([(nx, ny) for nx, ny in get_neighbours(i, j)])


    return result

def apply_gravity(puzzle):
    rows, cols = len(puzzle), len(puzzle[0])

    for col in range(cols):
        # Extract the column values
        column_values = [puzzle[row][col] for row in range(rows)]

        # Filter out the dots and keep the numbers
        numbers = [value for value in column_values if value != '.']

        # Fill the column from bottom to top
        for row in range(rows - 1, -1, -1):
            if numbers:
                puzzle[row][col] = numbers.pop()  # Fill with numbers
            else:
                puzzle[row][col] = '.'  # Fill empty space with dot

while True:
    blow = find_same_neighbours(puzzle)
    if len(blow) == 0:
        break
    for a,b in blow:
        puzzle[a][b] = "."
    apply_gravity(puzzle)
for row in puzzle:
    print(''.join(map(str, row)))