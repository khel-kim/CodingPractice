import itertools
combinations = itertools.combinations

n = int(input())
board = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    board.append(tmp)

minimum = 101
for team1 in combinations(list(range(1, n)), n//2):
    team2 = [0]
    for i in range(1, n):
        if i in team1: continue
        team2.append(i)
    team1_ability = 0
    team2_ability = 0
    for i in team1:
        for j in team1:
            team1_ability += board[i][j]
    for i in team2:
        for j in team2:
            team2_ability += board[i][j]
    differential = abs(team1_ability - team2_ability)
    if minimum > differential:
        minimum = differential

print(minimum)
