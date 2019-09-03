pipe1 = (1, 2)
set1 = ((0, 1), (0, -1))
set2 = ((1, 0), (-1, 0))
check_board = [[False] * 51 for _ in range(51)]


def DFS(visit, depth=1):
    global minimum
    if depth >= minimum - 3:
        return
    x, y, direction = visit[-1]
    if x == y == n-1:
        if board[x][y] in pipe1 and direction[0] == 0:
            if minimum > depth:
                minimum = depth
        elif board[x][y] not in pipe1 and direction[0] == 1:
            if minimum > depth:
                minimum = depth
    else:
        if board[x][y] in pipe1:
            moves = (direction,)
        else:
            moves = ((direction[1], direction[0]), (-1 * direction[1], -1 * direction[0]))

        for dx, dy in moves:
            if depth >= minimum - 4:
                return
            nx, ny = x + dx, y + dy
            if not 0 <= nx < n: continue
            if not 0 <= ny < n: continue
            if board[nx][ny] == 0: continue
            if check_board[nx][ny]:continue
            visit.append((nx, ny, (dx, dy)))
            check_board[nx][ny] = True
            DFS(visit, depth + 1)
            visit.pop()
            check_board[nx][ny] = False


T = int(input())
for t in range(T):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    minimum = 50 * 50
    DFS([(0, 0, (0, 1))])
    print("#%s" % (t + 1), minimum)
