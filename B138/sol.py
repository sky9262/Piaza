h, w = map(int, input().split())
donut_box = []

for i in range(h):
    element = input()
    donut_box.append(list(element))
count = 0
for i, row in enumerate(donut_box):
    for j, element in enumerate(row):
        try:
            if element == ".":
                if donut_box[i][j-1] == "#" and donut_box[i][j+1] == "#" and donut_box[i-1][j-1] == "#" and donut_box[i-1][j] == "#" and donut_box[i-1][j+1] == "#" and donut_box[i+1][j-1] == "#" and donut_box[i+1][j] == "#" and donut_box[i+1][j+1] == "#":
                    count += 1
        except:
            pass

print(count)