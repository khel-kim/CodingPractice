jobs = [[0, 3], [1, 9], [2, 6]]


def solution(jobs):
    import heapq
    sorted_jobs = sorted(jobs, key=lambda x: (x[0], x[1]))
    total = 0
    heap = []
    time = sorted_jobs[0][0]
    for request, taken_time in sorted_jobs:
        if request <= time:
            heapq.heappush(heap, (taken_time, request))
        else:
            while heap and time < request:
                cur_taken_time, cur_request = heapq.heappop(heap)
                if time < cur_request:
                    time = cur_request
                time += cur_taken_time
                total += time - cur_request

            heapq.heappush(heap, (taken_time, request))

    while heap:
        cur_taken_time, cur_request = heapq.heappop(heap)
        if time < cur_request:
            time = cur_request
        time += cur_taken_time
        total += time - cur_request
    return total // len(jobs)


print(solution(jobs))
