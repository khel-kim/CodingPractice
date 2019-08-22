length = int(input())
n = int(input())
repairs = list(map(int, input().split()))
time = list(map(int, input().split()))
distance = [0] * (n + 2)
for i in range(n+1):
    distance[i + 1] = distance[i] + repairs[i]


dp = [[0, [0]] for _ in range(n + 2)]

print(length)
print(repairs)
print(time)
print(distance)

current = 0
if distance[-1] < length:
    print(0)
    print(0)
    print()
else:
    for i in range(1, n + 2):
        if current + length >= distance[i]:
            print(current + length)
            print(distance[i])
            dp[i] = dp[i-1]
        else:
            minimum = distance[i] - length
            min_time = 10000
            index = None
            for j in range(1, i):
                if distance[j] < minimum:
                    continue
                if min_time > dp[j][0] + time[j-1]:
                    min_time = dp[j][0] + time[j-1]
                    index = j
            dp[i][0] = min_time
            dp[i][1] = dp[index][1] + [index]
            current = distance[index]
        print(i, dp)
    print(dp)

    print(dp[-1][0])
    print(len(dp[-1][1]) - 1)
    print(" ".join(map(str, dp[-1][1][1:])))

"""
140
5
100 30 100 40 50 60
5 8 4 11 7

101
5
50 50 50 50 50 50
5 8 4 11 7
"""
