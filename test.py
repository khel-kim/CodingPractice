def solution(n, times):
    minimum = min(times)
    start = minimum
    end = min(minimum * n + 1, (n // len(times)+1) * max(times))
    while start <= end:
        index = (start + end) // 2
        count = 0
        before_count = 0
        # print(start, end, index)
        for time in times:
            count += index // time
            before_count += (index - 1) // time
            if count > n:
                break
        if count == n:
            if before_count == n - 1:
                return index
            else:
                end = index
        elif count > n:
            end = index
        else:
            start = index
        if start == end:
            return start
        elif end - start == 1:
            return end


print(solution(1, [7, 10]))
