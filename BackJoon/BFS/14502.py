import itertools
import collections
import copy
import pprint
pprint = pprint.pprint
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

maximum = 0
board_origin = copy.deepcopy(board)
for candi in combinations(candidates, 3):
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
            if (nx, ny) in virus: continue
            board[nx][ny] = 2
            virus.append((nx, ny))
    count = 0
    for x in range(n):
        for y in range(m):
            if board[x][y] == 0:
                count += 1
    if maximum < count:
        maximum = count
    virus = virus_origin.copy()
    board = copy.deepcopy(board_origin)
print(maximum)
