n, m, k = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

# [현재 양분, 나무 나이 리스트, 죽은 나무 양분 추가 분, 현재 어린 나무 나이와 생성된 연도 튜플]
field = []
for _ in range(n):
    field.append([])
    for __ in range(n):
        tmp = [5, [], 0, []]
        field[-1].append(tmp)

for _ in range(m):
    tmp = list(map(int, input().split()))
    field[tmp[0] - 1][tmp[1] - 1][1].append(tmp[2])

reproduction = ((0, 1), (1, 0), (0, -1), (-1, 0),
                (1, 1), (1, -1), (-1, -1), (-1, 1))

for year in range(k):
    for x in range(n):
        for y in range(n):
            new_tree = []
            baby_tree = []

            for age, cycle in field[x][y][3]:  # 어린 나무가 있다면 먼저 체크
                if cycle == year - 1:
                    if age > field[x][y][0]:
                        continue
                    else:
                        field[x][y][0] -= age
                        new_tree.append(age + 1)
                else:
                    baby_tree.append((age, cycle))

            for age in field[x][y][1]:  # 현재 생존 나무 체크
                if age > field[x][y][0]:
                    field[x][y][2] += age // 2  # 죽은 나무가 있다면, 양분 추가량 증가
                else:
                    field[x][y][0] -= age
                    new_tree.append(age + 1)

                    if (age + 1) % 5 == 0: # 나이가 5의 배수라면 번식
                        for dx, dy in reproduction:
                            nx = x + dx
                            ny = y + dy
                            if 0 <= nx < n:
                                if 0 <= ny < n:
                                    field[nx][ny][3].append((1, year))

            field[x][y][0] += field[x][y][2] + A[x][y]
            field[x][y][2] = 0
            field[x][y][1] = new_tree
            field[x][y][3] = baby_tree

sum = 0
for i in range(n):
    for j in range(n):
        sum += len(field[i][j][1]) + len(field[i][j][3])
print(sum)
