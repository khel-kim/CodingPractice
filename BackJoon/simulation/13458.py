import math
n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

count = n
tmp1 = [i - b if i - b > 0 else 0 for i in a]
tmp2 = [math.ceil(j / c) for j in tmp1]

print(count + sum(tmp2))

"""
3
1 1 1
2 2
"""