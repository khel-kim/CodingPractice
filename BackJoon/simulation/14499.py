n, m, x, y, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

moves = list(map(int, input().split()))
dice = [-1] + [0] * 6
delta = [None, (0, 1), (0, -1), (-1, 0), (1, 0)]
dice_status = (1, 6, 4, 3, 2, 5)  # top, bottom, left side, right side, upside, downside


def get_dice_status(dice_status, move):
    if move == 1: return dice_status[2], dice_status[3], dice_status[1], dice_status[0], dice_status[4], dice_status[5]
    elif move == 2: return dice_status[3], dice_status[2], dice_status[0], dice_status[1], dice_status[4], dice_status[5]
    elif move == 3: return dice_status[5], dice_status[4], dice_status[2], dice_status[3], dice_status[0], dice_status[1]
    else: return dice_status[4], dice_status[5], dice_status[2], dice_status[3], dice_status[1], dice_status[0]


while moves:
    move = moves.pop(0)
    dx, dy = delta[move]
    nx = x + dx
    ny = y + dy
    if not 0 <= nx < n: continue
    if not 0 <= ny < m: continue
    dice_status = get_dice_status(dice_status, move)

    if board[nx][ny] == 0: board[nx][ny] = dice[dice_status[1]]
    else:
        dice[dice_status[1]] = board[nx][ny]
        board[nx][ny] = 0

    print(dice[dice_status[0]])
    x = nx
    y = ny
