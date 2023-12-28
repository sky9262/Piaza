# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
def valid_move(board, x, y, player):
    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[0]):
            continue
        if board[nx][ny] == '.' or board[nx][ny] == player:
            continue
        while 0 <= nx < len(board) and 0 <= ny < len(board[0]):
            if board[nx][ny] == player:
                return True
            if board[nx][ny] == '.':
                break
            nx += dx
            ny += dy
    return False

def count_valid_moves(board, player):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '.' and valid_move(board, i, j, player):
                count += 1
    return count

N = int(input().strip())
board = [list(input().strip()) for _ in range(N)]
print(count_valid_moves(board, 'B'))
