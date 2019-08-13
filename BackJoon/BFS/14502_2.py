import itertools
import collections
combinations = itertools.combinations
deque = collections.deque
movements = ((0, 1), (1, 0), (-1, 0), (0, -1))

n, m = map(int, input().split())
board = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    board.append(tmp)

candidates = []
virus = deque([])
for x in range(n):
    for y in range(m):
        if board[x][y] == 0:
            candidates.append((x, y))
        elif board[x][y] == 2:
            virus.append((x, y))

n_safe_zone = len(candidates)
n_safe_zone_origin = n_safe_zone
maximum = 0
for candi in combinations(candidates, 3):
    new_virus = []
    for x, y in candi:
        board[x][y] = 1
    virus_origin = virus.copy()
    while virus:
        current_x, current_y = virus.popleft()
        for dx, dy in movements:
            nx, ny = current_x + dx, current_y + dy
            if not 0 <= nx < n: continue
            if not 0 <= ny < m: continue
            if board[nx][ny] != 0: continue
            n_safe_zone -= 1
            board[nx][ny] = 2
            virus.append((nx, ny))
            new_virus.append((nx, ny))

    if maximum < (n_safe_zone - 3):
        maximum = (n_safe_zone - 3)

    virus = virus_origin.copy()
    for x, y in new_virus:
        board[x][y] = 0
    for x, y in candi:
        board[x][y] = 0
    n_safe_zone = n_safe_zone_origin

print(maximum)
