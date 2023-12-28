def calculate_days(n, works):
    last_day = max(max(sublist) for sublist in works)
    days = [0] * (last_day + 1)

    for start, end in works:
        for day in range(start, end + 1):
            days[day] = 1


    max_days = 0
    current_streak = 0
    for day in days:
        if day == 1:
            current_streak += 1
            max_days = max(max_days, current_streak)
        else:
            current_streak = 0

    return max_days

n = int(input())
works = []

for _ in range(n):
    start, end = map(int, input().split())
    works.append((start, end))

print(calculate_days(n, works))