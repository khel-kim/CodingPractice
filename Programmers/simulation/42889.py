def solution(N, stages):
    stages_dic = {}
    stay_dic = {}
    for i in range(1, N+2):
        stages_dic[i] = 0
        stay_dic[i] = 0
    for i in stages:
        stay_dic[i] += 1
        for j in range(1, i+1):
            stages_dic[j] += 1

    fail_rate = {}
    for i in range(1, N+2):
        if stages_dic[i] != 0:
            fail_rate[i] = stay_dic[i] / stages_dic[i]
        else:
            fail_rate[i] = 0

    result = []
    for i, rate in sorted(fail_rate.items(), key=lambda x: (x[1], -x[0]),reverse=True):
        if i == N+1:
            continue
        else:
            result.append(i)
    return result