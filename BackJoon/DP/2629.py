n = int(input())
chus = list(map(int, input().split()))
k = int(input())
balls = list(map(int, input().split()))


# chus = [1,1, 2, 3, 4,5]
# balls = [1,2,3,4,5,6]
check = [False] * 40001
visit = []
for chu in chus:
    # print("start" + "*" * 100)
    # print(chu)
    # print(visit, "before visit")
    # print(check, "before check")

    visit.append(chu)
    check[chu] = True

    for i in visit[:-1]:
        candi = i + chu
        if check[candi]:
            pass
        else:
            check[candi] = True
            visit.append(candi)

        candi = abs(i - chu)
        if candi == 0:
            continue
        elif check[candi]:
            pass
        else:
            check[candi] = True
            visit.append(candi)

    # print(visit, "after")
    # print(check, "after")

for ball in balls:
    if check[ball]:
        print("Y", end=" ")
    else:
        print("N", end=" ")
print()

"""
2
1 4
2
3 2
"""