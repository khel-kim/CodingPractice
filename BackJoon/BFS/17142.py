import itertools
import collections
combinations = itertools.combinations
deque = collections.deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
check_board = [[False] * n for _ in range(n)]
movements = ((1, 0), (0, 1), (-1, 0), (0, -1))

virus = []
space = 0
for x in range(n):
    for y in range(n):
        if board[x][y] == 1:
            check_board[x][y] = True
        else:
            space += 1
            if board[x][y] == 2:
                virus.append((x, y))

minimum = 10000
if space - len(virus) == 0:
    minimum = 0
else:
    for active_virus in combinations(virus, m):
        # init
        remained_space = space - m
        queue = deque([])
        visit = []
        # inactive virus init
        inactive_virus = []
        for vir in virus:
            if vir not in active_virus:
                inactive_virus.append(vir)
            else:
                x, y = vir
                visit.append((x, y))
                check_board[x][y] = True
                queue.append((vir[0], vir[1], 0))
        # BFS
        last = queue[-1]
        while queue:
            x, y, depth = queue.popleft()
            for dx, dy in movements:
                nx, ny = x + dx, y + dy
                if not 0 <= nx < n: continue
                if not 0 <= ny < n: continue
                if check_board[nx][ny]: continue
                visit.append((nx, ny))
                queue.append((nx, ny, depth + 1))
                check_board[nx][ny] = True
                remained_space -= 1
            # tail check
            if last == (x, y, depth):
                if queue:
                    last = queue[-1]
                count = 0
                for p, q in inactive_virus:
                    if not check_board[p][q]:
                        count += 1
                if remained_space - count <= 0:
                    if minimum > depth + 1:
                        minimum = depth + 1
                    break
            # minimum check
            if depth >= minimum - 1:
                break
        # recover
        for x, y in visit:
            check_board[x][y] = False

if minimum == 10000:
    print(-1)
else:
    print(minimum)
