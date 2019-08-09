import copy

n = int(input())
board = []
for _ in range(n):
    tmp_list = list(map(int, input().split()))
    board.append(tmp_list)


def push_horizontal(field, direction):
    dx, dy = direction
    if dy == -1:
        range_from = 1
        range_to = n
    else:
        range_from = 0
        range_to = n-1
    for x in range(n):
        while True:
            tmp_line = field[x].copy()  # 현재 상태를 기억하기 위해
            for y in range(range_from, range_to):
                if field[x][y + dy] != 0: continue
                field[x][y + dy], field[x][y] = field[x][y], field[x][y + dy]
            if tmp_line != field[x]: continue
            else:
                break
    return field


def sum_horizontal(field, direction):
    dx, dy = direction
    if dy == -1:
        range_from = 0
        range_to = n - 1
        step = 1
    else:
        range_from = n - 1
        range_to = 0
        step = -1
    for x in range(n):
        for y in range(range_from, range_to, step):
            if field[x][y] != field[x][y - dy]: continue
            field[x][y] *= 2
            field[x][y - dy] = 0
    return field


def move_horizontal(field, direction):
    field = push_horizontal(field, direction)
    field = sum_horizontal(field, direction)
    return push_horizontal(field, direction)


def move_vertical(field, direction):
    dx, dy = direction
    if dx == 1:
        direction = (0, -1)  # left
    else:
        direction = (0, 1)  # right
    tmp_field = [list(arr) for arr in zip(*field)]
    tmp_field = push_horizontal(tmp_field, direction)
    tmp_field = sum_horizontal(tmp_field, direction)
    tmp_field = push_horizontal(tmp_field, direction)
    return [list(arr) for arr in zip(*tmp_field)]


def move(field, direction):
    if direction in ((0, -1), (0, 1)):
        return move_horizontal(field, direction)
    else:
        return move_vertical(field, direction)


def DFS(field, tmp=0):
    if tmp == 5:
        yield field
        return
    else:
        for movement in movements:
            original_field = copy.deepcopy(field)
            field = move(field, movement)
            yield from DFS(field, tmp=tmp+1)
            field = original_field


movements = [(0, 1),
             (0, -1),
             (1, 0),
             (-1, 0)]
maximum = 0
for candi in DFS(board):
    for x in range(n):
        for y in range(n):
            if maximum < candi[x][y]:
                maximum = candi[x][y]
print(maximum)
