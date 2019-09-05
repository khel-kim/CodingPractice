def solution(food_times, k):
    from collections import deque
    dic_index = {}
    dic_times = {}
    summation = 0
    for index, time in enumerate(food_times):
        dic_index[index] = time
        summation += time
        if dic_times.get(time):
            dic_times[time].append(index)
        else:
            dic_times[time] = [index]

    if k >= summation:
        return -1
    minimum_list = deque(sorted(dic_times.keys()))
    minimum = minimum_list.popleft()
    prev_minimum = 0

    for _ in range(k):
        new_k = k - (len(dic_index) * (minimum - prev_minimum))

        if new_k >= 0:
            prev_minimum = minimum
            k = new_k

            index = dic_times[minimum]
            dic_times.pop(minimum)
            for i in index:
                dic_index.pop(i)

            minimum = minimum_list.popleft()
        else:
            keys = list(dic_index.keys())
            result_index = k % len(keys)
            return keys[result_index] + 1