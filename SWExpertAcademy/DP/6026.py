T = int(input())
data = []
for _ in range(T):
    n, m = map(int, input().split())
    data.append((n, m))


def combination(n, k):
    w = [[1]]
    k = min(k, n-k)
    for i in range(1, n + 1):
        w.append([])
        for j in range(min(i, k) + 1):
            if j == 0:
                w[-1].append(1)
            elif j == i:
                w[-1].append(1)
            else:
                w[-1].append(w[-2][j-1] + w[-2][j])
    return w[n][k]


def dp(m, n):
    memo = [0] * (m + 1)
    for i in range(1, m+1):
        memo[i] += i ** n
        for j in range(1, i):
            memo[i] -= combination2(i, j) * memo[j]
    return memo[-1]


def combination2(n, m):
    upper = 1
    for i in range(m+1, n +1):
        upper *= i
    down = 1
    for j in range(1, n - m + 1):
        down *= j
    return upper // down


for i, case in enumerate(data):
    m, n = case
    print("#%s" % (i + 1), dp(m,n) % 1000000007)
