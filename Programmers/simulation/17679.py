check = [(0, 0), (0, 1), (1, 0), (1, 1)]


def checker1(x, y, board):
    current = board[x][y]
    for dx, dy in check:
        if current != board[x+dx][y+dy]:
            return False
    return True


def checker(m, n, board):
    points = []
    for x in range(m-1):
        for y in range(n-1):
            if checker1(x, y, board):
                points.append((x, y))
    return points


def remove(points, board):
    for x, y in points:
        for dx, dy in check:
            board[x+dx][y+dy] = None


def move(m, n, board):
    new_board = []
    for y in range(n):
        new_line = []
        for x in range(m):
            if board[x][y] is not None:
                new_line.append(board[x][y])
        if len(new_line) < m:
            new_line = [y] * (m - len(new_line)) + new_line
        new_board.append(new_line)
    result_board = []
    for line in zip(*new_board):
        result_board.append(list(line))
    return result_board


def solution(m, n, board):
    board = [list(line) for line in board]
    while True:
        points = checker(m, n, board)
        if not points:
            break
        else:
            remove(points, board)
            board = move(m, n, board)

    count = 0
    for x in range(m):
        for y in range(n):
            if str(board[x][y]) not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                count += 1
    return count
