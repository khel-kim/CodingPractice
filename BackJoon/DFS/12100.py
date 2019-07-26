import copy

n = int(input())
board = []
for _ in range(n):
    tmp_list = list(map(int, input().split()))
    board.append(tmp_list)


def push_left(field):
    for x in range(n):
        while True:
            tmp = field[x].copy()
            for y in range(1, n):
                if field[x][y - 1] != 0: continue
                field[x][y - 1], field[x][y] = field[x][y], field[x][y - 1]
            if tmp != field[x]: continue
            else:
                break
    return field


def sum_left(field):
    for x in range(n):
        for y in range(n - 1):
            if field[x][y] != field[x][y + 1]: continue
            field[x][y] *= 2
            field[x][y + 1] = 0
    return field


def move_left(field):
    field = push_left(field)
    field = sum_left(field)
    return push_left(field)


def push_right(field):
    for x in range(n):
        while True:
            tmp = field[x].copy()
            for y in range(n - 1):
                if field[x][y + 1] != 0: continue
                field[x][y + 1], field[x][y] = field[x][y], field[x][y + 1]
            if tmp != field[x]: continue
            else:
                break
    return field


def sum_right(field):
    for x in range(n):
        for y in range(n - 1, 0, -1):
            if field[x][y] != field[x][y - 1]: continue
            field[x][y] *= 2
            field[x][y - 1] = 0
    return field


def move_right(field):
    field = push_right(field)
    field = sum_right(field)
    return push_right(field)


def push_up(field):
    tmp_field = [list(arr) for arr in zip(*field)]
    tmp_field = push_left(tmp_field)
    field = [list(arr) for arr in zip(*tmp_field)]
    return field


def sum_up(field):
    tmp_field = [list(arr) for arr in zip(*field)]
    tmp_field = sum_left(tmp_field)
    field = [list(arr) for arr in zip(*tmp_field)]
    return field


def move_up(field):
    field = push_up(field)
    field = sum_up(field)
    return push_up(field)


def push_down(field):
    tmp_field = [list(arr) for arr in zip(*field)]
    tmp_field = push_right(tmp_field)
    field = [list(arr) for arr in zip(*tmp_field)]
    return field


def sum_down(field):
    tmp_field = [list(arr) for arr in zip(*field)]
    tmp_field = sum_right(tmp_field)
    field = [list(arr) for arr in zip(*tmp_field)]
    return field


def move_down(field):
    field = push_down(field)
    field = sum_down(field)
    return push_down(field)


def move(field, method):
    if method == "left":
        return move_left(field)
    elif method == "right":
        return move_right(field)
    elif method == "up":
        return move_up(field)
    else:
        return move_down(field)


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


movements = ["left",
             "right",
             "up",
             "down",]
maximum = 0
for candi in DFS(board):
    for x in range(n):
        for y in range(n):
            if maximum < candi[x][y]:
                maximum = candi[x][y]
print(maximum)
