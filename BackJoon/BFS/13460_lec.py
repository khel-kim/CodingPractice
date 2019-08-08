n, m = map(int, input().split())  # 0번째
board = []
for i in range(n):
    tmp = list(input())
    for j, char in enumerate(tmp):
        if char == "B":
            b_location = (i, j)
        elif char == "R":
            r_location = (i, j)
        elif char == "O":
            o_location = (i, j)
    board.append(tmp)


def move_with_direction(main_ball, compare_ball, direction):  # 1번째
    if main_ball == (-100, -100):
        return main_ball
    while True:
        main_x, main_y = main_ball
        dx, dy = direction
        if board[main_x + dx][main_y + dy] != "#":
            if (main_x + dx, main_y + dy) != compare_ball:
                main_x += dx
                main_y += dy
                if (main_x, main_y) == o_location:
                    main_x = -100
                    main_y = -100
                    return main_x, main_y
        if (main_x, main_y) == main_ball:
            return main_x, main_y
        else:
            main_ball = main_x, main_y


def going(red_ball, blue_ball, direction):  # 2번째
    while True:
        red_x, red_y = move_with_direction(red_ball, blue_ball, direction)
        blue_x, blue_y = move_with_direction(blue_ball, red_ball, direction)
        if (red_x, red_y) == red_ball and (blue_x, blue_y) == blue_ball:
            break
        else:
            red_ball = red_x, red_y
            blue_ball = blue_x, blue_y
    return red_ball, blue_ball


pair_movements1 = [(0, -1), (0, 1)]  # 3번째
pair_movements2 = [(1, 0), (-1, 0)]
queue = [(r_location, b_location, (0, -1), 1),
         (r_location, b_location, (0, 1), 1),
         (r_location, b_location, (1, 0), 1),
         (r_location, b_location, (-1, 0), 1)]

answer = -1
while queue:
    current = queue.pop(0)
    r_cur, b_cur, direction, depth = current
    r_move, b_move = going(r_cur, b_cur, direction)
    if b_move == (-100, - 100): continue
    if (r_cur, b_cur) == (r_move, b_move): continue
    if r_move == (-100, -100):
        answer = depth
        break
    if depth == 10: continue
    if direction in pair_movements1:
        for movement in pair_movements2:
            queue.append((r_move, b_move, movement, depth + 1))
    else:
        for movement in pair_movements1:
            queue.append((r_move, b_move, movement, depth + 1))

print(answer)
