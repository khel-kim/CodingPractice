def solution(n, times):
    minimum = min(times)
    start = minimum
    end = minimum * n + 1
    while start <= end:
        index = (start + end) // 2
        count = 0
        for time in times:
            count += index // time
            if count >= n: break
        if count >= n: end = index
        else: start = index
        if end - start <= 1:
            return end


T = int(input())
data = [None] * T
for t in range(T):
    n, m = map(int, input().split())
    tmp = []
    for _ in range(n):
        tmp.append(int(input()))
    data[t] = m, tmp

for num, case in enumerate(data):
    m, times = case
    print("#%s" % (num + 1), solution(m, times))

