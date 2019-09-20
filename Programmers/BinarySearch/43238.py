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


print(solution(1, [7, 10]))
