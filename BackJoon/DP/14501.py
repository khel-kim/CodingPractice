n = int(input())
data = []
for i in range(n):
    t, p = map(int, input().split())
    data.append((i + 1, t + i, p))  # 시작날짜, 끝날짜, 가격

sorted_data = sorted(data, key=lambda x: (x[1]))
D = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(i, n + 1):
        for index in range(n):
            start, end, cost = sorted_data[index]
            if end <= j:
                for k in range(i-1, start):
                    D[i][j] = max(D[i][j], D[i-1][k] + cost)
            elif end > j:
                break
            D[i][j] = max(D[i][j], D[i-1][j])
print(D[-1][-1])
