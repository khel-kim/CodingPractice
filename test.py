def search(line):
    setting = []
    for i in range(0, n - 1):
        if line[i] - line[i + 1] == 0:
            continue
        elif line[i] - line[i + 1] == -1:
            if i - l + 1 < 0:
                return 0
            for index in range(i - l + 1, i+1):
                if line[index] == line[i]:
                    if index in setting:
                        return 0
                    setting.append(index)
                else:
                    return 0
        elif line[i] - line[i + 1] == 1:
            if i + l + 1 > n:
                return 0
            for index in range(i + 1, i + l + 1):
                if line[index] == line[i + 1]:
                    if index in setting:
                        return 0
                    setting.append(index)
                else:
                    return 0
        else:
            return 0
    return 1


numbers = "1234567898"
n = len(numbers)
l = 1
tmp = list(map(int, numbers))
print(search(tmp))
"""
(3, 2, 2, 1, 1, 1)
(3, 3, 2, 1, 1, 1)
(3, 3, 2, 1, 1, 2)
(3, 3, 3, 2, 3, 3)
(3, 3, 2, 2, 3, 3)
(3, 3, 3, 2, 1, 2)
"""