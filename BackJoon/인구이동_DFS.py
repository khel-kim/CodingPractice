import sys
limit = 3000
sys.setrecursionlimit(limit)

n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
moves = ((1, 0), (0, 1), (-1, 0), (0, -1))
change = True
count = 0


def dfs(x, y):
    global summation
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if not 0 <= nx < n: continue
        if not 0 <= ny < n: continue
        if check_board[nx][ny] is True: continue
        if l <= abs(board[x][y] - board[nx][ny]) <= r:
            check_board[nx][ny] = True
            visit.append((nx, ny))
            summation += board[nx][ny]
            dfs(nx, ny)


while change:
    change = False
    count += 1
    check_board = [[False] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if check_board[x][y] is True: continue
            check_board[x][y] = True
            visit = [(x, y)]
            summation = board[x][y]

            dfs(x, y)

            mean = summation // len(visit)
            for ux, uy in visit:
                board[ux][uy] = mean
            if len(visit) > 1:
                change = True
print(count-1)
