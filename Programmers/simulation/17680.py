cacheSize = 3
cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']

from collections import deque
cache = deque([])
time = 0
for i in range(len(cities)):
    city = cities[i].lower()

    flag = False
    for index in range(len(cache)):
        if cache[index] == city:
            flag = True
            cache.append(cache[index])
            cache.pop(index)
            break

    if flag:
        time += 1
    else:
        time += 5

    if flag:
        continue
    else:
        if len(cache) < cacheSize:
            cache.append(city)
        else:
            if not cache: continue
            cache.popleft()
            cache.append(city)
print(time)
