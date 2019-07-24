T = int(input())
data = []
for _ in range(T):
    n = input()
    data.append(list(map(int, input().split())))


def sol(case):
    reverse_case = case[::-1]

    profit = 0
    max = 0
    for stock in reverse_case:
        if stock > max:
            max = stock
        elif stock < max:
            profit += max - stock
    return profit


for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))
