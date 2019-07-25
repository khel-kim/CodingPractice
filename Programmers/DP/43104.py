def fibo(n):
    memo = []
    for i in range(n + 1):
        if i == 0:
            memo.append(0)
        elif i == 1:
            memo.append(1)
        else:
            memo.append(memo[i - 1] + memo[i - 2])
    return memo


def solution(n):
    fibo_list = fibo(n)
    print(fibo_list)
    height = fibo_list[-1]
    width = fibo_list[-1] + fibo_list[-2]
    return 2 * (height + width)


print(solution(5))