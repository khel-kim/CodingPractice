n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    board.append(tmp)

rotations = ((-1, 0), (0, -1), (1, 0), (0, 1))
if d == 0:
    direction = 0
elif d == 1:
    direction = 3
elif d == 2:
    direction = 2
else:
    direction = 1

count = 1
board[r][c] = 2
while True:
    current_location = (r, c)
    for i in range(1, 5):
        current_direction = (direction + i) % 4
        dx, dy = rotations[current_direction]
        nx, ny = r + dx, c + dy
        if board[nx][ny] != 0: continue
        r, c = nx, ny
        board[r][c] = 2
        count += 1
        direction = current_direction
        break
    if current_location != (r, c): continue
    else:
        current_direction = (direction + 2) % 4
        dx, dy = rotations[current_direction]
        nx, ny = r + dx, c + dy
        if board[nx][ny] == 1: break
        else:
            r, c = nx, ny

print(count)
