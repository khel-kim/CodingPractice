n, m, h = map(int, input().split())
dic_lines = {}
dic_candi = {}
for x in range(h):
    dic_lines[x] = []
    dic_candi[x] = []

for _ in range(m):
    tmp = list(map(int, input().split()))
    dic_lines[tmp[0]-1].append(tmp[1]-1)  # key: row index, value: line positions


candidates = []
for x in range(h):
    for y in range(n):
        if y in dic_lines[x]:
            continue
        if y-1 in dic_lines[x]:
            continue
        if y+1 in dic_lines[x]:
            continue
        if n <= y + 1:
            continue
        candidates.append((x, y))


def go_down():
    points = [i for i in range(n)]
    for row in range(h):
        for change in dic_lines[row]:
            points[change], points[change+1] = points[change+1], points[change]
        for change in dic_candi[row]:
            points[change], points[change+1] = points[change+1], points[change]
    for i, point in enumerate(points):
        if i != point:
            return False
    return True


def combinations(arr, k, visit=[]):
    if len(visit) == k:
        yield visit
    else:
        for i in range(len(arr)):
            if arr[i] in visit: continue
            if (arr[i][0], arr[i][1] - 1) in visit: continue
            visit.append(arr[i])
            yield from combinations(arr[i+1:], k, visit)
            visit.pop()


def sol():
    if go_down():
        return 0
    else:
        for added_line in range(1, 4):
            if added_line > len(candidates):
                break
            for candi in combinations(candidates, added_line):
                for key, value in candi:
                    dic_candi[key].append(value)
                if go_down():
                    return added_line
                for key, value in candi:
                    dic_candi[key] = []
        return -1

print(sol())
