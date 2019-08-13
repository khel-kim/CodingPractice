def fixed_len_power_set(arr, k, visit1=[0]):
    if len(visit1) == k:
        yield visit1
    else:
        for index in range(len(arr)):
            if len(visit1) >= k: continue
            visit1.append(arr[index])
            yield from fixed_len_power_set(arr[index+1:], k, visit1)
            visit1.pop()



n = 10
for j in fixed_len_power_set(list(range(n))[1:], n//2):
    print(j)
