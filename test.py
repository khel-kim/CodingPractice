def combinations(arr, k, visit=[]):
    if len(visit) == k:
        yield visit
    else:
        for i in range(len(arr)):
            visit.append(arr[i])
            yield from combinations(arr[i + 1:], k, visit)
            visit.pop()


for i in combinations([1,2,3,4,5,6], 4):
    print(i)