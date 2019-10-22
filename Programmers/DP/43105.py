def solution(triangle):
    height = len(triangle)
    dp = [[triangle[0][0]]]
    for h in range(1, height):
        dp.append([])
        for i in range(h+1):
            if i == 0:
                dp[-1].append(dp[-2][0] + triangle[h][i])
            elif i == h:
                dp[-1].append(dp[-2][-1] + triangle[h][i])
            else:
                dp[-1].append(max(dp[-2][i-1]+triangle[h][i], dp[-2][i]+triangle[h][i]))
    return max(dp[-1])