r, c, t = map(int, input().split())
movements = ((1, 0), (-1, 0), (0, 1), (0, -1))

purifier = []
dusts = []
board = []
for p in range(r):
    tmp = list(map(int, input().split()))
    for q in range(c):
        if tmp[q] == -1:
            purifier.append(p)
        elif tmp[q] != 0:
            dusts.append((p, q, tmp[q]))
    board.append(tmp)
x1, x2 = purifier

for _ in range(t):
    for x, y, dust in dusts:
        if dust < 5: continue
        else:
            dust //= 5
            for dx, dy in movements:
                nx, ny = x + dx, y + dy
                if not 0 <= nx < r: continue
                if not 0 <= ny < c: continue
                if board[nx][ny] == -1: continue
                board[nx][ny] += dust
                board[x][y] -= dust

    for i in range(x1 - 2, -1, -1):
        board[i + 1][0] = board[i][0]
    for i in range(x2 + 2, r):
        board[i - 1][0] = board[i][0]

    for j in range(1, c):
        board[0][j - 1] = board[0][j]
        board[r - 1][j - 1] = board[r - 1][j]

    for i in range(1, x1 + 1):
        board[i - 1][c - 1] = board[i][c - 1]
    for i in range(r - 2, x2 - 1, -1):
        board[i + 1][c - 1] = board[i][c - 1]

    for j in range(c - 2, 0, -1):
        board[x1][j + 1] = board[x1][j]
        board[x2][j + 1] = board[x2][j]
    board[x1][1] = 0
    board[x2][1] = 0

    dusts = [(x, y, board[x][y]) for y in range(c) for x in range(r) if board[x][y] != 0 and board[x][y] != -1]

summation = 0
for line in board:
    summation += sum(line)
print(summation + 2)
