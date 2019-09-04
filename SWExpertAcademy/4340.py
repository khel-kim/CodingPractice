pipe1 = (1, 2)
pipe2 = (3, 4, 5, 6)
T = int(input())
data = [None] * T
for t in range(T):
    n = int(input())
    data[t] = n, [list(map(int, input().split())) for _ in range(n)]


def sol(case):
    n, board = case
    route_board = [False] * (n * n)
    check_board = []
    for __ in range(n):
        check_board.append([])
        for ___ in range(n):
            check_board[-1].append([])

    route_board[-1] = True
    dp_dic = {1: [(n-1, n-1, (0, -1), route_board)]}
    check_board[n-1][n-1].append((0, -1))

    result = 0
    for depth in range(2, n * n + 1):
        dp_dic[depth] = []
        for x, y, direction, route in dp_dic[depth - 1]:
            if board[x][y] in pipe1:
                moves = [direction]
            else:
                if direction in ((0, 1), (0, -1)):
                    moves = ((-1, 0), (1, 0))
                else:
                    moves = ((0, -1), (0, 1))
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if not 0 <= nx < n: continue
                if not 0 <= ny < n: continue
                if board[nx][ny] == 0: continue
                if (dx, dy) in check_board[nx][ny]: continue
                if route[nx * n + ny]: continue

                if (nx, ny) == (0, 0):
                    if board[nx][ny] in pipe1 and (dx, dy) == (0, -1):
                        result = depth
                    if board[nx][ny] not in pipe1 and (dx, dy) == (-1, 0):
                        result = depth
                if result:
                    return result
                route[nx * n + ny] = True
                check_board[nx][ny].append((dx, dy))
                dp_dic[depth].append((nx, ny, (dx, dy), route[:]))
                route[nx * n + ny] = False


def sol2(case):
    n, board = case
    route_board = [False] * (n * n)
    check_board = []
    for __ in range(n):
        check_board.append([])
        for ___ in range(n):
            check_board[-1].append([])

    route_board[0] = True
    dp_dic = {1: [(0, 0, (0, 1), route_board)]}
    check_board[0][0].append((0, 1))

    result = 0
    for depth in range(2, n * n + 1):
        dp_dic[depth] = []
        for x, y, direction, route in dp_dic[depth - 1]:
            if board[x][y] in pipe1:
                moves = [direction]
            else:
                if direction in ((0, 1), (0, -1)):
                    moves = ((1, 0), (-1, 0))
                else:
                    moves = ((0, 1), (0, -1))
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if not 0 <= nx < n: continue
                if not 0 <= ny < n: continue
                if board[nx][ny] == 0: continue
                if (dx, dy) in check_board[nx][ny]: continue
                if route[nx * n + ny]: continue

                if (nx, ny) == (n-1, n-1):
                    if board[nx][ny] in pipe1 and (dx, dy) == (0, 1):
                        result = depth
                    if board[nx][ny] not in pipe1 and (dx, dy) == (1, 0):
                        result = depth
                if result:
                    return result
                route[nx * n + ny] = True
                check_board[nx][ny].append((dx, dy))
                dp_dic[depth].append((nx, ny, (dx, dy), route.copy()))
                route[nx * n + ny] = False


for num, case in enumerate(data):
    result1 = sol(case)
    result2 = sol2(case)
    print("#%s" % (num + 1), min(result1, result2))

"""
6
5
1 4 3 1 4 
0 6 4 0 2 
0 0 2 0 2 
0 0 6 3 5 
0 0 0 6 1 
5
1 2 3 0 0 
0 5 6 4 3 
3 6 5 4 3 
2 4 3 2 5 
5 2 5 3 6 
10
1 1 1 2 2 1 2 2 2 6 
3 1 1 1 1 1 1 1 2 4 
6 1 2 2 1 2 2 1 2 6 
6 1 2 1 2 1 2 1 1 4 
4 1 1 2 1 1 2 1 1 5 
3 1 2 2 1 1 1 1 1 6 
4 2 1 2 2 2 2 2 2 4 
3 2 1 2 1 2 2 2 1 6 
1 0 0 5 3 3 0 1 0 2 
3 2 2 2 1 1 1 1 1 1 
10
1 4 4 2 2 3 6 1 4 1 
0 2 5 4 4 6 3 3 5 3 
5 6 3 6 4 1 3 3 4 2 
1 2 1 4 2 1 5 6 6 0 
3 2 5 6 4 0 6 1 4 6 
0 3 2 0 6 3 5 3 0 2 
0 1 0 0 0 6 3 0 5 2 
0 4 5 2 3 1 2 2 2 4 
0 2 5 0 2 6 1 6 3 3 
0 0 4 0 5 6 0 5 4 6 
15
1 3 6 2 2 6 6 0 1 0 0 3 0 5 0 
0 4 4 0 5 4 0 0 0 3 0 3 0 0 3 
6 0 0 2 2 2 4 0 0 0 0 0 0 0 0 
0 6 1 3 6 5 0 6 0 2 0 0 0 3 1 
4 6 2 2 0 3 4 0 0 0 4 2 0 0 0 
0 5 0 2 3 6 0 0 2 0 3 6 0 4 0 
0 0 0 1 0 0 4 0 0 1 5 2 0 1 0 
5 1 1 4 5 4 6 3 0 2 0 0 2 4 1 
1 0 0 0 4 0 5 3 0 0 5 1 3 5 4 
1 0 5 3 0 0 5 4 5 5 0 0 0 1 1 
6 5 6 0 0 0 0 2 4 0 6 2 5 2 1 
5 5 0 1 0 0 0 0 0 0 0 5 3 6 2 
1 5 1 4 3 3 4 1 0 6 1 4 6 5 2 
6 3 0 5 3 1 5 3 3 3 4 4 1 4 2 
5 0 6 0 5 5 3 4 4 6 0 1 6 4 6
50
1 4 4 2 2 3 6 1 4 1 1 4 4 2 2 3 6 1 4 1 1 4 4 2 2 3 6 1 4 1 1 4 4 2 2 3 6 1 4 1 1 4 4 2 2 3 6 1 4 1 
0 2 5 4 4 6 3 3 5 3 0 2 5 4 4 6 3 3 5 3 0 2 5 4 4 6 3 3 5 3 0 2 5 4 4 6 3 3 5 3 0 2 5 4 4 6 3 3 5 3 
5 6 3 6 4 1 3 3 4 2 5 6 3 6 4 1 3 3 4 2 5 6 3 6 4 1 3 3 4 2 5 6 3 6 4 1 3 3 4 2 5 6 3 6 4 1 3 3 4 2 
1 2 1 4 2 1 5 6 6 0 1 2 1 4 2 1 5 6 6 0 1 2 1 4 2 1 5 6 6 0 1 2 1 4 2 1 5 6 6 0 1 2 1 4 2 1 5 6 6 0 
3 2 5 6 4 0 6 1 4 6 3 2 5 6 4 0 6 1 4 6 3 2 5 6 4 0 6 1 4 6 3 2 5 6 4 0 6 1 4 6 3 2 5 6 4 0 6 1 4 6 
0 3 2 0 6 3 5 3 0 2 0 3 2 0 6 3 5 3 0 2 0 3 2 0 6 3 5 3 0 2 0 3 2 0 6 3 5 3 0 2 0 3 2 0 6 3 5 3 0 2 
0 1 0 0 0 6 3 0 5 2 0 1 0 0 0 6 3 0 5 2 0 1 0 0 0 6 3 0 5 2 0 1 0 0 0 6 3 0 5 2 0 1 0 0 0 6 3 0 5 2 
0 4 5 2 3 1 2 2 2 4 0 4 5 2 3 1 2 2 2 4 0 4 5 2 3 1 2 2 2 4 0 4 5 2 3 1 2 2 2 4 0 4 5 2 3 1 2 2 2 4 
0 2 5 0 2 6 1 6 3 3 0 2 5 0 2 6 1 6 3 3 0 2 5 0 2 6 1 6 3 3 0 2 5 0 2 6 1 6 3 3 0 2 5 0 2 6 1 6 3 3 
0 0 4 0 5 6 0 5 4 6 0 0 4 0 5 6 0 5 4 6 0 0 4 0 5 6 0 5 4 6 0 0 4 0 5 6 0 5 4 6 0 0 4 0 5 6 0 5 4 6 
1 4 4 2 2 3 6 1 4 1 1 4 4 2 2 3 6 1 4 1 1 4 4 2 2 3 6 1 4 1 1 4 4 2 2 3 6 1 4 1 1 4 4 2 2 3 6 1 4 1 
0 2 5 4 4 6 3 3 5 3 0 2 5 4 4 6 3 3 5 3 0 2 5 4 4 6 3 3 5 3 0 2 5 4 4 6 3 3 5 3 0 2 5 4 4 6 3 3 5 3 
5 6 3 6 4 1 3 3 4 2 5 6 3 6 4 1 3 3 4 2 5 6 3 6 4 1 3 3 4 2 5 6 3 6 4 1 3 3 4 2 5 6 3 6 4 1 3 3 4 2 
1 2 1 4 2 1 5 6 6 0 1 2 1 4 2 1 5 6 6 0 1 2 1 4 2 1 5 6 6 0 1 2 1 4 2 1 5 6 6 0 1 2 1 4 2 1 5 6 6 0 
3 2 5 6 4 0 6 1 4 6 3 2 5 6 4 0 6 1 4 6 3 2 5 6 4 0 6 1 4 6 3 2 5 6 4 0 6 1 4 6 3 2 5 6 4 0 6 1 4 6 
0 3 2 0 6 3 5 3 0 2 0 3 2 0 6 3 5 3 0 2 0 3 2 0 6 3 5 3 0 2 0 3 2 0 6 3 5 3 0 2 0 3 2 0 6 3 5 3 0 2 
0 1 0 0 0 6 3 0 5 2 0 1 0 0 0 6 3 0 5 2 0 1 0 0 0 6 3 0 5 2 0 1 0 0 0 6 3 0 5 2 0 1 0 0 0 6 3 0 5 2 
0 4 5 2 3 1 2 2 2 4 0 4 5 2 3 1 2 2 2 4 0 4 5 2 3 1 2 2 2 4 0 4 5 2 3 1 2 2 2 4 0 4 5 2 3 1 2 2 2 4 
0 2 5 0 2 6 1 6 3 3 0 2 5 0 2 6 1 6 3 3 0 2 5 0 2 6 1 6 3 3 0 2 5 0 2 6 1 6 3 3 0 2 5 0 2 6 1 6 3 3 
0 0 4 0 5 6 0 5 4 6 0 0 4 0 5 6 0 5 4 6 0 0 4 0 5 6 0 5 4 6 0 0 4 0 5 6 0 5 4 6 0 0 4 0 5 6 0 5 4 6 
1 4 4 2 2 3 6 1 4 1 1 4 4 2 2 3 6 1 4 1 1 4 4 2 2 3 6 1 4 1 1 4 4 2 2 3 6 1 4 1 1 4 4 2 2 3 6 1 4 1 
0 2 5 4 4 6 3 3 5 3 0 2 5 4 4 6 3 3 5 3 0 2 5 4 4 6 3 3 5 3 0 2 5 4 4 6 3 3 5 3 0 2 5 4 4 6 3 3 5 3 
5 6 3 6 4 1 3 3 4 2 5 6 3 6 4 1 3 3 4 2 5 6 3 6 4 1 3 3 4 2 5 6 3 6 4 1 3 3 4 2 5 6 3 6 4 1 3 3 4 2 
1 2 1 4 2 1 5 6 6 0 1 2 1 4 2 1 5 6 6 0 1 2 1 4 2 1 5 6 6 0 1 2 1 4 2 1 5 6 6 0 1 2 1 4 2 1 5 6 6 0 
3 2 5 6 4 0 6 1 4 6 3 2 5 6 4 0 6 1 4 6 3 2 5 6 4 0 6 1 4 6 3 2 5 6 4 0 6 1 4 6 3 2 5 6 4 0 6 1 4 6 
0 3 2 0 6 3 5 3 0 2 0 3 2 0 6 3 5 3 0 2 0 3 2 0 6 3 5 3 0 2 0 3 2 0 6 3 5 3 0 2 0 3 2 0 6 3 5 3 0 2 
0 1 0 0 0 6 3 0 5 2 0 1 0 0 0 6 3 0 5 2 0 1 0 0 0 6 3 0 5 2 0 1 0 0 0 6 3 0 5 2 0 1 0 0 0 6 3 0 5 2 
0 4 5 2 3 1 2 2 2 4 0 4 5 2 3 1 2 2 2 4 0 4 5 2 3 1 2 2 2 4 0 4 5 2 3 1 2 2 2 4 0 4 5 2 3 1 2 2 2 4 
0 2 5 0 2 6 1 6 3 3 0 2 5 0 2 6 1 6 3 3 0 2 5 0 2 6 1 6 3 3 0 2 5 0 2 6 1 6 3 3 0 2 5 0 2 6 1 6 3 3 
0 0 4 0 5 6 0 5 4 6 0 0 4 0 5 6 0 5 4 6 0 0 4 0 5 6 0 5 4 6 0 0 4 0 5 6 0 5 4 6 0 0 4 0 5 6 0 5 4 6 
1 4 4 2 2 3 6 1 4 1 1 4 4 2 2 3 6 1 4 1 1 4 4 2 2 3 6 1 4 1 1 4 4 2 2 3 6 1 4 1 1 4 4 2 2 3 6 1 4 1 
0 2 5 4 4 6 3 3 5 3 0 2 5 4 4 6 3 3 5 3 0 2 5 4 4 6 3 3 5 3 0 2 5 4 4 6 3 3 5 3 0 2 5 4 4 6 3 3 5 3 
5 6 3 6 4 1 3 3 4 2 5 6 3 6 4 1 3 3 4 2 5 6 3 6 4 1 3 3 4 2 5 6 3 6 4 1 3 3 4 2 5 6 3 6 4 1 3 3 4 2 
1 2 1 4 2 1 5 6 6 0 1 2 1 4 2 1 5 6 6 0 1 2 1 4 2 1 5 6 6 0 1 2 1 4 2 1 5 6 6 0 1 2 1 4 2 1 5 6 6 0 
3 2 5 6 4 0 6 1 4 6 3 2 5 6 4 0 6 1 4 6 3 2 5 6 4 0 6 1 4 6 3 2 5 6 4 0 6 1 4 6 3 2 5 6 4 0 6 1 4 6 
0 3 2 0 6 3 5 3 0 2 0 3 2 0 6 3 5 3 0 2 0 3 2 0 6 3 5 3 0 2 0 3 2 0 6 3 5 3 0 2 0 3 2 0 6 3 5 3 0 2 
0 1 0 0 0 6 3 0 5 2 0 1 0 0 0 6 3 0 5 2 0 1 0 0 0 6 3 0 5 2 0 1 0 0 0 6 3 0 5 2 0 1 0 0 0 6 3 0 5 2 
0 4 5 2 3 1 2 2 2 4 0 4 5 2 3 1 2 2 2 4 0 4 5 2 3 1 2 2 2 4 0 4 5 2 3 1 2 2 2 4 0 4 5 2 3 1 2 2 2 4 
0 2 5 0 2 6 1 6 3 3 0 2 5 0 2 6 1 6 3 3 0 2 5 0 2 6 1 6 3 3 0 2 5 0 2 6 1 6 3 3 0 2 5 0 2 6 1 6 3 3 
0 0 4 0 5 6 0 5 4 6 0 0 4 0 5 6 0 5 4 6 0 0 4 0 5 6 0 5 4 6 0 0 4 0 5 6 0 5 4 6 0 0 4 0 5 6 0 5 4 6 
1 4 4 2 2 3 6 1 4 1 1 4 4 2 2 3 6 1 4 1 1 4 4 2 2 3 6 1 4 1 1 4 4 2 2 3 6 1 4 1 1 4 4 2 2 3 6 1 4 1 
0 2 5 4 4 6 3 3 5 3 0 2 5 4 4 6 3 3 5 3 0 2 5 4 4 6 3 3 5 3 0 2 5 4 4 6 3 3 5 3 0 2 5 4 4 6 3 3 5 3 
5 6 3 6 4 1 3 3 4 2 5 6 3 6 4 1 3 3 4 2 5 6 3 6 4 1 3 3 4 2 5 6 3 6 4 1 3 3 4 2 5 6 3 6 4 1 3 3 4 2 
1 2 1 4 2 1 5 6 6 0 1 2 1 4 2 1 5 6 6 0 1 2 1 4 2 1 5 6 6 0 1 2 1 4 2 1 5 6 6 0 1 2 1 4 2 1 5 6 6 0 
3 2 5 6 4 0 6 1 4 6 3 2 5 6 4 0 6 1 4 6 3 2 5 6 4 0 6 1 4 6 3 2 5 6 4 0 6 1 4 6 3 2 5 6 4 0 6 1 4 6 
0 3 2 0 6 3 5 3 0 2 0 3 2 0 6 3 5 3 0 2 0 3 2 0 6 3 5 3 0 2 0 3 2 0 6 3 5 3 0 2 0 3 2 0 6 3 5 3 0 2 
0 1 0 0 0 6 3 0 5 2 0 1 0 0 0 6 3 0 5 2 0 1 0 0 0 6 3 0 5 2 0 1 0 0 0 6 3 0 5 2 0 1 0 0 0 6 3 0 5 2 
0 4 5 2 3 1 2 2 2 4 0 4 5 2 3 1 2 2 2 4 0 4 5 2 3 1 2 2 2 4 0 4 5 2 3 1 2 2 2 4 0 4 5 2 3 1 2 2 2 4 
0 2 5 0 2 6 1 6 3 3 0 2 5 0 2 6 1 6 3 3 0 2 5 0 2 6 1 6 3 3 0 2 5 0 2 6 1 6 3 3 0 2 5 0 2 6 1 6 3 3 
0 0 4 0 5 6 0 5 4 6 0 0 4 0 5 6 0 5 4 6 0 0 4 0 5 6 0 5 4 6 0 0 4 0 5 6 0 5 4 6 0 0 4 0 5 6 0 5 4 6 
"""