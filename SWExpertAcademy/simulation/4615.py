from collections import deque
T = int(input())
data = []
for _ in range(T):
    n, m = map(int, input().split())
    strategy = deque([])
    for __ in range(m):
        tmp = list(map(int, input().split()))
        strategy.append((tmp[0] - 1, tmp[1] - 1, tmp[2]))
    data.append((n, m, strategy))


def check(location_x, location_y, direction1, direction2, color1, color2):
    location_x += direction1
    location_y += direction2
    while True:
        if not 0 <= location_x < n: return False
        elif not 0 <= location_y < n: return False
        elif board[location_x][location_y] == color2:
            location_x += direction1
            location_y += direction2
            continue
        elif board[location_x][location_y] == 100:
            return False
        elif board[location_x][location_y] == color1:
            return True


def change_board(strategy):
    if strategy[2] == 1:
        color1, color2 = "B", "W"
    else:
        color1, color2 = "W", "B"
    for dx, dy in moves:
        nx, ny = strategy[0], strategy[1]
        board[nx][ny] = color1
        what = check(nx, ny, dx, dy, color1, color2)
        if what:
            while True:
                nx += dx
                ny += dy
                if not 0 <= nx < n: break
                if not 0 <= ny < n: break
                if board[nx][ny] == color2:
                    board[nx][ny] = color1
                else:
                    break


def sol(case):
    global board, moves, n, m, strategies, strategy
    n, m, strategies = case
    board = [[100] * n for _ in range(n)]

    board[n // 2 - 1][n // 2 - 1] = "W"
    board[n // 2 - 1][n // 2] = "B"
    board[n // 2][n // 2 - 1] = "B"
    board[n // 2][n // 2] = "W"

    moves = [(1, 0), (0, 1), (-1, 0), (0, -1),
             (1, 1), (-1, 1), (1, -1), (-1, -1)]

    while strategies:
        strategy = strategies.popleft()
        change_board(strategy)

    black_count = 0
    white_count = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == "W":
                white_count += 1
            elif board[i][j] == "B":
                black_count += 1

    return black_count, white_count


for i, case in enumerate(data):
    result = sol(case)
    print("#%s" % (i + 1), result[0], result[1])

