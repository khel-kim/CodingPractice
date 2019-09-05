def solution(food_times, k):
    if k < len(food_times):
        return k + 1
    if k >= sum(food_times):
        return -1

    new_food_times = [(id, time) for id, time in enumerate(food_times)]
    prev_minimum = 0
    for _ in range(k):
        n = len(new_food_times)
        minimum = 100000001
        index = []
        for order, (id, time) in enumerate(new_food_times):
            if minimum > time:
                minimum = time
                index = [order]
            elif minimum == time:
                index.append(order)

        new_k = k - (n * (minimum - prev_minimum))
        if new_k >= 0:
            tmp = 0
            for i in index:
                new_food_times.pop(i - tmp)
                tmp += 1
        else:
            result_index = k % len(new_food_times)
            return new_food_times[result_index][0] + 1
        k = new_k
        prev_minimum = minimum


food_times = [1,2,3,4,5,6,6,7,8,9,10,11]
k = 16

print(solution(food_times.copy(), k))