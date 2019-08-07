from itertools import combinations
from collections import deque
T = int(input())
data = []
for _ in range(T):
    tmp = input().split()
    numbers = list(map(int, list(tmp[0])))
    n_interchange = int(tmp[1])
    data.append((numbers, n_interchange))


def sol(case):
    visited = []
    numbers, n = case
    wanted = sorted(numbers, reverse=True)
    index = [i for i in range(len(numbers))]
    maximum = 0
    queue = deque([(numbers, 0)])
    while queue:
        current, depth = queue.popleft()
        if current == wanted:
            if (n - depth) & 1 == 0:
                return "".join(list(map(str, current)))
            else:
                set_cur = set(current)
                for i in set_cur:
                    if current.count(i) > 1:
                        return int("".join(list(map(str, current))))
                current[-2], current[-1] = current[-1], current[-2]
                return "".join(list(map(str, current)))
        if depth == n:
            candi_max = int("".join(list(map(str, current))))
            if candi_max > maximum:
                maximum = candi_max
            continue
        for combination in combinations(index, 2):
            copy_current = current.copy()
            a, b = combination
            if copy_current[a] <= copy_current[b]:
                copy_current[a], copy_current[b] = copy_current[b], copy_current[a]
                queue.append((copy_current, depth + 1))
                visited.append(copy_current)
    return maximum


for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))
