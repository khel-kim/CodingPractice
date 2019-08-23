def permutation(arr, k, visit=[]):
    if len(visit) == k:
        print(visit)
    else:
        for i in range(len(arr)):
            if arr[i] in visit: continue
            visit.append(arr[i])
            permutation(arr, k, visit)
            visit.pop()

arr = [1,2,3]
k = 3
permutation(arr, k)