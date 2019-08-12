def combination(arr, length, visit=[]):
    if len(visit) == length:
        yield visit
    else:
        for i in range(len(arr)):
            if arr[i] in visit: continue
            visit.append(arr[i])
            yield from combination(arr[i:], length, visit)
            visit.pop()


print("this is a combination generator")
num = 0
for combine in combination(["A", "B", "C", "D", "E"], 3):
    num += 1
    print(num, combine)
print("*" * 100)


def ordered_power_set(arr,visit=[]):
    yield visit
    for content in arr:
        if content in visit: continue
        visit.append(content)
        yield from ordered_power_set(arr, visit)
        visit.pop()


print("this is an ordered power set generator")
num = 0
for magic in ordered_power_set(["A", "B", "C", "D", "E"]):
    num += 1
    print(num, magic)