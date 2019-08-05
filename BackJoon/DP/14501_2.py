n = int(input())
data = [(0, 0, 0)]
for i in range(n):
    t, p = map(int, input().split())
    data.append((i + 1, t + i, p))  # 시작날짜, 끝날짜, 가격
memo = [0] * (n + 1)
if data[n][1] == n:
    memo[n] = data[n][2]
for day in range(n - 1, 0, -1):
    if data[day][1] > n:
        memo[day] = memo[day + 1]
    elif data[day][1] == n:
        memo[day] = max(memo[day + 1], data[day][2])
    else:
        memo[day] = max(memo[day + 1], memo[data[day][1] + 1] + data[day][2])

print(memo[1])