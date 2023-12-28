h, w, s = map(int, input().split())
seats = [[0 for _ in range(w)] for _ in range(h)]

total_rows = len(seats)
total_columns = len(seats[0])

for i in range(s):
    s_seat = int(input())
    x = (s_seat - 1) // total_columns
    y = (s_seat - 1) % total_columns
    seats[x][y] = i + 1
    
new_seats = seats
for i in range(total_rows):
    for j in range(total_columns):
        if seats[i][j] > 0 and seats[i-1][j] == 0:
            k = i
            while k > 0 and seats[k-1][j] == 0:
                seats[k-1][j] = seats[k][j]
                seats[k][j] = 0
                k -= 1

for row in seats:
    print(' '.join(map(str, row)))
