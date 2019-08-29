r, c, m = map(int, input().split())
candi = []
sharks = []
for _ in range(m):
    tmp = tuple(list(map(int, input().split())))
    if tmp[1] == 1:
        candi.append(tmp)
    else:
        sharks.append(tmp)

r_board = [i for i in range(1, r + 1)] + [i for i in range(r - 1, 1, -1)]
r_len = len(r_board)
c_board = [i for i in range(1, c + 1)] + [i for i in range(c - 1, 1, -1)]
c_len = len(c_board)


total = 0
# 1. 상어 이동
# 2. 상어 정리
# 3. 낚시왕 이동
# 4. 상어 잡기

for column in range(2, c+1):
    print(sharks)
    candi_dic = {}
    # print(candi)
    if candi:
        # 중복제거
        for x, y, s, d, z in candi:
            candi_info = candi_dic.get((x, y))
            if candi_info and candi_info[2] < z:
                candi_dic[(x, y)] = s, d, z
            else:
                candi_dic[(x, y)] = s, d, z
        candi = []
        for key, value in candi_dic.items():
            candi.append(key + value)
        # 가장 위에 상어
        candi.sort(key=lambda x: x[0])
        total += candi[0][4]
    sharks.extend(candi[1:])

    sharks_dic = {}
    candi = []
    for x, y, s, d, z in sharks:
        # 상어별 이동
        if d == 1:
            index = (x - 1 - s) % r_len
            x = r_board[index]
            if index >= r:
                d = 2
        elif d == 2:
            index = (x - 1 + s) % r_len
            x = r_board[index]
            if index >= r:
                d = 1
        elif d == 3:
            index = (y - 1 + s) % c_len
            y = c_board[index]
            if index >= c:
                d = 4
        else:
            index = (y - 1 - s) % c_len
            y = c_board[index]
            if index >= c:
                d = 3
        print(x, y, column)
        if y == column:
            candi.append((x, y, s, d, z))
        else:
            shark_info = sharks_dic.get((x, y))
            if shark_info and shark_info[2] < z:
                sharks_dic[(x, y)] = s, d, z
            else:
                sharks_dic[(x, y)] = s, d, z

    sharks = []
    for key, value in sharks_dic.items():
        sharks.append(key + value)
    print(sharks)
    print(total)
candi_dic = {}
if candi:
    for x, y, s, d, z in candi:
        candi_info = candi_dic.get((x, y))
        if candi_info and candi_info[2] < z:
            candi_dic[(x, y)] = s, d, z
        else:
            candi_dic[(x, y)] = s, d, z
    candi = []
    for key, value in candi_dic.items():
        candi.append(key + value)
    candi.sort(key=lambda x: x[0])
    total += candi[0][4]

print(total)

"""
4 6 4
4 1 3 3 8
1 3 5 2 9
2 4 8 4 1
4 5 0 1 4

4 6 1
2 2 3 4 8

"""