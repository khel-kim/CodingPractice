n = int(input())
block_info = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]

checkers = [(-1, -1), (1, -1), (1, 1), (-1, 1)]

u, v, w, x, y = block_info
base_block = []
for i in range(x + v + 1):
    if i == 0:
        tmp = [0] * u
    elif 1 <= i < 1 + x:
        tmp = []
        for j in range(u):
            if j < w:
                tmp.append(0)
            elif w <= j < w + y:
                tmp.append(1)
            else:
                tmp.append(0)
    else:
        tmp = [1] * u
    base_block.append(tmp)


def rotation_block(block):
    rotated_block = []
    height = len(block)
    width = len(block[0])
    for y in range(1, width + 1):
        rotated_block.append([])
        for x in range(height):
            rotated_block[-1].append(block[x][-y])
    return rotated_block


def checker(block, h, w, p, q):
    for dx in range(h):
        for dy in range(w):
            nx, ny = p + dx, q + dy
            if board[nx][ny] + block[dx][dy] != 1:
                return False
    return True


count = 0
position = []
for i in range(4):
    base_block = rotation_block(base_block)
    height = len(base_block)
    width = len(base_block[0])
    # print(n)
    # print(height, width)
    # print(base_block)
    for p in range(n - height + 1):
        for q in range(n - width + 1):
            if checker(base_block, height, width, p, q):
                if i == 0:
                    nx = p - 1
                    ny = q
                    if not 0 <= nx < n: pass
                    elif not 0 <= ny < n: pass
                    elif board[nx][ny] == 1: break
                    nx = p + height
                    ny = q
                    if not 0 <= nx < n: pass
                    elif not 0 <= ny < n: pass
                    elif board[nx][ny] == 1:break
                elif i == 2:
                    nx = p - 1
                    ny = q + 1
                    if not 0 <= nx < n: pass
                    elif not 0 <= ny < n: pass
                    elif board[nx][ny] == 1: break
                    nx = p + height
                    ny = q + 1
                    if not 0 <= nx < n: pass
                    elif not 0 <= ny < n: pass
                    elif board[nx][ny] == 1: break

                elif i == 1:
                    nx = p + 1
                    ny = q - 1
                    if not 0 <= nx < n: pass
                    elif not 0 <= ny < n: pass
                    elif board[nx][ny] == 1: break
                    nx = p + 1
                    ny = q + width
                    if not 0 <= nx < n: pass
                    elif not 0 <= ny < n: pass
                    elif board[nx][ny] == 1: break
                elif i == 3:
                    nx = p
                    ny = q - 1
                    if not 0 <= nx < n: pass
                    elif not 0 <= ny < n: pass
                    elif board[nx][ny] == 1: break
                    nx = p
                    ny = q + width
                    if not 0 <= nx < n: pass
                    elif not 0 <= ny < n: pass
                    elif board[nx][ny] == 1: break
                count += 1

                if i == 1:
                    x = p + 1
                    y = q
                elif i == 2:
                    x = p
                    y = q + 1
                elif i == 0:
                    x, y = p, q - 1
                    while 0 <= y and board[x][y] == 1:
                        y -= 1
                    y += 1
                elif i == 3:
                    x, y = p - 1, q
                    while 0 <= x and board[x][y] == 1:
                        x -= 1
                    x += 1

                position.append((x, y))

if not count:
    print(0)
    print()
else:
    print(count)
    for p, q in position:
        print(p+1, q+1)

"""
5
5 1 1 1 3
0 0 0 0 0 
0 1 1 1 1 
0 1 0 0 1
0 1 0 0 1 
0 1 0 0 1 
"""