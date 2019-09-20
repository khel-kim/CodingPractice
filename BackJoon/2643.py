n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]


def check(paper1, paper2):
    if paper1[0] >= paper2[0] and paper1[1] >= paper2[1]:
        return True
    elif paper1[1] >= paper2[0] and paper1[0] >= paper2[1]:
        return True
    else:
        return False


candi = paper
count = 0
while candi:
    new_candi = []
    for paper2 in candi:
        flag = False
        for paper1 in candi:
            if paper1 == paper2:
                continue
            if check(paper1, paper2):
                flag = True
                break
        if flag:
            new_candi.append(paper2)
    candi = new_candi
    count += 1

print(count)
