n = int(input())
curves = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    curves.append((tmp[1], tmp[0], tmp[2], tmp[3]))


def rotation_90(points):
    global max_x, max_y
    """
    rotation matrix: [[0, 1],[-1, 0]]
    """
    last_point = points[-1]
    rotated_last_points = (last_point[1], -last_point[0])
    difference_vector_x = last_point[0] - rotated_last_points[0]
    difference_vector_y = last_point[1] - rotated_last_points[1]
    rotated_points = []
    for point in points[-2::-1]:
        new_x = point[1] + difference_vector_x
        new_y = -point[0] + difference_vector_y
        rotated_points.append((new_x, new_y))
        board[new_x][new_y] = 1
        if max_x < new_x:
            max_x = new_x
        if max_y < new_y:
            max_y = new_y
    return rotated_points


board = [[0] * 101 for _ in range(101)]
moves = ((0, 1),
         (-1, 0),
         (0, -1),
         (1, 0),)
max_x = 0
max_y = 0
for curve in curves:
    current_curve = []

    row, column, direction, generation = curve
    current_curve.append((row, column))
    board[row][column] = 1  # 현재 위치

    nx, ny = row + moves[direction][0], column + moves[direction][1]
    current_curve.append((nx, ny))
    board[nx][ny] = 1  # 0세대

    max_x = max(row, nx, max_x)
    max_y = max(column, ny, max_y)

    for iteration in range(1, generation+1):
        current_curve.extend(rotation_90(current_curve))

count = 0
for x in range(max_x):
    for y in range(max_y):
        if board[x][y] == 1 and board[x+1][y] == 1 and board[x][y+1] == 1 and board[x+1][y+1] == 1:
            count += 1
print(count)
