def solution(board, black=1000):
    n = len(board)
    m = len(board[0])
    check_board1 = [
        [[0, black, black], [0, 0, 0]],
        [[black, 0, black], [0, 0, 0]],
        [[black, black, 0], [0, 0, 0]],
    ]
    check_board2 = [
        [[black, 0], [black, 0], [0, 0]],
        [[0, black], [0, black], [0, 0]],
    ]

    def check(x, y, check_board):
        check_set = []
        for dx in range(len(check_board)):
            for dy in range(len(check_board[0])):
                tmp = board[x + dx][y + dy] + check_board[dx][dy]
                if tmp == 0:
                    return False
                elif tmp != black:
                    check_set.append(tmp)
        if len(set(check_set)) == 1:
            return True
        else:
            return False

    def check_upward(start_x, start_y, check_board):
        index_y = []
        for index, value in enumerate(check_board[0]):
            if value:
                index_y.append(index)
        for check_y in index_y:
            for check_x in range(start_x):
                if board[check_x][start_y + check_y]:
                    return False
        return True

    change = True
    count = 0
    while change:
        change = False
        for i in range(n-1):
            for j in range(m-2):
                for check_field in check_board1:
                    if check(i, j, check_field) and check_upward(i, j, check_field):
                        count += 1
                        change = True
                        for p in range(2):
                            for q in range(3):
                                board[i+p][j+q] = False
        for i in range(n-2):
            for j in range(m-1):
                for check_field in check_board2:
                    if check(i, j, check_field) and check_upward(i, j, check_field):
                        count += 1
                        change = True
                        for p in range(3):
                            for q in range(2):
                                board[i+p][j+q] = False
    return count
