from collections import deque
T = int(input())
data = []
for _ in range(T):
    n, m, k = map(int, input().split())
    board = []
    for __ in range(n):
        tmp = list(map(int, input().split()))
        board.append(tmp)
    data.append((n, m, k, board))


reproductions = [(1, 0),
                (0, 1),
                (-1, 0),
                (0, -1),]


def sol(case):
    n, m, k, board = case
    # field init
    field = [[(0, 301)] * 350 for _ in range(350)]  # board's (0, 0) -> field's (150, 150)

    # Search
    cell = deque([])
    for x in range(n):
        for y in range(m):
            if board[x][y] != 0:
                cell.append(((x + 150, y + 150), board[x][y] + 1, board[x][y]))  # 좌표, 번식의 절대적 시간, 생명력, 활성이 끝나는 시간
                field[x + 150][y + 150] = (board[x][y], 0)

    active = []
    for hour in range(2, k+1):
        newbie = deque([])
        inactive_tmp = deque([])

        for inactive_cur in cell:
            # inactive_cur = ((x좌표, y좌표), 번식의 절대적 시간, 생명력)
            if inactive_cur[1] == hour:
                x, y = inactive_cur[0][0], inactive_cur[0][1]
                life = inactive_cur[2]
                field[x][y] = (field[x][y][0], False)
                if life > 1:
                    active.append((hour, hour + life - 2))
                for dx, dy in reproductions:
                    nx, ny = x + dx, y + dy
                    if field[nx][ny][1] < hour:  # 전 분기에 업데이트 됐으면 continue
                        continue
                    if field[nx][ny][0] == 0:  # 업데이트 된적이 없다면,
                        field[nx][ny] = (life, hour)
                        newbie.append(((nx, ny), hour + life + 1, life))
                    elif life > field[nx][ny][0]:  # 지금 life가 전보다 높을 경우
                        newbie.remove(((nx, ny), hour + field[nx][ny][0] + 1, field[nx][ny][0]))
                        field[nx][ny] = (life, hour)
                        newbie.append(((nx, ny), hour + life + 1, life))
            else:
                inactive_tmp.append(inactive_cur)

            for activation in active:
                if hour > activation[1]:
                    active.remove(activation)
        cell = inactive_tmp
        cell.extend(newbie)
    return len(cell) + len(active)


for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))
