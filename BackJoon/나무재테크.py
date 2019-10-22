from collections import deque
n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
trees = [list(map(int, input().split())) for _ in range(m)]

board = [[5] * n for _ in range(n)]
adjacent = ((1, 0), (0, 1), (-1, 0), (0, -1),
            (1, 1), (-1, -1), (1, -1), (-1, 1),)

# tree init
tree_dic = {(x, y): deque([]) for x in range(n) for y in range(n)}
for x, y, age in trees:
    tree_dic[(x - 1, y - 1)].append(age)


def spring_summer(tree_dic, board):
    global reproduce_trees
    reproduce_trees = deque([])
    for (x, y), trees in tree_dic.items():
        new_trees = deque([])
        dead_trees = 0
        for age in trees:
            if board[x][y] >= age:
                board[x][y] -= age
                new_trees.append(age+1)
                if (age + 1) % 5 == 0:
                    reproduce_trees.append((x, y))
            else:
                dead_trees += age // 2
        tree_dic[(x, y)] = new_trees
        board[x][y] += dead_trees


def fall(reproduce_trees):
    for x, y in reproduce_trees:
        for dx, dy in adjacent:
            nx, ny = x + dx, y + dy
            if not 0 <= nx < n: continue
            if not 0 <= ny < n: continue
            tree_dic[(nx, ny)].appendleft(1)


def winter(board, a):
    for x in range(n):
        for y in range(n):
            board[x][y] += a[x][y]


for _ in range(k):
    spring_summer(tree_dic, board)
    fall(reproduce_trees)
    winter(board, a)

count = 0
for value in tree_dic.values():
    count += len(value)

print(count)
