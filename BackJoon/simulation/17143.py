r, c, m = map(int, input().split())
sharks = [list(map(int, input().split())) for _ in range(m)]

sharks_dic = {(x, y): (s, d, z) for x, y, s, d, z in sharks}

r_board = [i for i in range(1, r + 1)] + [i for i in range(r - 1, 1, -1)]
r_len = len(r_board)
c_board = [i for i in range(1, c + 1)] + [i for i in range(c - 1, 1, -1)]
c_len = len(c_board)


total = 0

for column in range(1, c+1):
    for x in range(1, r+1):
        candi = sharks_dic.get((x, column))
        if candi:
            total += candi[2]
            sharks_dic.pop((x, column))
            break
        else:
            continue

    new_sharks_dic = {}
    for key, value in sharks_dic.items():
        x, y = key
        s, d, z = value
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

        check = new_sharks_dic.get((x, y))
        if check:
            if check[2] < z:
                new_sharks_dic[(x, y)] = s, d, z
        else:
            new_sharks_dic[(x, y)] = s, d, z

    sharks_dic = new_sharks_dic

print(total)
