import copy
n, m = map(int, input().split())
board = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    board.append(tmp)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
moves = [0, 4, 2, 4, 4, 1]  # 맨 앞에 0은 인덱스를 편하게 하기 위해서 추가
cctv = []
cctv_kinds = []
for x in range(n):
    for y in range(m):
        if board[x][y] not in (0, 6):
            cctv.append((x, y))
            cctv_kinds.append(board[x][y])
            board[x][y] = 7


def watch(loc_x, loc_y, direction, field):
    dx, dy = direction
    step = 1
    while True:
        nx, ny = loc_x + step * dx, loc_y + step * dy
        if not 0 <= nx < n: break
        if not 0 <= ny < m: break
        if field[nx][ny] == 6: break
        field[nx][ny] = 7
        step += 1


def DFS(kinds, visit=[], depth=0):
    if len(visit) == len(kinds):
        yield visit
    else:
        for i in range(moves[kinds[depth]]):
            visit.append(i)
            yield from DFS(kinds, visit, depth+1)
            visit.pop()


minimum = n * m
for direction_kinds in DFS(cctv_kinds):
    board_copy = copy.deepcopy(board)
    for cctv_loc, cctv_kind, toward in zip(cctv, cctv_kinds, direction_kinds):
        if cctv_kind == 1:
            direction = directions[toward]
            watch(cctv_loc[0], cctv_loc[1], direction, board_copy)
        elif cctv_kind == 2:
            direction = [directions[toward], directions[(toward + 2) % 4]]
            for direc in direction:
                watch(cctv_loc[0], cctv_loc[1], direc, board_copy)
        elif cctv_kind == 3:
            direction = [directions[toward], directions[(toward + 1) % 4]]
            for direc in direction:
                watch(cctv_loc[0], cctv_loc[1], direc, board_copy)
        elif cctv_kind == 4:
            direction = [directions[toward], directions[(toward + 1) % 4], directions[(toward + 2) % 4]]
            for direc in direction:
                watch(cctv_loc[0], cctv_loc[1], direc, board_copy)
        else:
            for direc in directions:
                watch(cctv_loc[0], cctv_loc[1], direc, board_copy)

    count = 0
    for x in range(n):
        for y in range(m):
            if board_copy[x][y] == 0:
                count += 1
    if minimum > count:
        minimum = count

    board_copy = copy.deepcopy(board)

print(minimum)
