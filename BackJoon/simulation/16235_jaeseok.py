def s_s(size, matrix):
    for s_s_i in range(size):
        for s_s_j in range(size):
            filed_soils = matrix[s_s_i][s_s_j][0]  # 양분상태
            tree_status = matrix[s_s_i][s_s_j][1]  # 나무들
            if len(tree_status) == 0:
                continue
            check = 0
            tree_status2 = []
            for index_num in range(len(tree_status)):  # for index_num, tree in enumerate(tree_status):
                if check == 0:
                    filed_soils -= tree_status[index_num]
                    tree_status[index_num] += 1
                    if filed_soils < 0:
                        tree_status2 = tree_status[:index_num]
                        filed_soils += tree_status[index_num]
                        filed_soils += tree_status[index_num]//2
                        check = 1
                else:
                    filed_soils += tree_status[index_num]//2
            if check == 0:
                tree_status2 = tree_status
            matrix[s_s_i][s_s_j] = [filed_soils, tree_status2]
def birth_tree(num_x, num_y, size, matrix):
    birth_square = [(1, 0), (1, 1), (0, 1), (-1, 1),
                    (-1, 0), (-1, -1), (0, -1), (1, -1)]
    add_tree = [(x + num_x, y + num_y) for x, y in birth_square]
    for x_num, y_num in add_tree:
        if (0 <= x_num < size) and (0 <= y_num < size):
            matrix[x_num][y_num][1] = [1] + matrix[x_num][y_num][1]
def fall(size, matrix):
    for fall_i in range(size):
        for fall_j in range(size):
            field_status = matrix[fall_i][fall_j][1]
            for old in field_status:
                if old % 5 == 0:
                    birth_tree(fall_i, fall_j, size, matrix)
def winter(size, soil_matrix, feild_matrix):
    for winter_i in range(size):
        for winter_j in range(size):
            feild_matrix[winter_i][winter_j][0] += soil_matrix[winter_i][winter_j]
n, m, k = map(int, input().split())
soil = []
tree_feild = []
for line in range(n):
    line_soil = list(map(int, input().split()))
    soil.append(line_soil)
for i in range(n):
    tree_feild.append([[5, []] for j in range(n)])
for tree in range(m):
    i, j, tree_old = tuple(map(int, input().split()))
    tree_feild[i-1][j-1][1] = tree_feild[i-1][j-1][1] + [tree_old]
#
# for i in range(n):
#     for j in range(n):
#         tree_feild[i][j][1].sort()
for year in range(k):
    s_s(n, tree_feild)
    fall(n, tree_feild)
    winter(n, soil, tree_feild)
sum_old = 0
for i in range(n):
    for j in range(n):
        sum_old += len(tree_feild[i][j][1])
print(sum_old)