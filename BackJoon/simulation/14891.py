top1 = list(map(int, input()))
top2 = list(map(int, input()))
top3 = list(map(int, input()))
top4 = list(map(int, input()))

k = int(input())
rotations = []
for _ in range(k):
    tmp = list(map(int, input().split()))
    rotations.append((tmp[0] - 1, tmp[1]))

top = [top1, top2, top3, top4]


def rotation(wheel, method):
    if method == 1:
        return wheel[-1:] + wheel[:-1]
    else:
        return wheel[1:] + wheel[:1]


for top_index, direction in rotations:
    changed = [(top_index, direction)]
    if top_index == 0:
        for __ in range(3):
            if top[top_index][2] != top[top_index + 1][6]:
                top_index += 1
                direction *= -1
                changed.append((top_index, direction))
            else:
                break

    elif top_index == 1:
        if top[0][2] != top[1][6]:
            changed.append((0, direction * (-1)))
        if top[1][2] != top[2][6]:
            changed.append((2, direction * (-1)))
            if top[2][2] != top[3][6]:
                changed.append((3, direction))

    elif top_index == 2:
        if top[2][2] != top[3][6]:
            changed.append((3, direction * (-1)))
        if top[1][2] != top[2][6]:
            changed.append((1, direction * (-1)))
            if top[0][2] != top[1][6]:
                changed.append((0, direction))

    else:
        for __ in range(3):
            if top[top_index][6] != top[top_index - 1][2]:
                top_index -= 1
                direction *= -1
                changed.append((top_index, direction))
            else:
                break

    for index, toward in changed:
        top[index] = rotation(top[index], toward)

score = top[0][0] + top[1][0] * 2 + top[2][0] * 4 + top[3][0] * 8
print(score)
