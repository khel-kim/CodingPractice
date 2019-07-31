n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

checking_types = [
    [(0, 0), (0, 1), (0, 2), (0, 3), (1, 4)],  # 생김새 + (세로, 가로 크기) # 긴거
    [(0, 0), (1, 0), (2, 0), (3, 0), (4, 1)],  # 생김새 + (세로, 가로 크기)

    [(0, 0), (0, 1), (1, 0), (1, 1), (2, 2)],  # 생김새 + (세로, 가로 크기) # 네모

    [(0, 0), (1, 0), (1, 1), (1, 2), (2, 3)],  # 생김새 + (세로, 가로 크기) # ㄴ
    [(0, 1), (1, 1), (2, 1), (2, 0), (3, 2)],  # 생김새 + (세로, 가로 크기)
    [(0, 0), (0, 1), (0, 2), (1, 2), (2, 3)],  # 생김새 + (세로, 가로 크기)
    [(0, 0), (0, 1), (1, 0), (2, 0), (3, 2)],  # 생김새 + (세로, 가로 크기)

    [(0, 0), (0, 1), (1, 1), (2, 1), (3, 2)],  # 생김새 + (세로, 가로 크기) # ㄱ
    [(0, 0), (0, 1), (0, 2), (1, 0), (2, 3)],  # 생김새 + (세로, 가로 크기)
    [(0, 0), (1, 0), (2, 0), (2, 1), (3, 2)],  # 생김새 + (세로, 가로 크기)
    [(1, 0), (1, 1), (1, 2), (0, 2), (2, 3)],  # 생김새 + (세로, 가로 크기)

    [(0, 0), (0, 1), (1, 1), (1, 2), (2, 3)],  # 생김새 + (세로, 가로 크기) # ㄱ_
    [(0, 1), (1, 1), (1, 0), (2, 0), (3, 2)],  # 생김새 + (세로, 가로 크기)

    [(0, 2), (0, 1), (1, 1), (1, 0), (2, 3)],  # 생김새 + (세로, 가로 크기) # _r
    [(0, 0), (1, 0), (1, 1), (2, 1), (3, 2)],  # 생김새 + (세로, 가로 크기)

    [(1, 0), (1, 1), (1, 2), (0, 1), (2, 3)],  # 생김새 + (세로, 가로 크기) # ㅗ
    [(1, 0), (1, 1), (0, 1), (2, 1), (3, 2)],  # 생김새 + (세로, 가로 크기)
    [(0, 0), (0, 1), (0, 2), (1, 1), (2, 3)],  # 생김새 + (세로, 가로 크기)
    [(0, 0), (1, 0), (2, 0), (1, 1), (3, 2)],  # 생김새 + (세로, 가로 크기)
    ]


max_tetrimino = 0
for checking_type in checking_types:  # time_complexity *= 19
    poly = checking_type[:-1]
    height, width = checking_type[-1]
    for i in range(n - height + 1):  # time_complexity *= 500
        for j in range(m - width + 1):  # time_complexity *= 500
            sum_now = 0
            for dx, dy in poly:  # time_complexity *= 4
                nx = i + dx
                ny = j + dy
                sum_now += board[nx][ny]
            if max_tetrimino < sum_now:
                max_tetrimino = sum_now

print(max_tetrimino)

# from pprint import pprint
# import copy
# tmp_board = [[None] * 4 for _ in range(4)]
#
# for i, checking_type in enumerate(checking_types):
#
#     checking_board = copy.deepcopy(tmp_board)
#     poly = checking_type[:-1]
#     height, width = checking_type[-1]
#     for dx, dy in poly:
#         checking_board[dx][dy] = 1000
#     print(i)
#     print("height and width: ", height, width)
#     pprint(checking_board)
