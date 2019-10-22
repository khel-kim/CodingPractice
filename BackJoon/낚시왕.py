R, C, m = map(int, input().split())
sharks = []
for _ in range(m):
    r, c, s, d, z = map(int, input().split())
    sharks.append((r-1, c-1, s, d, z))

# shark init
shark_dic = {(x, y): [] for x in range(R) for y in range(C)}
for r, c, s, d, z in sharks:
    shark_dic[(r, c)].append((s, d, z))


def move(x, y, s, d):
    if d == 1:
        x = 2 * R - 2 - x
        now = (x + s) % (2 * R - 2)
        if now < R:
            return now, y, 2
        else:
            return (2 * R - 2) - now, y, 1
    elif d == 2:
        now = (x + s) % (2 * R - 2)
        if now < R:
            return now, y, 2
        else:
            return (2 * R - 2) - now, y, 1
    elif d == 3:
        now = (y + s) % (2 * C - 2)
        if now < C:
            return x, now, 3
        else:
            return x, (2 * C - 2) - now, 4
    else:
        y = 2 * C - 2 - y
        now = (y + s) % (2 * C - 2)
        if now < C:
            return x, now, 3
        else:
            return x, (2 * C - 2) - now, 4


total = 0
for now in range(C):
    # 낚시
    for row in range(R):
        if len(shark_dic[(row, now)]) > 0:
            total += shark_dic[(row, now)][0][2]
            shark_dic[(row, now)] = []
            break
    # 이동
    new_shark_dic = {(x, y): [] for x in range(R) for y in range(C)}
    for (x, y), value in shark_dic.items():
        if len(value) == 0:
            continue
        s, d, z = value[0]
        nx, ny, nd = move(x, y, s, d)
        new_shark_dic[(nx, ny)].append((s, nd, z))
    # 잡기
    for (x, y), value in new_shark_dic.items():
        if len(value) > 1:
            new_shark_dic[(x, y)] = [sorted(new_shark_dic[(x, y)], key=lambda x: -x[2])[0]]
    shark_dic = new_shark_dic
print(total)
