import itertools
combinations = itertools.combinations

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

chickens = []
houses = []
for x in range(n):
    for y in range(n):
        if board[x][y] == 2:
            chickens.append((x, y))
        if board[x][y] == 1:
            houses.append((x, y))

minimum_chicken_distance = 10000
for chicks in combinations(chickens, m):
    minimum_distance = 0
    for x, y in houses:
        minimum = 100000
        for r, s in chicks:
            tmp = abs(x - r) + abs(y - s)
            if minimum > tmp:
                minimum = tmp
        minimum_distance += minimum
    if minimum_chicken_distance > minimum_distance:
        minimum_chicken_distance = minimum_distance

print(minimum_chicken_distance)
