import collections
deque = collections.deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
movements = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def get_shark_location():
    for x in range(n):
        for y in range(n):
            if board[x][y] == 9:
                board[x][y] = 0
                return x, y


shark_location = get_shark_location()
shark_body = 2
shark_eat = 0
check_board = [[False] * n for _ in range(n)]


def bfs(location):
    global shark_eat, shark_body
    candi = []
    queue = deque([(location, 0)])
    visit = [location]
    check_board[location[0]][location[1]] = True
    max_depth = 9999
    while queue:
        loc, depth = queue.popleft()
        if max_depth <= depth:
            break
        for dx, dy in movements:
            nx, ny = loc[0] + dx, loc[1] + dy
            if not 0 <= nx < n: continue
            if not 0 <= ny < n: continue
            if board[nx][ny] > shark_body: continue
            if check_board[nx][ny]: continue
            if 0 < board[nx][ny] < shark_body:
                candi.append((nx, ny, depth+1))
                max_depth = depth + 1
                visit.append((nx, ny))
                check_board[nx][ny] = True
            elif not candi:
                queue.append(((nx, ny), depth+1))
                visit.append((nx, ny))
                check_board[nx][ny] = True
    if candi:
        candi.sort(key=lambda x: (x[0], x[1]))
        nx, ny, depth = candi[0]
        board[nx][ny] = 0
        shark_eat += 1
        if shark_eat == shark_body:
            shark_body += 1
            shark_eat = 0
        for x, y in visit:
            check_board[x][y] = False
        return (nx, ny), depth
    else:
        return


time = 0
while True:
    result = bfs(shark_location)
    if result is None:
        break
    else:
        time += result[1]
        shark_location = result[0]
print(time)
