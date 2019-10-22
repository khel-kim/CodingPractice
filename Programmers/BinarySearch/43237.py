budgets = [120, 110, 140, 150]
M = 485


def solution(budgets, M):
    start = 0
    end = max(budgets)
    while start <= end:
        m = (start + end) // 2
        summation = 0
        for budget in budgets:
            if budget <= m:
                summation += budget
            else:
                summation += m
        if summation == M:
            return m
        elif summation < M:
            start = m + 1
        else:
            end = m - 1
    return start-1


print(solution(budgets, M))
