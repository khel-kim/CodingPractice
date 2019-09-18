def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    count = 0
    i = 0  # start
    while i < len(arr):
        count += 1
        print("countcount", count, "*" * 100)
        print(i)
        print(c)
        print(arr,"before")
        print(result, "before")
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0

            i += 1
        print("%" * 20)
        print(arr, "after")
        print(result, "after")
    return result


arr = [i for i in range(1, 4)]
print(len(permute(arr)))

import itertools

permutations = itertools.permutations

for i, arr in enumerate(permutations(arr)):
    # print(i+1, arr)
    pass
print(i+1)
