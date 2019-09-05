def solution(food_times, k):
    if k < len(food_times):
        return k + 1
    maximum = 0
    summation = 0
    for i in food_times:
        summation += i
        if maximum < i:
            maximum = i
    if k >= summation:
        return -1
    else:
        n = len(food_times)
        board = [[0] * maximum for _ in range(n)]
        count = 1
        for y in range(maximum):
            x = 0
            remove_index = []
            while x < n:
                if y < food_times[x]:
                    if count == k + 1:
                        return board[x][0]
                    board[x][y] = count
                    count += 1
                else:
                    remove_index.append(x)
                x += 1
            if remove_index:
                tmp = 0
                for j in remove_index:
                    food_times.pop(j - tmp)
                    board.pop(j - tmp)
                    tmp += 1
            n = len(food_times)


def solution2(food_times, k):
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


def solution3(food_times, k):
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
    minimum_list = deque(sorted(dic_times.key()))
    minimum = minimum_list.popleft()
    prev_minimum = 0

    print(dic_index, dic_times, minimum_list, k)
    for _ in range(k):
        new_k = k - (len(dic_index) * (minimum - prev_minimum))

        if new_k >= 0:
            prev_minimum = minimum
            k = new_k

            print(dic_times)
            index = dic_times[minimum]
            dic_times.pop(minimum)
            for i in index:
                dic_index.pop(i)

            minimum = minimum_list.popleft()
            print(dic_index, dic_times, minimum_list, k)
        else:
            keys = sorted(dic_index.keys())
            print(keys, k)
            return keys[k] + 1
food_times = [1,2,3,4,5,6,6,7,8,9,10,11]
k = 70
print(solution(food_times.copy(), k))
print("*" * 100)
print("*" * 100)
print("*" * 100)
print("*" * 100)
print(solution3(food_times.copy(), k))