import collections
deque = collections.deque
n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
movements = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]


def day():
    check = [[False] * n for _ in range(n)]
    union = []
    for i in range(n):
        for j in range(n):
            if check[i][j]: continue
            queue = deque([(i, j)])
            visit = [(i, j)]
            while queue:
                x, y = queue.popleft()
                check[x][y] = True
                population = board[x][y]
                for dx, dy in movements:
                    nx, ny = x + dx, y + dy
                    if not 0 <= nx < n: continue
                    if not 0 <= ny < n: continue
                    if not l <= abs(board[nx][ny] - population) <= r: continue
                    if (nx, ny) in visit: continue
                    queue.append((nx, ny))
                    visit.append((nx, ny))
            union.append(visit)

    # print(union)

    change = False
    for unit in union:
        if len(unit) == 1: continue
        sum_population = 0
        for x, y in unit:
            sum_population += board[x][y]
        mean_population = sum_population // len(unit)
        for x, y in unit:
            board[x][y] = mean_population
        change = True
    # print(board)
    return change


count = 0
while True:
    if day():
        count += 1
    else:
        break

print(count)
