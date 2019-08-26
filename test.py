arr = [i for i in range(1, 11)]


def DFS(arr, visit=[], depth=0, now_sum=0):
    if now_sum == 10:
        yield visit
    else:
        if depth >= 10:
            return
        for i in range(2):
            if i == 0:
                yield from DFS(arr, visit, depth+1, now_sum)
            elif i == 1:
                if now_sum + arr[depth] > 10: continue
                visit.append(arr[depth])
                yield from DFS(arr, visit, depth+1, now_sum + arr[depth])
                visit.pop()


for i, j in enumerate(DFS(arr, [])):
    print(i, j)
