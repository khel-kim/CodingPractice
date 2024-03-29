pipe1 = (1, 2)
set1 = ((0, -1), (0, 1))
set2 = ((-1, 0), (1, 0))
check_board = [[False] * 51 for _ in range(51)]


def DFS(visit, depth=1):
    global minimum
    if depth >= minimum - 3:
        return
    x, y, direction = visit[-1]
    if x == y == 0:
        if direction[0] == final_direction:
            if minimum > depth:
                print("check", visit)
                minimum = depth
    else:
        if board[x][y] == 1:
            moves = [direction]
        else:
            if not direction[0]:
                moves = set2
            else:
                moves = set1
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if check_board[nx][ny]: continue
            if not dic.get((nx, ny)): continue

            if nx == n-1 and dy == 1: continue
            if ny == n-1 and dx == 1: continue
            if nx == 0 and dy == 1: continue
            if ny == 0 and dx == 1: continue

            visit.append((nx, ny, (dx, dy)))
            check_board[nx][ny] = True
            DFS(visit, depth + 1)
            visit.pop()
            check_board[nx][ny] = False


for t in range(int(input())):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    dic = {}
    for p in range(n):
        for q in range(n):
            if board[p][q] == 0:
                pass
            elif board[p][q] in pipe1:
                board[p][q] = 1
                dic[(p, q)] = 1
            else:
                board[p][q] = 2
                dic[(p, q)] = 2
    if board[0][0] == 1:
        final_direction = 0
    else:
        final_direction = 1

    check_board[n-1][n-1] = True
    minimum = 50 * 50
    DFS([(n-1, n-1, (0, -1))])
    print("#%s" % (t + 1), minimum)
    check_board[n - 1][n - 1] = False

"""
5
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


1
5
1 4 3 1 4 
0 3 1 1 3 
0 0 2 0 2 
0 0 6 3 5 
0 0 0 6 1 

1
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