def combinations(arr, m, visit=[]):
    if len(visit) == m:
        yield visit
    else:
        for i in range(len(arr)):
            visit.append(arr[i])
            yield from combinations(arr[i+1:], m, visit)
            visit.pop()


n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
houses = []
chicken_stores = []

for x in range(n):
    for y in range(n):
        if board[x][y] == 0:
            continue
        elif board[x][y] == 1:
            houses.append((x, y))
        else:
            chicken_stores.append((x, y))


result = 10000000000
for candi_chicken in combinations(chicken_stores, m):
    total = 0
    for x, y in houses:
        chicken_length = 10000000
        for cx, cy in candi_chicken:
            length = abs(x - cx) + abs(y - cy)
            if chicken_length > length:
                chicken_length = length
        total += chicken_length
        if total > result:
            break
    if result > total:
        result = total

print(result)
