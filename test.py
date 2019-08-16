moves = [0, 4, 2, 4, 4, 1]


def DFS(kinds, visit=[], depth=0):
    if len(visit) == len(kinds):
        yield visit
    else:
        for i in range(moves[kinds[depth]]):
            visit.append(i)
            yield from DFS(kinds, visit, depth+1)
            visit.pop()


for k in DFS([1, 2, 3, 4, 1, 2, 5]):
    print(k)
