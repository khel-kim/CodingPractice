def rotation_90(points):
    """
    [[0, 1],[-1, 0]]
    """
    last_point = points[-1]
    last_rotated_points = (last_point[1], -last_point[0])
    rotated_points = []
    for point in points[-2::-1]:
        new_x = point[1] + last_point[0] - last_rotated_points[0]
        new_y = -point[0] + last_point[1] - last_rotated_points[1]
        rotated_points.append((new_x, new_y))
        # board[new_x, new_y]
    return rotated_points


print(rotation_90([(2, 4), (1, 4), (1, 3)]))