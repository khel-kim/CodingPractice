n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

moves = [(1, 0), (0, 1), (-1, 0)]
except_cases = [
    [(0, 1), (1, 1), (1, 0), (1, 2), (2, 3)], # 생김새 + (세로, 가로 크기) # ㅗ
    [(0, 0), (1, 0), (2, 0), (1, 1), (3, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 1), (2, 3)],
    [(1, 0), (0, 1), (1, 1), (2, 1), (3, 2)],
    ]


def dfs(visit):
    if len(visit) >= 4:
        sum_tetromino = 0
        for x, y in visit:
            sum_tetromino += board[x][y]
        yield sum_tetromino
    else:
        current_x, current_y = visit[-1]
        for dx, dy in moves:
            nx = current_x + dx
            ny = current_y + dy
            if not 0 <= nx < n: continue
            if not 0 <= ny < m: continue
            if (nx, ny) in visit: continue
            visit.append((nx, ny))
            yield from dfs(visit)
            visit.pop()


max_tetromino = 0
for i in range(n):
    for j in range(m):
        visit = [(i, j)]
        for result in dfs(visit):
            if max_tetromino < result:
                max_tetromino = result

        for except_case in except_cases:
            except_sum = 0
            poly = except_case[:-1]
            height, width = except_case[-1]
            if i > n - height: continue
            if j > m - width: continue
            for dx, dy in poly:
                nx = i + dx
                ny = j + dy
                except_sum += board[nx][ny]
            if max_tetromino < except_sum:
                max_tetromino = except_sum

print(max_tetromino)
