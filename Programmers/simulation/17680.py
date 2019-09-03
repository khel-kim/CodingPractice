def solution(cacheSize, cities):
    cache = []
    time = 0
    for i in range(len(cities)):
        city = cities[i].lower()
        flag = False
        for index in range(len(cache)):
            if cache[index] == city:
                flag = True
                tmp = cache.pop(index)
                cache.append(tmp)
                time += 1
                break
        else:
            time += 5
        if flag: continue
        if len(cache) < cacheSize:
            cache.append(city)
        else:
            if not cache: continue
            cache.pop(0)
            cache.append(city)
    return time