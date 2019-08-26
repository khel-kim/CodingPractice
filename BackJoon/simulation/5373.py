T = int(input())
data = []
for _ in range(T):
    n = int(input())
    rotation = input().split()
    data.append((n, rotation))


def rotation_clock(surface):
    new_surface = []
    for _ in range(3):
        new_surface.append([None] * 3)
    for i in range(3):
        line = surface[i]
        for x in range(3):
            new_surface[x][2 - i] = line[x]
    return new_surface


def rotation_counter_clock(surface):
    new_surface = []
    for _ in range(3):
        new_surface.append([None] * 3)
    for i in range(3):
        line = surface[i]
        for x in range(3):
            new_surface[x][i] = line[2 - x]
    return new_surface


def sol(case):
    board = [
        [["w"] * 3, ["w"] * 3, ["w"] * 3],  # U, index = 0
        [["y"] * 3, ["y"] * 3, ["y"] * 3],  # D, index = 1
        [["r"] * 3, ["r"] * 3, ["r"] * 3],  # F, index = 2
        [["o"] * 3, ["o"] * 3, ["o"] * 3],  # B, index = 3
        [["g"] * 3, ["g"] * 3, ["g"] * 3],  # L, index = 4
        [["b"] * 3, ["b"] * 3, ["b"] * 3],  # R, index = 5
    ]
    n, rotations = case

    def U(method):
        surface = board[0]
        tmp_line = board[2][0].copy()
        if method == "+":
            board[0] = rotation_clock(surface)
            board[2][0] = board[5][0]
            board[5][0] = board[3][0]
            board[3][0] = board[4][0]
            board[4][0] = tmp_line
        elif method == "-":
            board[0] = rotation_counter_clock(surface)
            board[2][0] = board[4][0]
            board[4][0] = board[3][0]
            board[3][0] = board[5][0]
            board[5][0] = tmp_line

    def D(method):  # 바닥의 경우 회전을 반대로 해야함
        surface = board[1]
        tmp_line = board[2][2].copy()
        if method == "+":
            board[1] = rotation_counter_clock(surface)
            board[2][2] = board[4][2]
            board[4][2] = board[3][2]
            board[3][2] = board[5][2]
            board[5][2] = tmp_line
        elif method == "-":
            board[1] = rotation_clock(surface)
            board[2][2] = board[5][2]
            board[5][2] = board[3][2]
            board[3][2] = board[4][2]
            board[4][2] = tmp_line

    def F(method):
        surface = board[2]
        tmp_line = board[0][2].copy()
        if method == "+":
            board[2] = rotation_clock(surface)
            board[0][2] = [board[4][2][2], board[4][1][2], board[4][0][2]]
            board[4][0][2], board[4][1][2], board[4][2][2] = board[1][2]
            board[1][2] = [board[5][2][0], board[5][1][0], board[5][0][0]]
            board[5][0][0], board[5][1][0], board[5][2][0] = tmp_line
        elif method == "-":
            board[2] = rotation_counter_clock(surface)
            board[0][2] = [board[5][0][0], board[5][1][0], board[5][2][0]]
            board[5][0][0], board[5][1][0], board[5][2][0] = board[1][2][::-1]
            board[1][2] = [board[4][0][2], board[4][1][2], board[4][2][2]]
            board[4][0][2], board[4][1][2], board[4][2][2] = tmp_line[::-1]

    def B(method):
        surface = board[3]
        tmp_line = board[0][0].copy()
        if method == "+":
            board[3] = rotation_clock(surface)
            board[0][0] = [board[5][0][2], board[5][1][2], board[5][2][2]]
            board[5][0][2], board[5][1][2], board[5][2][2] = board[1][0][::-1]
            board[1][0] = [board[4][0][0], board[4][1][0], board[4][2][0]]
            board[4][0][0], board[4][1][0], board[4][2][0] = tmp_line[::-1]
        elif method == "-":
            board[3] = rotation_counter_clock(surface)
            board[0][0] = [board[4][2][0], board[4][1][0], board[4][0][0]]
            board[4][0][0], board[4][1][0], board[4][2][0] = board[1][0]
            board[1][0] = [board[5][2][2], board[5][1][2], board[5][0][2]]
            board[5][0][2], board[5][1][2], board[5][2][2] = tmp_line

    def L(method):
        surface = board[4]
        tmp_line = [board[0][0][0], board[0][1][0], board[0][2][0]]
        if method == "+":
            board[4] = rotation_clock(surface)
            board[0][0][0], board[0][1][0], board[0][2][0] = [board[3][2][2], board[3][1][2], board[3][0][2]]
            board[3][0][2], board[3][1][2], board[3][2][2] = [board[1][0][0], board[1][1][0], board[1][2][0]]
            board[1][0][0], board[1][1][0], board[1][2][0] = [board[2][2][0], board[2][1][0], board[2][0][0]]
            board[2][0][0], board[2][1][0], board[2][2][0] = tmp_line
        elif method == "-":
            board[4] = rotation_counter_clock(surface)
            board[0][0][0], board[0][1][0], board[0][2][0] = [board[2][0][0], board[2][1][0], board[2][2][0]]
            board[2][0][0], board[2][1][0], board[2][2][0] = [board[1][2][0], board[1][1][0], board[1][0][0]]
            board[1][0][0], board[1][1][0], board[1][2][0] = [board[3][0][2], board[3][1][2], board[3][2][2]]
            board[3][0][2], board[3][1][2], board[3][2][2] = tmp_line[::-1]

    def R(method):
        surface = board[5]
        tmp_line = [board[0][0][2], board[0][1][2], board[0][2][2]]
        if method == "+":
            board[5] = rotation_clock(surface)
            board[0][0][2], board[0][1][2], board[0][2][2] = [board[2][0][2], board[2][1][2], board[2][2][2]]
            board[2][0][2], board[2][1][2], board[2][2][2] = [board[1][2][2], board[1][1][2], board[1][0][2]]
            board[1][0][2], board[1][1][2], board[1][2][2] = [board[3][0][0], board[3][1][0], board[3][2][0]]
            board[3][0][0], board[3][1][0], board[3][2][0] = tmp_line[::-1]
        elif method == "-":
            board[5] = rotation_counter_clock(surface)
            board[0][0][2], board[0][1][2], board[0][2][2] = [board[3][2][0], board[3][1][0], board[3][0][0]]
            board[3][0][0], board[3][1][0], board[3][2][0] = [board[1][0][2], board[1][1][2], board[1][2][2]]
            board[1][0][2], board[1][1][2], board[1][2][2] = [board[2][2][2], board[2][1][2], board[2][0][2]]
            board[2][0][2], board[2][1][2], board[2][2][2] = tmp_line

    for string in rotations:
        direction, method = string[0], string[1]
        if direction == "U":
            U(method)
        elif direction == "D":
            D(method)
        elif direction == "F":
            F(method)
        elif direction == "B":
            B(method)
        elif direction == "L":
            L(method)
        elif direction == "R":
            R(method)
    result = ""
    for line in board[0]:
        result += "".join(line) + "\n"
    return result[:-1]


for case in data:
    print(sol(case))
