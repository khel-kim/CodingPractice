import math
n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

print(n + sum([math.ceil((i - b) / c) if i - b > 0 else 0 for i in a]))
