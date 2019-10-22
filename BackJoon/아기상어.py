from collections import deque
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
moves = ((1, 0), (0, 1), (-1, 0), (0, -1))

shark_body = 2
shark_eat = 0


def get_shark_loc():
    for x in range(n):
        for y in range(n):
            if board[x][y] == 9:
                board[x][y] = 0
                return x, y


shark_loc = get_shark_loc()

queue = deque([(shark_loc, 0)])
check_board = [[False] * n for _ in range(n)]
check_board[shark_loc[0]][shark_loc[1]] = True

candi = []
total = 0
while queue:
    cur_loc, depth = queue.popleft()
    for dx, dy in moves:
        nx, ny = cur_loc[0] + dx, cur_loc[1] + dy
        if not 0 <= nx < n: continue
        if not 0 <= ny < n: continue
        if check_board[nx][ny] is True: continue
        if board[nx][ny] > shark_body: continue

        if 0 < board[nx][ny] < shark_body:
            candi.append((nx, ny))
            continue
        check_board[nx][ny] = True
        queue.append(((nx, ny), depth+1))

    if (not queue and candi) or (queue and queue[0][1] != depth and candi):
        candi.sort(key=lambda x: (x[0], x[1]))
        x, y = candi[0]
        board[x][y] = 0
        shark_eat += 1
        if shark_body == shark_eat:
            shark_body += 1
            shark_eat = 0

        total += depth+1
        candi = []
        queue = deque([((x, y), 0)])
        check_board = [[False] * n for _ in range(n)]
        check_board[x][y] = True

print(total)