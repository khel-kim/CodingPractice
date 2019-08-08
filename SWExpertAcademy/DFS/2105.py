T = int(input())
data = []
for _ in range(T):
    n = int(input())
    board = []
    for __ in range(n):
        tmp = list(map(int, input().split()))
        board.append(tmp)
    data.append((n, board))


def sol(case):
    n, board = case
    moves = [(1, 1),
             (1, -1),
             (-1, -1),
             (-1, 1)]

    def DFS(visit, dessert, move_index=0, depth=0):
        if visit[-1][0] == visit[0][0] + 1 and visit[-1][1] == visit[0][1] - 1:
            yield len(dessert)
        else:
            if depth == 0:
                changes = 1
            else:
                changes = 2
            for change in range(changes):  # change == 0 => 직진, change == 1 => 우회전
                move_index += change
                if move_index > 3:
                    break
                nx = visit[-1][0] + moves[move_index][0]
                ny = visit[-1][1] + moves[move_index][1]
                if not 0 <= nx < n: continue
                if not 0 <= ny < n: continue
                if board[nx][ny] in dessert: continue
                visit.append([nx, ny])
                dessert.append(board[nx][ny])
                yield from DFS(visit, dessert, move_index, depth+1)
                visit.pop()
                dessert.pop()

    maximum = 0
    for i in range(0, n-2):
        for j in range(1, n-1):
            visit = [(i, j)]
            dessert = [board[i][j]]
            for summation in DFS(visit, dessert):
                if maximum < summation:
                    maximum = summation
    if maximum == 0:
        return -1
    return maximum


for num, case in enumerate(data):
    print("#%s" %(num + 1), sol(case))
