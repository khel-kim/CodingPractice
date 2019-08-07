T = int(input())
data = []
for _ in range(T):
    n = int(input())
    board = []
    for __ in range(n):
        tmp = list(map(int, input().split()))
        board.append(tmp)
    data.append((n, board))


def sol(case):
    n, board = case

    people = []  # (x, y), 계단1까지의 거리, 계단2까지의 거리
    stairs = []  # (x, y), 소요시간
    for x in range(n):
        for y in range(n):
            if board[x][y] != 0 and board[x][y] != 1:
                stairs.append(((x, y), board[x][y]))

    for x in range(n):
        for y in range(n):
            if board[x][y] == 1:
                stair_time = []
                for stair in stairs:
                    location, time = stair
                    stair_time.append(abs(x - location[0]) + abs(y - location[1]))
                tmp = [(x, y)]
                tmp.extend(stair_time)
                people.append(tmp)

    def DFS(array, index=0, visit1=[], visit2=[]):
        if index == len(array):
            yield visit1, visit2
        else:
            for i in range(2):
                if i == 0:
                    visit1.append(array[index])
                    yield from DFS(array, index+1, visit1, visit2)
                    visit1.pop()
                else:
                    visit2.append(array[index])
                    yield from DFS(array, index+1, visit1, visit2)
                    visit2.pop()

    def get_time(people, stair, stair_type):
        n_people = len(people)
        stair_time = stair[1]

        cur_stair = []
        n_complete_people = 0
        cur_time = 0
        while n_complete_people != n_people:
            cur_time += 1
            cur_stair_tmp = []
            for person in cur_stair:
                person[1] += 1
                if person[1] >= stair_time:
                    n_complete_people += 1
                else:
                    cur_stair_tmp.append(person)
            cur_stair = cur_stair_tmp
            if len(cur_stair) == 3:
                continue

            new_people = []
            for person in people:
                if cur_time >= person[stair_type] and len(cur_stair) < 3:
                    cur_stair.append([person, 0])
                else:
                    new_people.append(person)
            people = new_people
        return cur_time + 1

    minimum = 1000000
    for group1, group2 in DFS(people):
        people_stair1 = sorted(group1, key=lambda x: x[1])
        people_stair2 = sorted(group2, key=lambda x: x[2])
        time1 = get_time(people_stair1, stairs[0], 1)
        time2 = get_time(people_stair2, stairs[1], 2)
        if minimum > max(time1, time2):
            minimum = max(time1, time2)
    return minimum


for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))
