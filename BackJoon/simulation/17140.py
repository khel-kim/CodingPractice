r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]


def make_line(line):
    new_line = []
    dic = {}
    for i in line:
        if i == 0:
            continue
        count = dic.get(i)
        if count:
            dic[i] += 1
        else:
            dic[i] = 1
    for key, value in dic.items():
        new_line.append((key, value))
    new_line.sort(key=lambda x: (x[1], x[0]))
    result_line = []
    for line in new_line:
        result_line.extend(line)
    return result_line


def padding(semi_board):
    max_len = 0
    for line in semi_board:
        if max_len < len(line):
            max_len = len(line)
    result_board = []
    for line in semi_board:
        result_board.append(line + [0] * (max_len - len(line)))
    return result_board


r -= 1
c -= 1
for time in range(101):
    row_len = len(board)
    column_len = len(board[0])
    if r < row_len and c < column_len and board[r][c] == k:
        print(time)
        break
    else:
        new_board = []
        if column_len <= row_len:
            for line in board:
                new_board.append(make_line(line))
            board = padding(new_board)
        else:
            for line in zip(*board):
                new_board.append(make_line(line))
            tmp_board = padding(new_board)
            board = []
            for line in zip(*tmp_board):
                board.append(line)
else:
    print(-1)
