from collections import deque
T = 1
data = []
for _ in range(T):
    v, e = map(int, input().split())
    tmp = list(map(int, input().split()))
    dic1 = {i+1: deque([]) for i in range(v)}
    dic2 = {i+1: [] for i in range(v)}
    tail = []
    for i in range(0, 2 * e, 2):
        dic1[tmp[i]].append(tmp[i+1])
        dic2[tmp[i+1]].append(tmp[i])
        tail.append(tmp[i+1])
    data.append((v, dic1, dic2, tail))


def sol(case):
    v, dic1, dic2, tail = case
    top = deque([i for i in range(1, v+1) if i not in tail])

    def DFS(current):
        if not dic1[current]:
            return
        else:
            while dic1[current]:
                next_point = dic1[current].popleft()
                if len(dic2[next_point]) > 1:
                    dic2[next_point].remove(current)
                    continue
                if next_point not in visit:
                    visit.append(next_point)
                DFS(next_point)

    visit = top.copy()
    while top:
        DFS(top.popleft())
    return " ".join(map(str, visit))


for num, case in enumerate(data):
    print("#%s" % (num + 1), sol(case))
