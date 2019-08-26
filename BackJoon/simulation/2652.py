n = int(input())
block_info = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]


def get_block(info):
    u, v, w, x, y = info
    block = [[0] * u for _ in range(x+1)]
    for p in range(1, 1 + x):
        for q in range(w, w + y):
            block[p][q] = 1
    for _ in range(v):
        block.append([1] * u)
    return block


def get_rotated_block(block):
    height = len(block)
    width = len(block[0])
    new_block = [[0] * height for _ in range(width)]
    for p in range(height):
        for q in range(width):
            new_block[width - q - 1][p] = block[p][q]
    return new_block


def search(x, y, block):
    height = len(block)
    width = len(block[0])
    for p in range(height):
        for q in range(width):
            if board[x + p][y + q] + block[p][q] != 1:
                return False
    return True


count = 0
locations = []
#########################################################
base_block = get_block(block_info)
height = len(base_block)
width = len(base_block[0])
for x in range(n - height + 1):
    for y in range(n - width + 1):
        if search(x, y, base_block):
            if 0 <= y - 1 and board[x][y-1] == 1:
                break
            if y + width < n and board[x][y + width] == 1:
                break

            count += 1
            while 0 <= x and board[x][y] == 1:
                x -= 1
            x += 1
            locations.append((x, y))
############################################################
block1 = get_rotated_block(base_block)
height = len(block1)
width = len(block1[0])
for x in range(n - height + 1):
    for y in range(n - width + 1):
        if search(x, y, block1):
            if 0 <= x - 1 and board[x-1][y] == 1:
                break
            if x + height < n and board[x + height][y] == 1:
                break

            count += 1
            while 0 <= y and board[x][y] == 1:
                y -= 1
            y += 1
            locations.append((x, y))
############################################################
block2 = get_rotated_block(block1)
height = len(block2)
width = len(block2[0])
for x in range(n - height + 1):
    for y in range(n - width + 1):
        if search(x, y, block2):
            if 0 <= y - 1 and board[x+block_info[1]][y-1] == 1:
                break
            if y + width < n and board[x+block_info[1]][y+width] == 1:
                break

            count += 1
            locations.append((x + block_info[1], y))
############################################################
block3 = get_rotated_block(block2)
height = len(block3)
width = len(block3[0])
for x in range(n - height + 1):
    for y in range(n - width + 1):
        if search(x, y, block3):
            if 0 <= x - 1 and board[x-1][y+block_info[1]] == 1:
                break
            if x + height < n and board[x+height][y+block_info[1]] == 1:
                break

            count += 1
            locations.append((x, y + block_info[1]))
############################################################
if count == 0:
    print(0)
    print()
else:
    print(count)
    for location in locations:
        print(location[0] + 1, location[1] + 1)
