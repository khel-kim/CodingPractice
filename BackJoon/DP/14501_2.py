n = int(input())
data = []
for i in range(n):
    t, p = map(int, input().split())
    data.append((i + 1, t + i, p))  # 시작날짜, 끝날짜, 가격

